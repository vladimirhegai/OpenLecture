from typing import Annotated, Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, model_validator

from . import digital, schematic
from .errors import DomainError


def new_id() -> str:
    return str(uuid4())


class Model(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True, allow_inf_nan=False)


class Citation(Model):
    source_id: UUID
    version: int = Field(ge=1)
    chunk_id: UUID


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list | tuple):
        for item in value:
            yield from strings(item)
    elif isinstance(value, BaseModel):
        for name in type(value).model_fields:
            yield from strings(getattr(value, name))


class BaseBlock(Model):
    id: UUID = Field(default_factory=uuid4)
    citations: list[Citation] = Field(default_factory=list, max_length=30)

    @model_validator(mode="after")
    def valid_schematics(self):
        """Markdown text may embed ```schematic fences; reject drawings that would not render."""
        try:
            for text in strings(self):
                if "```schematic" in text:
                    schematic.check_fences(text)
                if "```digital" in text:
                    digital.check_fences(text)
            if getattr(self, "language", None) == "digital":
                digital.check(self.text)
        except DomainError as error:
            raise ValueError(error.message) from None
        return self


class Paragraph(BaseBlock):
    type: Literal["paragraph"] = "paragraph"
    text: str = Field(min_length=1, max_length=30000)


class Heading(BaseBlock):
    type: Literal["heading"] = "heading"
    text: str = Field(min_length=1, max_length=300)
    level: int = Field(default=2, ge=1, le=6)


class Equation(BaseBlock):
    type: Literal["equation"] = "equation"
    latex: str = Field(min_length=1, max_length=5000)
    display: bool = True


class ListBlock(BaseBlock):
    type: Literal["list"] = "list"
    items: list[str] = Field(min_length=1, max_length=100)
    ordered: bool = False


class Callout(BaseBlock):
    type: Literal["callout"] = "callout"
    text: str = Field(min_length=1, max_length=10000)
    tone: Literal["info", "warning", "tip", "reminder"] = "info"


class Table(BaseBlock):
    type: Literal["table"] = "table"
    columns: list[str] = Field(min_length=1, max_length=20)
    rows: list[list[str]] = Field(max_length=100)

    @model_validator(mode="after")
    def rectangular(self):
        if any(len(row) != len(self.columns) for row in self.rows):
            raise ValueError("Every table row must match the column count")
        return self


class Code(BaseBlock):
    type: Literal["code"] = "code"
    language: str = Field(default="text", max_length=40)
    text: str = Field(max_length=30000)


class SolutionStep(Model):
    explanation: str = Field(min_length=1, max_length=3000)
    latex: str = Field(default="", max_length=3000)


class PracticeProblem(BaseBlock):
    type: Literal["practice_problem"] = "practice_problem"
    title: str = Field(default="", max_length=200)
    prompt: str = Field(min_length=1, max_length=10000)
    solution: str = Field(default="", max_length=10000)
    steps: list[SolutionStep] = Field(default_factory=list, max_length=30)
    answer: str = Field(default="", max_length=3000)
    origin: Literal["original", "source"] = "original"
    difficulty: Literal["introductory", "intermediate", "advanced"] = "introductory"

    @model_validator(mode="after")
    def source_required(self):
        if self.origin == "source" and not self.citations:
            raise ValueError("Source-derived problems require a citation; label invented problems original")
        if not self.solution and not self.steps:
            raise ValueError("A practice problem needs solution steps or a solution")
        return self


class WorkedExample(BaseBlock):
    type: Literal["worked_example"] = "worked_example"
    title: str = Field(min_length=1, max_length=200)
    prompt: str = Field(min_length=1, max_length=10000)
    steps: list[SolutionStep] = Field(min_length=1, max_length=30)
    answer: str = Field(default="", max_length=3000)


class Schematic(BaseBlock):
    type: Literal["schematic"] = "schematic"
    source: str = Field(min_length=1, max_length=8000)
    caption: str = Field(default="", max_length=500)

    @model_validator(mode="after")
    def renders(self):
        try:
            schematic.check(self.source)
        except DomainError as error:
            raise ValueError(error.message) from None
        return self


class ArtifactReference(BaseBlock):
    type: Literal["artifact_reference"] = "artifact_reference"
    artifact_id: UUID
    caption: str = Field(default="", max_length=500)


class DerivationStep(Model):
    explanation: str = Field(min_length=1, max_length=3000)
    latex: str = Field(min_length=1, max_length=3000)


class Derivation(BaseBlock):
    type: Literal["derivation"] = "derivation"
    title: str = Field(min_length=1, max_length=300)
    steps: list[DerivationStep] = Field(min_length=1, max_length=40)


class Solution(BaseBlock):
    type: Literal["solution"] = "solution"
    title: str = Field(default="Worked solution", max_length=300)
    text: str = Field(min_length=1, max_length=10000)
    collapsed: bool = True


