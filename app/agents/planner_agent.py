from app.agents.base_agent import BaseAgent
from app.models.orchestrator_context import OrchestratorContext
from app.prompts.system_prompts import PLANNER_SYSTEM_PROMPT
from app.config.logging_config import logger


class PlannerAgent(BaseAgent):
    
    def __init__(self, llm: BedrockClient):
        super().__init__(
            PLANNER_SYSTEM_PROMPT,
            llm
        )


    def execute(self, context: OrchestratorContext):
        logger.info("Executing PlannerAgent")
        prompt = f"""
    {PLANNER_SYSTEM_PROMPT}

User Request:

{context.user_request}
"""
        context.plan = self.invoke(prompt)

        context.execution_log.append("PlannerAgent completed")

        return context