def evaluate_result(state):

    final_answer = state.get(
        "final_answer",
        ""
    )

    critique = state.get(
        "critique",
        ""
    )

    errors = state.get(
        "errors",
        []
    )

    revision_count = state.get(
        "revision_count",
        0
    )

    evaluation = {
        "answer_generated": bool(
            final_answer.strip()
        ),

        "critic_passed": (
            "STATUS: PASS"
            in critique
        ),

        "errors": len(errors),

        "revision_count": revision_count,

        "agents_executed": len(
            state.get(
                "execution_log",
                []
            )
        )
    }

    return evaluation