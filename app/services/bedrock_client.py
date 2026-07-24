from app.services.bedrock_client import BedrockClient


class BaseAgent:

    def __init__(
        self,
        system_prompt: str,
        llm: BedrockClient
    ):

        self.system_prompt = system_prompt
        self.llm = llm