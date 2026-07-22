from app.agents.base_agent import BaseAgent

from app.prompts.system_prompts import (
    PLANNER_SYSTEM_PROMPT
)


class PlannerAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            PLANNER_SYSTEM_PROMPT
        )