Block = Annotated[
    Paragraph
    | Heading
    | Equation
    | ListBlock
    | Callout
    | Table
    | Code
    | PracticeProblem
    | WorkedExample
    | Schematic
    | ArtifactReference
    | Derivation
    | Solution,
    Field(discriminator="type"),
]


class CourseCreate(Model):
    code: str = Field(min_length=1, max_length=40)
    title: str = Field(min_length=1, max_length=200)


class FolderCreate(Model):
    title: str = Field(min_length=1, max_length=200)
    parent_id: UUID | None = None


class DocumentCreate(Model):
    schema_version: Literal[1] = 1
    title: str = Field(min_length=1, max_length=300)
    document_type: Literal["study_notes", "revision_sheet", "practice_set", "reference"] = "study_notes"
    academic_week: int | None = Field(default=None, ge=1, le=60)
    topic_keys: list[Annotated[str, Field(pattern=r"^[a-z0-9_]{1,80}$")]] = Field(
        default_factory=list, max_length=30
    )
    folder_id: UUID | None = None
    blocks: list[Block] = Field(default_factory=list, max_length=500)
    actor: Literal["student", "agent"] = "student"
    separate_copy: bool = False
    idempotency_key: str | None = Field(default=None, min_length=1, max_length=200)

    @model_validator(mode="after")
    def unique_blocks(self):
        if len({block.id for block in self.blocks}) != len(self.blocks):
            raise ValueError("Block IDs must be unique within a document")
        self.topic_keys = sorted(set(self.topic_keys))
        return self


class BlockOperation(Model):
    op: Literal["insert", "replace", "remove", "move"]
    block_id: UUID | None = None
    block: Block | None = None
    after_id: UUID | None = None

    @model_validator(mode="after")
    def valid_operation(self):
        if self.op in ("insert", "replace") and self.block is None:
            raise ValueError("insert/replace require a block")
        if self.op != "insert" and self.block_id is None:
            raise ValueError("replace/remove/move require block_id")
        if self.op == "replace" and self.block.id != self.block_id:
            raise ValueError("Replacement must preserve the block ID")
        if self.op in ("remove", "move") and self.block is not None:
            raise ValueError("remove/move do not accept a block")
        if self.op in ("remove", "replace") and self.after_id is not None:
            raise ValueError("after_id is only valid for insert/move")
        if self.op == "insert" and self.block_id is not None:
            raise ValueError("insert uses the new block's ID")
        return self


class DocumentEdit(Model):
    expected_revision: int = Field(ge=1)
    title: str | None = Field(default=None, min_length=1, max_length=300)
    folder_id: UUID | None = None
    operations: list[BlockOperation] = Field(default_factory=list, max_length=100)
    actor: Literal["student", "agent"] = "student"


class RevisionRequest(Model):
    expected_revision: int = Field(ge=1)
    actor: Literal["student", "agent"] = "student"


class ChatCreate(Model):
    title: str = Field(min_length=1, max_length=200)


class DocumentReference(Model):
    document_id: UUID
    revision: int = Field(ge=1)
    block_id: UUID | None = None


class MessageCreate(Model):
    role: Literal["user", "assistant"]
    content: str = Field(min_length=1, max_length=30000)
    references: list[DocumentReference] = Field(default_factory=list, max_length=20)


class AgentRunRequest(Model):
    provider: Literal["claude", "codex"]
    model: str = Field(default="default", pattern=r"^[A-Za-z0-9][A-Za-z0-9._\-]{0,79}$")
    effort: str | None = Field(default=None, pattern=r"^[A-Za-z0-9][A-Za-z0-9._\-]{0,79}$")
    content: str = Field(min_length=1, max_length=8000)
    document: DocumentReference | None = None
    source_id: UUID | None = None
    source_page: int | None = Field(default=None, ge=1, le=2000)


class ModelChoice(Model):
    provider: Literal["claude", "codex"]
    model: str = Field(default="default", pattern=r"^[A-Za-z0-9][A-Za-z0-9._\-]{0,79}$")
    effort: str | None = Field(default=None, pattern=r"^[A-Za-z0-9][A-Za-z0-9._\-]{0,79}$")


class SettingsUpdate(Model):
    reading_model: ModelChoice


class WeekGenerate(ModelChoice):
    regenerate: bool = False


class ReadRequest(Model):
    pages: list[Annotated[int, Field(ge=1, le=2000)]] | None = Field(default=None, max_length=500)


class ViewerState(Model):
    document_id: UUID | None = None
    revision: int | None = Field(default=None, ge=1)
    block_id: UUID | None = None

    @model_validator(mode="after")
    def valid_reference(self):
        if self.document_id is None and (self.revision is not None or self.block_id is not None):
            raise ValueError("revision/block_id require document_id")
        return self


class ContextRequest(Model):
    query: str = Field(min_length=1, max_length=8000)
    token_budget: int = Field(default=6000, ge=1000, le=32000)


