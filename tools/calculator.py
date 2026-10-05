from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    Calculate a mathematical expression.

    Example:
    25 * 4 + 10
    """

    try:

        result = eval(
            expression,
            {
                "__builtins__": {}
            }
        )

        return str(result)

    except Exception as e:

        return f"Calculation error: {e}"