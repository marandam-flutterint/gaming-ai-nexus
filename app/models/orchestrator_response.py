from dataclasses import dataclass


@dataclass
class OrchestratorResponse:
    user_request: str
    plan: str
    research: str
    architecture: str
