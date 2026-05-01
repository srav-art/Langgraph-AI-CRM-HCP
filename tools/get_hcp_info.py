def get_hcp_info_tool(state):
    text = state["input"]

    if "dr sharma" in text.lower():
        return {"output": "Dr Sharma is a Cardiologist at Apollo Hospital"}
    
    return {"output": "No HCP info found"}