from agents.model import llm
from schemas.outputs import CriticDecision
from graph.logging import log_agent


structured_llm = llm.with_structured_output(
    CriticDecision
)


def critic_agent(state):

    try:

        query = state["user_query"]

        research = state.get(
            "research",
            ""
        )

        analysis = state.get(
            "analysis",
            ""
        )

        specialist = state.get(
            "specialist_findings",
            ""
        )

        tool_results = state.get(
            "tool_results",
            []
        )

        prompt = f"""
You are the Critic Agent.

Review the work produced by the other agents.

USER REQUEST:
{query}

RESEARCH:
{research}

ANALYSIS:
{analysis}

SPECIALIST:
{specialist}

TOOL RESULTS:
{tool_results}

Check:

- Logical correctness
- Contradictions
- Missing information
- Unsupported claims
- Tool usage
- Quality of reasoning

Return PASS if the work is good.

Return REVISE if important problems exist.

Return the structured decision.
"""

        result = structured_llm.invoke(
            prompt
        )

        output = (
            f"STATUS: {result.status}\n"
            f"FEEDBACK: {result.feedback}"
        )

        logs = log_agent(
            state,
            "critic",
            "SUCCESS",
            output
        )

        return {
            "critique": output,
            "execution_log": logs
        }

    except Exception as error:

        logs = log_agent(
        state,
        "critic",
        "SUCCESS",
        output
    )

    return {
        "critique": output,
        "execution_log": logs
    }