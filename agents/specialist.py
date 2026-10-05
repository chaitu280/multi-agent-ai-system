from agents.model import llm
from graph.logging import log_agent


def specialist_agent(state):

    try:

        query = state["user_query"]
        plan = state["plan"]

        prompt = f"""
You are the Specialist Agent.

USER REQUEST:
{query}

SUPERVISOR PLAN:
{plan}

Provide technical and domain-specific reasoning.

Focus on:

- Technical considerations
- Edge cases
- Risks
- Practical implementation
- Domain-specific insights

Return specialist findings.
"""

        response = llm.invoke(prompt)

        output = response.content

        logs = log_agent(
            state,
            "specialist",
            "SUCCESS",
            output
        )

        return {
            "specialist_findings": output,
            "execution_log": logs
        }

    except Exception as error:

        logs = log_agent(
        state,
        "specialist",
        "SUCCESS",
        output
    )

    return {
        "specialist_findings": output,
        "execution_log": logs
    }