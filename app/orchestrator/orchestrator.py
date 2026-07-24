from app.agents.agent_factory import AgentFactory
from app.config.logging_config import logger
from app.models.orchestrator_context import OrchestratorContext
from app.models.orchestrator_response import OrchestratorResponse


class MultiAgentOrchestrator:

    def __init__(self):

        logger.info("Initializing Multi-Agent Orchestrator")

    def execute(self, request: str):

        logger.info("Creating orchestration context")

        context = OrchestratorContext(
            user_request=request
        )

        planner = AgentFactory.get("planner")
        researcher = AgentFactory.get("research")
        architect = AgentFactory.get("architecture")

        planner.execute(context)

        researcher.execute(context)

        architect.execute(context)

        logger.info("Workflow completed")

        logger.info(context.execution_log)

        return OrchestratorResponse(
            user_request=context.user_request,
            plan=context.plan,
            research=context.research,
            architecture=context.architecture,
        )

        