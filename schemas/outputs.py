from typing import List, Literal

from pydantic import BaseModel, Field


class SupervisorDecision(BaseModel):

    plan: str = Field(
        description="Execution plan for the task"
    )

    selected_agents: List[
        Literal[
            "researcher",
            "analyst",
            "specialist"
        ]
    ] = Field(
        description="Agents required for the task"
    )


class CriticDecision(BaseModel):

    status: Literal[
        "PASS",
        "REVISE"
    ]

    feedback: str = Field(
        description="Detailed critique of agent outputs"
    )