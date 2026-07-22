from app.agents.base_agent import BaseAgent
from app.prompts.system_prompts import RESEARCH_SYSTEM_PROMPT


class ResearchAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            RESEARCH_SYSTEM_PROMPT
        )