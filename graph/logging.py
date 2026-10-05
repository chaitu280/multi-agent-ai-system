from memory.store import save_execution


def log_agent(state, agent_name, status, output):
    session_id = state["session_id"]

    save_execution(
        session_id=session_id,
        agent=agent_name,
        status=status,
        output=output
    )

    # IMPORTANT:
    # Return ONLY the new log entry.
    # Do NOT return the existing execution_log.
    return [f"{agent_name}: {status}"]