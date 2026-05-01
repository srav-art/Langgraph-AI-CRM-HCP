def summarize_tool(state):
    text = state["input"]

    summary = f"Summary: {text[:60]}..."

    return {"output": summary}