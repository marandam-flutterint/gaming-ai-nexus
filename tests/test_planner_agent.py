from app.agents.planner_agent import PlannerAgent


planner = PlannerAgent()

response = planner.invoke(
    """
Build an enterprise fraud detection platform using AWS.
    """
)

print(response)