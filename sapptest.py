from helper.openai_api import create_message
from helper.twilio_api import send_message
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from fastapi.responses import PlainTextResponse
from typing import Dict

load_dotenv()

app = FastAPI()


@app.get('/')
async def home():
    return {"Cheking" : "OK", "sapptest version" : "0.1.0"}


@app.post('/twilio/receiveMessage', response_class=PlainTextResponse)
async def receiveMessage(request: Request) -> None:
    
        form_data: Dict[str, str] = await request.form()
        message = form_data.get('Body')
        sender_id = form_data.get('From')

        # Get response from Openai
        result = create_message(message)
        if result['status'] == 1:
            send_message(sender_id, result['response'])
  