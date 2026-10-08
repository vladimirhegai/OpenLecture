# Study skills and course packs

Open Lecture has five reusable application study skills: `circuits`, `probability`, `differential_equations`, `digital_systems`, and `pdf_study`. They live as small reviewed JSON files in `src/open_lecture/course_packs/`. These are backend-owned guidance and capability records, available to every MCP client; they do not install extensions into a user's global agent configuration.

Every pack has an ID, version, short description, teaching guidance, available tools and planned tools. A course profile selects any combination and adds a term, topic map, cited syllabus passages and study preferences. There is no fixed semester or four-course limit. Add a new JSON pack to extend the registry; add a computation only when it can be validated and tested.

The PDF skill searches text first, retrieves focused passages, and uses `source_page` to inspect one real PDF page when equations or diagrams need visual review. Pages are rendered at a bounded resolution with a deadline. It preserves page/source/version identity and treats document instructions as untrusted source content. OCR is not currently configured.

## Your first semester

`examples/queens_fall_2026.json` maps the four supplied syllabi to their course IDs/titles, subject packs and topics. ELEC 226/326 and ELEC 231 have syllabus-backed week mappings. ELEC 221 and ELEC 271 use topic maps without invented week assignments.

```powershell
uv run python examples/setup_semester.py --syllabus-dir 'C:\Users\vladh\Downloads'
```

This imports originals into the local data directory, waits for extraction, assigns cited profiles, creates folders and a source-grounded course map. It can be rerun without duplicating sources/maps or replacing customized profiles. Originals remain local and ignored by Git. The shared 226/326 syllabus is represented as one workspace course; the code can be tailored later if desired.

The syllabi establish course scope; they are not lecture notes or tutorial problem banks. The setup creates honest course maps, not invented complete lecture notes. Upload lectures/tutorials as they become available.

## Available tools by subject

| Subject | Working computation | Still needed for broader coverage |
|---|---|---|
| Circuits | Resistive DC, voltage/current sources, nodal result, power balance | ngspice, dependent sources, RC/RL/RLC topology simulation, AC |
| Probability | Binomial, normal, Poisson, exponential, uniform, gamma; PMF/PDF/CDF charts | Joint distributions, process simulation, broader symbolic integration |
| Mathematical methods | Bounded symbolic arithmetic/differentiation/polynomial roots; constant-forcing first/second-order ODE curves | General ODEs, Laplace/convolution, phase planes, numerical-method comparisons |
| Digital systems | Up to six-variable truth tables, equivalent minimal SOP, 2-4-variable Gray-code Karnaugh maps | Don't-cares, sequential simulation, HDL tooling and timing diagrams |

Symbolic instructions and scaffolding do not count as verified computations. The standard note recipe asks for definitions, assumptions, reasoning, citations, meaningful diagrams, worked examples, original practice, and common mistakes. Actual educational quality still depends on the connected agent and the provided course materials.
