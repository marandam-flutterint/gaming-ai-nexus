from app.services.bedrock_client import BedrockClient
from app.config.logging_config import logger


class BaseAgent:

    def __init__(self, system_prompt: str):

        self.system_prompt = system_prompt

        self.llm = BedrockClient()

    def invoke(self, user_prompt: str):

        logger.info(f"Executing {self.__class__.__name__}")


        return self.llm.invoke_model(
            user_prompt=user_prompt,
            system_prompt=self.system_prompt

        )