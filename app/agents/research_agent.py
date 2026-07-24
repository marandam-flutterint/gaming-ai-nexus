from app.agents.base_agent import BaseAgent
from app.models.orchestrator_context import OrchestratorContext
from app.prompts.system_prompts import RESEARCH_SYSTEM_PROMPT
from app.config.logging_config import logger


class ResearchAgent(BaseAgent):

    def __init__(self, llm: BedrockClient):
        super().__init__(
            RESEARCH_SYSTEM_PROMPT,
            llm
        )

    def execute(self, context: OrchestratorContext):


        prompt = f"""

Implementation Plan:

{context.plan}
"""
        context.research = self.invoke(prompt)

        context.execution_log.append(
            "ResearchAgent completed"
        )

        return context