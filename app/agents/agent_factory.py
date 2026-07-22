from app.agents.planner_agent import PlannerAgent


class AgentFactory:

    _instances = {}

    @classmethod
    def get(cls, agent_name: str):

        if agent_name not in cls._instances:

            if agent_name == "planner":
                cls._instances[agent_name] = PlannerAgent()
            else:
                raise ValueError(f"Unknown agent: {agent_name}")

        return cls._instances[agent_name]