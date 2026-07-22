from dataclasses import dataclass


@dataclass
class OrchestratorResponse:

    plan: str

    research: str

    architecture: str

    return OrchestratorResponse(
    plan=plan,
    research=research,
    architecture=architecture
)