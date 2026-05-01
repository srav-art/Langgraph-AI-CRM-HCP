import json, datetime
from app.agent.llm import call_llm
from app.core.database import SessionLocal
from app.models.interaction import Interaction

def log_interaction_tool(text):
    prompt = f"""
    Extract JSON:
    fields: interaction_type, notes, sentiment, next_action
    text: {text}
    """

    result = call_llm(prompt)

    try:
        data = json.loads(result)
    except:
        data = {
            "interaction_type": "unknown",
            "notes": text,
            "sentiment": "neutral",
            "next_action": "follow up"
        }

    db = SessionLocal()
    interaction = Interaction(
        hcp_id=1,
        date=datetime.date.today(),
        interaction_type=data["interaction_type"],
        notes=data["notes"],
        sentiment=data["sentiment"],
        next_action=data["next_action"]
    )
    db.add(interaction)
    db.commit()

    return {"status": "logged", "data": data}