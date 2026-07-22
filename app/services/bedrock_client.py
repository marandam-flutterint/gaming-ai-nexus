import boto3

from botocore.exceptions import ClientError

from app.config.settings import settings
from app.config.logging_config import logger


class BedrockClient:

    def __init__(self):

        logger.info("Initializing Amazon Bedrock Runtime Client...")

        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=settings.AWS_REGION
        )

        self.model_id = settings.MODEL_ID

        logger.info(f"Using model: {self.model_id}")

    def invoke_model(self, prompt: str) -> str:

        try:

            logger.info("Invoking Amazon Bedrock model...")

            response = self.client.converse(
                modelId=self.model_id,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "text": prompt
                            }
                        ]
                    }
                ],
                inferenceConfig={
                    "maxTokens": 512,
                    "temperature": 0.5
                }
            )

            answer = response["output"]["message"]["content"][0]["text"]

            logger.info("Response received from Bedrock.")

            return answer

        except ClientError as e:
            logger.exception("Bedrock Client Error")
            raise e

        except Exception as e:
            logger.exception("Unexpected Error")
            raise e