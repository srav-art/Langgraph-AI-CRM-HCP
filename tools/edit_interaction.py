from app.core.database import SessionLocal
from app.models.interaction import Interaction

def edit_interaction_tool():
    db = SessionLocal()
    interaction = db.query(Interaction).first()
    if interaction:
        interaction.notes = "Edited via AI"
        db.commit()
    return {"status": "edited"}