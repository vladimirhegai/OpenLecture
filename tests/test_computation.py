import math

import pytest

from open_lecture.circuits import parse, simulate_dc
from open_lecture.errors import DomainError

DIVIDER = """circuit "Voltage divider"
V1 vin 0 DC 10V
R1 vin vout 2kOhm
R2 vout 0 3kOhm
analyze dc
probe V(vout)
probe I(V1)
"""


def test_real_math(client):
    result = client.post("/api/v1/math/evaluate", json={"expression": "1/3 + 1/6"}).json()
    assert result["verified"] and result["exact"] == "1/2"
    derivative = client.post(
        "/api/v1/math/evaluate", json={"operation": "differentiate", "expression": "x**3"}
    ).json()
    assert derivative["exact"] == "3*x**2"
    roots = client.post("/api/v1/math/evaluate", json={"operation": "solve", "expression": "x**2 - 4"}).json()
    assert set(roots["solutions"]) == {"-2", "2"}
    for expression in [
        "__import__('os').getcwd()",
        "x.__class__",
        "[1,2]",
        "9**999999",
        "1/0",
        "(lambda: 1)()",
        "exp(1000000000000)",
    ]:
        assert client.post("/api/v1/math/evaluate", json={"expression": expression}).status_code == 422


def test_binomial_card_and_artifact_reference(client, course):
    result = client.post("/api/v1/math/binomial", json={"n": 10, "p": 0.35, "k": 3}).json()
    assert result["outputs"]["probability_exact"] == pytest.approx(math.comb(10, 3) * 0.35**3 * 0.65**7)
    assert sum(result["chart"]["y"]) == pytest.approx(1)
    assert client.post("/api/v1/math/binomial", json={"n": 2, "p": 0.5, "k": 3}).status_code == 422
    base = f"/api/v1/courses/{course}"
    artifact = client.post(base + "/math-cards/binomial", json={"n": 10, "p": 0.5, "k": 5}).json()
    doc = client.post(
        base + "/documents",
        json={
            "title": "Probability",
            "blocks": [{"type": "artifact_reference", "artifact_id": artifact["id"]}],
        },
    ).json()["document"]
    assert doc["blocks"][0]["artifact_id"] == artifact["id"]


def test_divider_simulation_is_persisted_and_embeddable(client, course):
    base = f"/api/v1/courses/{course}"
    circuit = client.post(base + "/circuits", json={"definition": DIVIDER}).json()
    assert ".op" in circuit["payload"]["spice_netlist"]
    result = client.post(base + f"/circuits/{circuit['id']}/simulate").json()
    data = result["payload"]
    assert data["node_voltages"]["vout"] == pytest.approx(6)
    assert data["branch_currents"]["R1"] == pytest.approx(0.002)
    assert data["component_power"]["V1"] == pytest.approx(-0.02)
    assert data["power_balance_watts"] == pytest.approx(0, abs=1e-12)
    assert client.get(base + f"/artifacts/{result['id']}").json()["payload"] == data
    doc = client.post(
        base + "/documents",
        json={
            "title": "Divider example",
            "blocks": [
                {"type": "artifact_reference", "artifact_id": circuit["id"]},
                {"type": "artifact_reference", "artifact_id": result["id"]},
            ],
        },
    ).json()["document"]
    assert len(doc["blocks"]) == 2


def test_current_source_and_circuit_failures():
    result = simulate_dc(parse('circuit "Current source"\nI1 0 a DC 2mA\nR1 a 0 1kOhm\nanalyze dc'))
    assert result["node_voltages"]["a"] == pytest.approx(2)
    for text in [
        DIVIDER + "\n.include /secret",
        DIVIDER.replace("2kOhm", "-1Ohm"),
        DIVIDER.replace("analyze dc", "analyze transient 0s 1s 1ms"),
        DIVIDER + "\nprobe V(unknown)",
    ]:
        with pytest.raises(DomainError):
            parse(text)
    with pytest.raises(DomainError, match="floating"):
        simulate_dc(parse('circuit "Floating"\nR1 a b 1kOhm\nR2 c 0 1kOhm\nanalyze dc'))
