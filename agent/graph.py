from langgraph.graph import StateGraph
from typing import TypedDict

from app.tools.log_interaction import log_interaction_tool
from app.tools.edit_interaction import edit_interaction_tool
from app.tools.fetch_insights import fetch_insights_tool
from app.tools.suggest_action import suggest_next_action_tool
from app.tools.recommend_product import recommend_product_tool


class State(TypedDict):
    user_input: str
    intent: str
    response: str


def detect_intent(state):
    text = state["user_input"].lower()

    if "edit" in text:
        return {"intent": "edit"}

    elif "insight" in text:
        return {"intent": "insights"}

    elif "recommend" in text:
        return {"intent": "recommend"}

    return {"intent": "log"}


def route(state):
    return state["intent"]


def log_node(state):
    res = log_interaction_tool(state["user_input"])
    return {"response": str(res)}


def edit_node(state):
    res = edit_interaction_tool()
    return {"response": str(res)}


def insights_node(state):
    res = fetch_insights_tool()
    return {"response": str(res)}


def recommend_node(state):
    res = recommend_product_tool()
    return {"response": str(res)}


graph = StateGraph(State)

graph.add_node("intent", detect_intent)
graph.add_node("router", route)

graph.add_node("log", log_node)
graph.add_node("edit", edit_node)
graph.add_node("insights", insights_node)
graph.add_node("recommend", recommend_node)

graph.set_entry_point("intent")

graph.add_edge("intent", "router")

graph.add_conditional_edges(
    "router",
    route,
    {
        "log": "log",
        "edit": "edit",
        "insights": "insights",
        "recommend": "recommend"
    }
)

app = graph.compile()