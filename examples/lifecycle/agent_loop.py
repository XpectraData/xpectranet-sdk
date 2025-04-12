from agents.base import Agent
from rituals.remix_engine import RemixEngine
from memory.trail import InsightTrail
from circles.governance import CirclePolicy

agent = Agent.from_yaml("examples/agents/psi_echo.yaml")
trail = InsightTrail()
policy = CirclePolicy.load("data/circles/circle.ethics.yaml")

origin = trail.mint(agent, content="The system is unstable", layer="L1")
print("Origin:", origin)

remix = RemixEngine.remix(agent, origin)
print("Remix:", remix)

if policy.validate(remix, origin, agent):
    validated = trail.validate(remix, agent)
    print("Validated:", validated)

    if policy.canonize(validated, agent, remix_depth=3, divergence_score=remix['divergence_score']):
        final = trail.canonize(validated, agent)
        print("Canonized:", final)
