from dataclasses import dataclass


@dataclass
class AgentResponse:

    answer: str

    model: str

    agent: str

    latency: float