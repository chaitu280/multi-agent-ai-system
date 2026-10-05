from agents.model import llm
from tools.calculator import calculator
from graph.logging import log_agent


analyst_llm = llm.bind_tools(
    [calculator]
)


def analyst_agent(state):

    try:

        query = state["user_query"]
        plan = state["plan"]

        research = state.get(
            "research",
            ""
        )

        prompt = f"""
You are the Analyst Agent.

USER REQUEST:
{query}

PLAN:
{plan}

RESEARCH:
{research}

Analyze the problem.

You may use the calculator tool when
mathematical calculations are required.

Focus on:

- Reasoning
- Comparisons
- Trade-offs
- Quantitative analysis
- Conclusions

Return analytical findings.
"""

        response = analyst_llm.invoke(prompt)

        tool_results = state.get(
            "tool_results",
            []
        )

        if response.tool_calls:

            for tool_call in response.tool_calls:

                if tool_call["name"] == "calculator":

                    result = calculator.invoke(
                        tool_call["args"]
                    )

                    tool_results.append(
                        result
                    )

        output = response.content

        logs = log_agent(
            state,
            "analyst",
            "SUCCESS",
            output
        )

        return {
            "analysis": output,
            "tool_results": tool_results,
            "execution_log": logs
        }

    except Exception as error:

        logs = log_agent(
        state,
        "analyst",
        "SUCCESS",
        output
    )

    return {
        "analysis": output,
        "tool_results": tool_results,
        "execution_log": logs
    }