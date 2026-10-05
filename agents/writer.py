from agents.model import llm
from graph.logging import log_agent


def writer_agent(state):

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

        tool_results = state.get(
            "tool_results",
            []
        )

        prompt = f"""
You are the Writer Agent.

Create the final answer.

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

CRITIC:
{critique}

Instructions:

- Synthesize the strongest information.
- Use valid tool results.
- Address critic feedback.
- Resolve contradictions.
- Do not mention internal agents.
- Do not mention the workflow.
- Produce a clear final answer.

Return only the final answer.
"""

        response = llm.invoke(
            prompt
        )

        output = response.content

        logs = log_agent(
            state,
            "writer",
            "SUCCESS",
            output
        )

        return {
            "final_answer": output,
            "execution_log": logs
        }

    except Exception as error:

        logs = log_agent(
        state,
        "writer",
        "SUCCESS",
        output
    )

    return {
        "final_answer": output,
        "execution_log": logs
    }