from typing import TypedDict, List, Annotated
import operator


class AgentState(TypedDict):
    user_query: str
    session_id: str

    plan: str
    selected_agents: List[str]

    research: str
    analysis: str
    specialist_findings: str

    # These fields can receive updates from parallel agents.
    # operator.add merges the new list with the existing list.
    tool_results: Annotated[List[str], operator.add]
    execution_log: Annotated[List[str], operator.add]
    errors: Annotated[List[str], operator.add]

    critique: str
    final_answer: str

    revision_count: int