class ActionRequest(Model):
    intent: Literal["question", "create", "edit", "separate"]
    document_type: Literal["study_notes", "revision_sheet", "practice_set", "reference"] = "study_notes"
    academic_week: int | None = Field(default=None, ge=1, le=60)
    topic_keys: list[str] = Field(default_factory=list, max_length=30)
    target_document_id: UUID | None = None


class MathRequest(Model):
    operation: Literal["evaluate", "differentiate", "solve"] = "evaluate"
    expression: str = Field(min_length=1, max_length=500)
    variable: Literal["x", "y", "t", "n"] = "x"
    values: dict[Literal["x", "y", "t", "n"], float] = Field(default_factory=dict)


class BinomialRequest(Model):
    n: int = Field(ge=1, le=100)
    p: float = Field(ge=0, le=1)
    k: int = Field(ge=0, le=100)

    @model_validator(mode="after")
    def valid_k(self):
        if self.k > self.n:
            raise ValueError("k must be no greater than n")
        return self


class CircuitRequest(Model):
    definition: str = Field(min_length=1, max_length=20000)


class DigitalRequest(Model):
    source: str = Field(min_length=1, max_length=30000)


class SchematicRequest(Model):
    source: str = Field(min_length=1, max_length=8000)


class CourseTopic(Model):
    key: str = Field(pattern=r"^[a-z0-9_]{1,80}$")
    title: str = Field(min_length=1, max_length=200)
    week: int | None = Field(default=None, ge=1, le=60)
    reading: str = Field(default="", max_length=200)


class CourseProfileUpdate(Model):
    expected_revision: int = Field(ge=0)
    term: str = Field(default="", max_length=100)
    pack_ids: list[str] = Field(default_factory=list, max_length=10)
    topics: list[CourseTopic] = Field(default_factory=list, max_length=200)
    syllabus_citations: list[Citation] = Field(default_factory=list, max_length=30)
    study_preferences: list[Annotated[str, Field(max_length=500)]] = Field(
        default_factory=list, max_length=15
    )


class NormalRequest(Model):
    distribution: Literal["normal"]
    mean: float = Field(default=0, ge=-1e6, le=1e6)
    std: float = Field(default=1, gt=1e-9, le=1e6)
    x: float = Field(ge=-1e6, le=1e6)


class PoissonRequest(Model):
    distribution: Literal["poisson"]
    rate: float = Field(gt=0, le=100)
    x: int = Field(ge=0, le=10000)


class ExponentialRequest(Model):
    distribution: Literal["exponential"]
    rate: float = Field(gt=1e-9, le=1e6)
    x: float = Field(ge=-1e6, le=1e6)


class UniformRequest(Model):
    distribution: Literal["uniform"]
    low: float = Field(ge=-1e6, le=1e6)
    high: float = Field(ge=-1e6, le=1e6)
    x: float = Field(ge=-1e6, le=1e6)

    @model_validator(mode="after")
    def valid_range(self):
        if self.high - self.low < 1e-9:
            raise ValueError("high must exceed low by at least 1e-9")
        return self


class GammaRequest(Model):
    distribution: Literal["gamma"]
    shape: float = Field(ge=1, le=100)
    scale: float = Field(gt=1e-9, le=1e6)
    x: float = Field(ge=-1e6, le=1e6)


DistributionRequest = Annotated[
    NormalRequest | PoissonRequest | ExponentialRequest | UniformRequest | GammaRequest,
    Field(discriminator="distribution"),
]


class LinearODERequest(Model):
    order: Literal[1, 2] = 1
    a: float = Field(ge=-1000, le=1000)
    b: float = Field(default=0, ge=-1000, le=1000)
    forcing: float = Field(default=0, ge=-1e6, le=1e6)
    y0: float = Field(default=0, ge=-1e6, le=1e6)
    dy0: float = Field(default=0, ge=-1e6, le=1e6)
    duration: float = Field(gt=0, le=1000)
    samples: int = Field(default=101, ge=2, le=501)

    @model_validator(mode="after")
    def valid_first_order(self):
        if self.order == 1 and (self.b != 0 or self.dy0 != 0):
            raise ValueError("First-order ODEs use a, forcing, and y0; b and dy0 apply only to second order")
        if self.duration * (abs(self.a) + abs(self.b) + 1) > 5000:
            raise ValueError("Coefficient-time product exceeds the supported range")
        return self


class LogicRequest(Model):
    expression: str = Field(min_length=1, max_length=300)
    variables: list[Annotated[str, Field(pattern=r"^[A-Za-z][A-Za-z0-9_]{0,15}$")]] = Field(
        min_length=1, max_length=6
    )

    @model_validator(mode="after")
    def unique_variables(self):
        if len(set(self.variables)) != len(self.variables):
            raise ValueError("Logic variables must be unique")
        return self
