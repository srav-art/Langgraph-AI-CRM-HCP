from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.agent.graph import app as agent
from app.core.database import Base, engine
import re
from datetime import datetime
# 👇 IMPORTANT (loads tables)
from app.models import hcp, interaction
from pydantic import BaseModel

class ChatRequest(BaseModel):
    input_text: str
app = FastAPI()

# CORS (for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👇 This creates tables automatically
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "AI CRM Running"}



# 👉 medicine list (expand anytime)
MEDICINES = [
    "insulin", "paracetamol", "aspirin",
    "metformin", "amoxicillin", "atorvastatin"
]

@app.post("/chat")
def chat(req: ChatRequest):
    text = req.input_text
    lower = text.lower()

    print("🔥 CHAT:", text)

    # -------------------------
    # 🧠 EDIT CASES
    # -------------------------
    if "sentiment was" in lower:
        if "negative" in lower:
            return {"action": "edit", "field": "sentiment", "value": "Negative"}
        elif "positive" in lower:
            return {"action": "edit", "field": "sentiment", "value": "Positive"}
        else:
            return {"action": "edit", "field": "sentiment", "value": "Neutral"}

    if "name is" in lower:
        name = text.split("name is")[1].strip().title()
        return {"action": "edit", "field": "doctor", "value": name}

    # -------------------------
    # 🧠 LOG CASE
    # -------------------------

    # 👉 Extract doctor name
    doctor_match = re.search(r"dr\.?\s+[a-zA-Z]+", text, re.IGNORECASE)
    doctor = doctor_match.group(0).title() if doctor_match else ""

    # 👉 Extract medicines → topics
    found_meds = [med.title() for med in MEDICINES if med in lower]
    topics = ", ".join(found_meds) if found_meds else "General discussion"

    # 👉 Detect sentiment
    if any(word in lower for word in ["good", "great", "positive", "happy"]):
        sentiment = "Positive"
    elif any(word in lower for word in ["bad", "negative", "angry", "poor"]):
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

        # 👉 Detect interaction type
    if any(word in lower for word in ["visit", "met", "meeting"]):
       interaction_type = "Visit"
    elif any(word in lower for word in ["call", "phone", "called"]):
       interaction_type = "Call"
    elif any(word in lower for word in ["zoom", "online", "virtual"]):
       interaction_type = "Meeting"
    else:
        interaction_type = ""

    # 👉 Auto date & time
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M")

    return {
    "action": "log",
    "doctor_name": doctor,
    "interaction_type": interaction_type,
    "topics": topics,
    "sentiment": sentiment,
    "date": current_date,
    "time": current_time,
    "summary": text
}