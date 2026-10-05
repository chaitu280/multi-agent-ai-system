from agents.model import llm
from schemas.outputs import SupervisorDecision
from graph.logging import log_agent


structured_llm = llm.with_structured_output(
    SupervisorDecision
)


def supervisor_agent(state):

    query = state["user_query"]

    try:

        prompt = f"""
You are the Supervisor Agent.

Analyze the user's task and determine which agents
are required.

USER REQUEST:
{query}

Available agents:

researcher:
Information gathering.

analyst:
Reasoning, comparison and evaluation.

specialist:
Technical/domain-specific reasoning.

Select only necessary agents.

Return a structured decision.
"""

        result = structured_llm.invoke(
            prompt
        )

        logs = log_agent(
            state,
            "supervisor",
            "SUCCESS",
            result.plan
        )

        return {
            "plan": result.plan,
            "selected_agents": result.selected_agents,
            "execution_log": logs
        }

    except Exception as error:
        logs = log_agent(
        state,
        "supervisor",
        "ERROR",
        str(error)
    )

    return {
        "plan": "Supervisor failed. Use the researcher agent as fallback.",
        "selected_agents": ["researcher"],
        "execution_log": logs,
        "errors": [str(error)]
    }