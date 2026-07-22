from app.services.bedrock_client import BedrockClient

client = BedrockClient()

response = client.invoke_model("What is Generative AI?")

print(response)