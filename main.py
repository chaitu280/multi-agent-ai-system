import uuid

from graph.workflow import build_workflow

from memory.store import (
    initialize_memory,
    save_session
)

from evaluation.evaluator import (
    evaluate_result
)


def main():

    initialize_memory()

    print("\n" + "=" * 70)
    print("       MULTI-AGENT AI SYSTEM - V5")
    print("                GPT-6 Luna")
    print("=" * 70)

    query = input(
        "\nEnter your task:\n> "
    )

    if not query.strip():

        print("Please enter a task.")

        return

    session_id = str(
        uuid.uuid4()
    )

    app = build_workflow()

    initial_state = {

        "user_query": query,

        "session_id": session_id,

        "plan": "",

        "selected_agents": [],

        "research": "",

        "analysis": "",

        "specialist_findings": "",

        "tool_results": [],

        "critique": "",

        "final_answer": "",

        "revision_count": 0,

        "execution_log": [],

        "errors": []
    }

    print(
        "\nRunning V5 multi-agent system..."
    )

    result = app.invoke(
        initial_state
    )

    save_session(
        session_id=session_id,
        user_query=query,
        final_answer=result[
            "final_answer"
        ]
    )

    evaluation = evaluate_result(
        result
    )

    print("\n" + "=" * 70)
    print("PLAN")
    print("=" * 70)

    print(
        result["plan"]
    )

    print("\nSELECTED AGENTS:")

    print(
        ", ".join(
            result["selected_agents"]
        )
    )

    print("\n" + "=" * 70)
    print("CRITIC")
    print("=" * 70)

    print(
        result["critique"]
    )

    print("\n" + "=" * 70)
    print("FINAL ANSWER")
    print("=" * 70)

    print(
        result["final_answer"]
    )

    print("\n" + "=" * 70)
    print("EXECUTION REPORT")
    print("=" * 70)

    for key, value in evaluation.items():

        print(
            f"{key}: {value}"
        )

    print("\n" + "=" * 70)
    print("AGENT EXECUTION LOG")
    print("=" * 70)

    for log in result[
        "execution_log"
    ]:

        print(
            f"- {log}"
        )

    print("\n" + "=" * 70)
    print("WORKFLOW COMPLETED")
    print("=" * 70)


if __name__ == "__main__":

    main()