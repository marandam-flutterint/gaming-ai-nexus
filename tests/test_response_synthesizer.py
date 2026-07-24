from app.models.orchestrator_context import OrchestratorContext
from app.agents.agent_factory import AgentFactory

context = OrchestratorContext(
    user_request="Design an Enterprise AI Platform"
)

context.plan = "Implementation Plan..."

context.research = "Research Findings..."

context.architecture = "Architecture Recommendation..."

agent = AgentFactory.get("synthesizer")

agent.execute(context)

print(context.final_response)