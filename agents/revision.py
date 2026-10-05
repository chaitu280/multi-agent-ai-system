from agents.model import llm
from graph.logging import log_agent


def revision_agent(state):

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

        critique = state.get(
            "critique",
            ""
        )

        prompt = f"""
You are the Revision Agent.

Improve the multi-agent work based on critic feedback.

USER REQUEST:
{query}

RESEARCH:
{research}

ANALYSIS:
{analysis}

SPECIALIST:
{specialist}

CRITIC:
{critique}

Fix the identified issues.

Return improved analytical findings.

Do not write the final answer.
"""

        response = llm.invoke(
            prompt
        )

        output = response.content

        logs = log_agent(
            state,
            "revision",
            "SUCCESS",
            output
        )

        return {
            "analysis": output,
            "revision_count": (
                state.get(
                    "revision_count",
                    0
                ) + 1
            ),
            "execution_log": logs
        }

    except Exception as error:

        logs = log_agent(
        state,
        "revision",
        "SUCCESS",
        output
    )

    return {
        "analysis": output,
        "revision_count": state.get("revision_count", 0) + 1,
        "execution_log": logs
    }