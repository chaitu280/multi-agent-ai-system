def route_agents(state):

    selected = state.get(
        "selected_agents",
        []
    )

    routes = []

    if "researcher" in selected:
        routes.append("researcher")

    if "analyst" in selected:
        routes.append("analyst")

    if "specialist" in selected:
        routes.append("specialist")

    return routes


def route_after_critic(state):

    critique = state.get(
        "critique",
        ""
    )

    revision_count = state.get(
        "revision_count",
        0
    )

    if (
        "STATUS: REVISE" in critique
        and revision_count < 2
    ):
        return "revision"

    return "writer"