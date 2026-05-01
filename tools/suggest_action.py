from app.agent.llm import call_llm

def suggest_next_action_tool(history):
    prompt = f"Suggest next action: {history}"
    return call_llm(prompt)