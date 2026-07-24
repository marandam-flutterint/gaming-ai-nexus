from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class OrchestratorContext:
    """
    Shared workflow state for the Multi-Agent Orchestrator.
    """

    user_request: str

    plan: Optional[str] = None
    research: Optional[str] = None
    architecture: Optional[str] = None
    final_response: Optional[str] = None

    metadata: Dict[str, Any] = field(default_factory=dict)

    execution_log: List[str] = field(default_factory=list)

    errors: List[str] = field(default_factory=list)