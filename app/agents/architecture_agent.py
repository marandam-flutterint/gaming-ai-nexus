from app.agents.base_agent import BaseAgent
from app.prompts.system_prompts import ARCHITECTURE_SYSTEM_PROMPT


class ArchitectureAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            ARCHITECTURE_SYSTEM_PROMPT
        )