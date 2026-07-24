from app.agents.base_agent import BaseAgent
from app.models.orchestrator_context import OrchestratorContext
from app.prompts.system_prompts import ARCHITECTURE_SYSTEM_PROMPT
from app.config.logging_config import logger



class ArchitectureAgent(BaseAgent):

    def __init__(self, llm: BedrockClient):
        super().__init__(
            ARCHITECTURE_SYSTEM_PROMPT,
            llm
        )

    def execute(self, context: OrchestratorContext):

    

        prompt = f"""


Implementation Plan:

{context.plan}

Research:

{context.research}

"""
        context.architecture = self.invoke(prompt)

        context.execution_log.append(
            "ArchitectureAgent completed"
        )

        return context