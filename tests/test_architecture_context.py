from app.models.orchestrator_context import OrchestratorContext
from app.agents.architecture_agent import ArchitectureAgent

context = OrchestratorContext(
    user_request="Design an Enterprise AI Platform"
)

architecture_agent = ArchitectureAgent()

architecture_agent.execute(context)

print("\nARCHITECTURE\n")
print(context.architecture)

print("\nLOG\n")
print(context.execution_log)