from app.models.orchestrator_context import OrchestratorContext
from app.agents.planner_agent import PlannerAgent

context = OrchestratorContext(
    user_request="Design an Enterprise AI Platform"
)

planner = PlannerAgent()

planner.execute(context)

print("\nPLAN\n")
print(context.plan)

print("\nLOG\n")
print(context.execution_log)