from langchain_core.tools import tool


@tool
def search_information(query: str) -> str:
    """
    Placeholder search tool.

    In the next version this can be connected
    to a real search API.
    """

    return (
        f"Search tool received query: {query}\n"
        "External search integration will be connected "
        "in the production version."
    )