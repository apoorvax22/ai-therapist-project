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

@app.get("/")
def home():
    return {"message": "Backend is running 🚀"}

@app.get("/chat")
def chat(msg: str):
    msg = msg.lower()

    if "sad" in msg:
        return {"reply": "I'm really sorry you're feeling sad. I'm here for you ❤️"}
    
    elif "happy" in msg:
        return {"reply": "That's amazing! Keep smiling 😊"}
    
    elif "stress" in msg:
        return {"reply": "Take a deep breath. You’ve got this 💪"}
    
    else:
        return {"reply": "Tell me more about how you're feeling."}