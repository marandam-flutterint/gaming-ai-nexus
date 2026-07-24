from app.services.bedrock_client import BedrockClient


class AgentFactory:

    _llm = BedrockClient()

    _instances = {}

    _registry = {
        "planner": PlannerAgent,
        "research": ResearchAgent,
        "architecture": ArchitectureAgent,
    }

    @classmethod
    def get(cls, name):

        if name not in cls._instances:

            cls._instances[name] = cls._registry[name](cls._llm)

        return cls._instances[name]