from app.services.bedrock_client import BedrockClient

from app.agents.planner_agent import PlannerAgent
from app.agents.research_agent import ResearchAgent
from app.agents.architecture_agent import ArchitectureAgent
from app.agents.response_synthesizer_agent import ResponseSynthesizerAgent


class AgentFactory:

    _llm = BedrockClient()

    _instances = {}

    _registry = {
        "planner": PlannerAgent,
        "research": ResearchAgent,
        "architecture": ArchitectureAgent,
        "synthesizer": ResponseSynthesizerAgent,
}

    @classmethod
    def get(cls, name):

        if name not in cls._instances:

            cls._instances[name] = cls._registry[name](cls._llm)

        return cls._instances[name]