from app.agents.planner_agent import PlannerAgent
from app.agents.research_agent import ResearchAgent


class AgentFactory:

    _instances = {}

    _registry = {
        "planner": PlannerAgent,
        "research": ResearchAgent,
    }

    @classmethod
    def get(cls, agent_name: str):

        if agent_name not in cls._registry:
            raise ValueError(f"Unknown agent: {agent_name}")


        if agent_name not in cls._instances:
            cls._instances[agent_name] = cls._registry[agent_name]()

        return cls._instances[agent_name]