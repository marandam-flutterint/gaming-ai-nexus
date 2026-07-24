from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class AgentResult:
    """
    Standard response returned by every AI agent.
    """

    agent_name: str

    output: Optional[str] = None

    success: bool = True

    error: Optional[str] = None

    metadata: Dict[str, Any] = field(default_factory=dict)