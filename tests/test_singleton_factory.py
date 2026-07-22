from app.agents.agent_factory import AgentFactory

planner1 = AgentFactory.get("planner")
planner2 = AgentFactory.get("planner")

print(id(planner1))
print(id(planner2))

print(planner1 is planner2)