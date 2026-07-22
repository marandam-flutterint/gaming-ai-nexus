from app.agents.agent_factory import AgentFactory

agent = AgentFactory.get("planner")

response = agent.invoke(
    "Design a scalable AI platform for a gaming company."
)

print(response)