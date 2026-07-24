from app.agents.base_agent import BaseAgent
from app.models.orchestrator_context import OrchestratorContext
from app.prompts.system_prompts import SYNTHESIZER_SYSTEM_PROMPT
from app.config.logging_config import logger
from app.services.bedrock_client import BedrockClient


class ResponseSynthesizerAgent(BaseAgent):

    def __init__(self, llm: BedrockClient):
        super().__init__(
            SYNTHESIZER_SYSTEM_PROMPT,
            llm
        )

    def execute(self, context: OrchestratorContext):

        logger.info("Executing ResponseSynthesizerAgent")

        prompt = f"""
Original User Request

{context.user_request}

-------------------------------------

Implementation Plan

{context.plan}

-------------------------------------

Research

{context.research}

-------------------------------------

Architecture Recommendation

{context.architecture}

-------------------------------------

Create ONE executive-quality recommendation.
"""

        context.final_response = self.invoke(prompt)

        context.execution_log.append(
            "ResponseSynthesizerAgent completed"
        )

        return context