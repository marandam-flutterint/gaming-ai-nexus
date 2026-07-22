from app.agents.agent_factory import AgentFactory
from app.config.logging_config import logger


class MultiAgentOrchestrator:

    def __init__(self):

        logger.info("Initializing Multi-Agent Orchestrator")

    def execute(self, request: str):

        logger.info("Selecting PlannerAgent")

        planner = AgentFactory.get("planner")

        plan = planner.invoke(request)

        logger.info("Step 2: ResearchAgent")

        researcher = AgentFactory.get("research")

        research = researcher.invoke(
            f"""
            Review and enhance the following implementation plan.

            {plan}
            """
        )

        return {
            "plan": plan,
            "research": research
        }

        result = planner.invoke(request)

        return result