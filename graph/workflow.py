from langgraph.graph import (
    StateGraph,
    START,
    END
)

from graph.state import AgentState
from graph.routing import (
    route_agents,
    route_after_critic
)

from agents.supervisor import supervisor_agent
from agents.researcher import researcher_agent
from agents.analyst import analyst_agent
from agents.specialist import specialist_agent
from agents.critic import critic_agent
from agents.revision import revision_agent
from agents.writer import writer_agent


def build_workflow():

    workflow = StateGraph(
        AgentState
    )

    # --------------------
    # Nodes
    # --------------------

    workflow.add_node(
        "supervisor",
        supervisor_agent
    )

    workflow.add_node(
        "researcher",
        researcher_agent
    )

    workflow.add_node(
        "analyst",
        analyst_agent
    )

    workflow.add_node(
        "specialist",
        specialist_agent
    )

    workflow.add_node(
        "critic",
        critic_agent
    )

    workflow.add_node(
        "revision",
        revision_agent
    )

    workflow.add_node(
        "writer",
        writer_agent
    )

    # --------------------
    # Start
    # --------------------

    workflow.add_edge(
        START,
        "supervisor"
    )

    # --------------------
    # Dynamic routing
    # --------------------

    workflow.add_conditional_edges(
        "supervisor",
        route_agents,
        {
            "researcher": "researcher",
            "analyst": "analyst",
            "specialist": "specialist"
        }
    )

    # --------------------
    # Agent outputs
    # --------------------

    workflow.add_edge(
        "researcher",
        "critic"
    )

    workflow.add_edge(
        "analyst",
        "critic"
    )

    workflow.add_edge(
        "specialist",
        "critic"
    )

    # --------------------
    # Critic routing
    # --------------------

    workflow.add_conditional_edges(
        "critic",
        route_after_critic,
        {
            "revision": "revision",
            "writer": "writer"
        }
    )

    # --------------------
    # Revision
    # --------------------

    workflow.add_edge(
        "revision",
        "critic"
    )

    # --------------------
    # Final
    # --------------------

    workflow.add_edge(
        "writer",
        END
    )

    return workflow.compile()