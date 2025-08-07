from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
import os, re, sys
from db.database import SessionLocal
from models.models import Guest, Room

# ✅ Load environment variables from project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

# ✅ Setup Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# ✅ Add conversation memory
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(llm=llm, memory=memory)

# ✅ Name extractor
def extract_name_and_role(text: str) -> tuple[str | None, str | None]:
    name_match = re.search(r"(?:i am|i’m|my name is|this is)\s+(\w+)", text, re.IGNORECASE)
    role_match = re.search(r"(?:i am|i’m|this is)\s+\w+\s*,?\s*(an?|the)?\s*(guest|admin|staff|manager)", text, re.IGNORECASE)

    name = name_match.group(1).capitalize() if name_match else None
    role = role_match.group(3).lower() if role_match else None
    return name, role


# ✅ Core assistant function
def get_ai_response(message: str) -> dict:
    guest_name, user_role = extract_name_and_role(message)

    db = SessionLocal()

    if user_role == "admin":
        return {"response": "Welcome Admin. You can manage guests, rooms, and bookings."}

    if user_role == "staff":
        return {"response": "Hello Staff! You can assist guests or update room statuses here."}

    if guest_name:
        guest = db.query(Guest).filter(Guest.name == guest_name).first()
        if guest:
            room = db.query(Room).filter(Room.available == True).first()
            if room:
                return {
                    "response": f"Hello {guest.name}! We recommend the {room.type} room – perfect for {', '.join(guest.preferences.get('likes', []))} lovers."
                }
            else:
                return {"response": f"Hi {guest.name}, sorry – all rooms are currently booked."}
        else:
            return {"response": f"No guest found with name {guest_name}."}

    # If no name or role found, fallback to AI conversation
    ai_response = conversation.predict(input=message)
    return {"response": ai_response}


    if guest_name:
        guest = db.query(Guest).filter(Guest.name == guest_name).first()
        if guest:
            room = db.query(Room).filter(Room.available == True).first()
            if room:
                return {
                    "response": f"We recommend the {room.type} room for {guest.name} – great for {', '.join(guest.preferences.get('likes', []))} lovers."
                }
            else:
                return {"response": "Sorry, no rooms are available right now."}
        else:
            # 🧠 Let Gemini politely respond if guest not found
            context = f"The user says their name is {guest_name}, but we couldn't find them in the database. Be polite and helpful."
            reply = conversation.predict(input=f"{context}\nUser: {message}")
            return {"response": reply}

    # 🧠 Generic fallback with system-level context
    system_prompt = (
        "You are a helpful AI concierge assistant. If the user's preferences are known, personalize your reply. "
        "Otherwise, be friendly and helpful."
    )
    full_prompt = f"{system_prompt}\nUser: {message}"
    reply = conversation.predict(input=full_prompt)
    return {"response": reply}
