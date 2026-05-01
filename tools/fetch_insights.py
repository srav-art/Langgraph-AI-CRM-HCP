from app.core.database import SessionLocal
from app.models.interaction import Interaction

def fetch_insights_tool():
    db = SessionLocal()
    interactions = db.query(Interaction).all()
    return [{"notes": i.notes, "sentiment": i.sentiment} for i in interactions]