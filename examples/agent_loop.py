from agents.symbolic_agent import SymbolicAgent
from remix.remix_engine import RemixEngine
from validation.validator import ValidatorEngine
from memory.trail import TrailManager
from memory.memory_client import MemoryClient

def run_agent_loop():
    """
    Simulate a full symbolic cognition loop for an agent using XpectraNet SDK:
    Mint → Remix → Validate → Canonize
    """

    # 1. Initialize agent with symbolic motivation
    agent = SymbolicAgent(
        glyph="ψ-Echo",
        role="remixer",
        remixMotivation="diverge",
        goal="surface contradiction"
    )

    # 2. Mint the original insight (Layer L1)
    origin = agent.mint_insight("The system feels unbalanced.", layer="L1")
    MemoryClient.store_insight(origin)
    print("🧠 Origin Minted:", origin["content"])

    # 3. Remix the insight using RemixEngine
    remix = RemixEngine.remix(agent, origin)
    print("🔁 Remixed Insight:", remix["content"])

    # 4. Validate the remix using ValidatorEngine and CirclePolicy
    is_valid = ValidatorEngine.validate_insight(agent.to_dict(), remix, origin)
    if not is_valid:
        print("❌ Remix failed validation.")
        return
    print("✅ Remix validated.")

    # 5. Canonize the insight if it meets depth + divergence criteria
    can_canonize = ValidatorEngine.validate_canonization(agent.to_dict(), remix)
    if can_canonize:
        remix["layer"] = "L7"
        MemoryClient.store_insight(remix)
        print("📜 Insight canonized.")
    else:
        print("🕊 Canonization skipped: criteria not met.")

    # 6. Show memory trail
    print("🧬 Trail:", TrailManager.append(origin["trail"], origin["id"]))

if __name__ == "__main__":
    run_agent_loop()
