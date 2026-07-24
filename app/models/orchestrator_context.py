from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from app.agents.agent_result import AgentResult


@dataclass
class OrchestratorContext:
    """
    Shared workflow state for the Multi-Agent Orchestrator.
    """

    user_request: str

    plan: Optional[AgentResult] = None
    research: Optional[AgentResult] = None
    architecture: Optional[AgentResult] = None
    final_response: Optional[AgentResult] = None

    metadata: Dict[str, Any] = field(default_factory=dict)

    execution_log: List[str] = field(default_factory=list)

    errors: List[str] = field(default_factory=list)