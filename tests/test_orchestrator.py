from app.orchestrator.orchestrator import MultiAgentOrchestrator

orchestrator = MultiAgentOrchestrator()

result = orchestrator.execute(
    "Design an Enterprise AI Platform for a Gaming Company"
)

print("\n===== USER REQUEST =====\n")
print(result.user_request)

print("\n===== PLANNER =====\n")
print(result.plan)

print("\n===== RESEARCH =====\n")
print(result.research)

print("\n===== ARCHITECTURE =====\n")
print(result.architecture)