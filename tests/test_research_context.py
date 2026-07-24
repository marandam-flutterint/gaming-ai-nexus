from app.models.orchestrator_context import OrchestratorContext
from app.agents.research_agent import ResearchAgent

context = OrchestratorContext(
    user_request="Design an Enterprise AI Platform"
)

research_agent = ResearchAgent()

research_agent.execute(context)

print("\nRESEARCH\n")
print(context.research)

print("\nLOG\n")
print(context.execution_log)