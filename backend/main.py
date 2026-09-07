from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Therapist API",
    description="Backend API for an AI-powered mental wellness chatbot",
    version="1.0.0"
)

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "AI Therapist API is running 🚀"
    }


@app.get("/chat")
def chat(msg: str):

    message = msg.lower().strip()

    if not message:
        return {
            "reply": "I'm here to listen. Tell me how you're feeling."
        }

    if any(word in message for word in ["sad", "depressed", "unhappy", "cry"]):
        return {
            "reply": "I'm really sorry you're feeling this way. You don't have to handle everything alone. I'm here to listen. ❤️",
            "mood": "sad"
        }

    elif any(word in message for word in ["happy", "great", "excited", "good"]):
        return {
            "reply": "That's wonderful to hear! I'm glad you're having a good moment. 😊",
            "mood": "happy"
        }

    elif any(word in message for word in ["stress", "stressed", "pressure", "overwhelmed"]):
        return {
            "reply": "It sounds like you're dealing with a lot right now. Take a slow breath and give yourself a moment. You don't have to solve everything at once. 💙",
            "mood": "stressed"
        }

    elif any(word in message for word in ["anxious", "anxiety", "worried", "nervous"]):
        return {
            "reply": "It's understandable to feel anxious sometimes. Try taking a few slow breaths and focusing on what you can control right now. 🌱",
            "mood": "anxious"
        }

    elif any(word in message for word in ["tired", "exhausted", "sleepy"]):
        return {
            "reply": "You sound like you may need some rest. Be gentle with yourself and give your mind and body some time to recharge. 😴",
            "mood": "tired"
        }

    else:
        return {
            "reply": "Thank you for sharing that with me. Tell me a little more about what you're experiencing.",
            "mood": "neutral"
        }