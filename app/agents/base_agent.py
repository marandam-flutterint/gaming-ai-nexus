from app.services.bedrock_client import BedrockClient


class BaseAgent:

    def __init__(self, system_prompt: str):

        self.system_prompt = system_prompt

        self.llm = BedrockClient()

    def invoke(self, user_prompt: str):

        prompt = f"""
{self.system_prompt}

User Request:

{user_prompt}
"""

        return self.llm.invoke_model(prompt)