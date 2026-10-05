from agents.model import llm
from tools.search import search_information
from graph.logging import log_agent


research_llm = llm.bind_tools(
    [search_information]
)


def researcher_agent(state):

    try:

        query = state["user_query"]
        plan = state["plan"]

        prompt = f"""
You are the Research Agent.

USER REQUEST:
{query}

SUPERVISOR PLAN:
{plan}

Research the information required for the task.

You may use the search_information tool when useful.

Return clear research findings.
"""

        response = research_llm.invoke(prompt)

        tool_results = state.get(
            "tool_results",
            []
        )

        if response.tool_calls:

            for tool_call in response.tool_calls:

                if tool_call["name"] == "search_information":

                    result = search_information.invoke(
                        tool_call["args"]
                    )

                    tool_results.append(
                        result
                    )

        output = response.content

        logs = log_agent(
            state,
            "researcher",
            "SUCCESS",
            output
        )

        return {
            "research": output,
            "tool_results": tool_results,
            "execution_log": logs
        }

    except Exception as error:

        logs = log_agent(
            state,
            "researcher",
            "ERROR",
            str(error)
        )

        return {
            "research": "",
            "tool_results": state.get(
                "tool_results",
                []
            ),
            "execution_log": logs,
            "errors": state.get(
                "errors",
                []
            ) + [str(error)]
        }