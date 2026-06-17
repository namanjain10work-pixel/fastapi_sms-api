from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

sms = FastAPI()

messages =[
    {
        "id" : 1,
        "From" : "9824030554" ,
        "To" : "9104199768" ,
        "Body" : "hellow naman"
    },
    {
        "id": 2,
        "from_number": "1234567890",
        "to_number": "9104199768",
        "body": "hello mama "
    }      
]

class Message(BaseModel):
    From: str
    To: str
    Body: str




@sms.get("/")
def index ():
    return {"data":"sms api working properly"}

@sms.get("/messages/{id}")
def get_messages(id:int):
    for msg in messages:
        if msg["id"] == id:
            return msg

    return {"error": "Message not found"}

@sms.post("/messages")
def create_message(message: Message):

    new_message = {
        "id": len(messages) + 1,
        "From": message.From,
        "To": message.To,
        "Body": message.Body
    }

    messages.append(new_message)

    return {
        "message": "SMS created successfully",
        "data": new_message
    }

@sms.delete("/messages/{id}")
def delete_message(id: int):

    for index, msg in enumerate(messages):
        if msg["id"] == id:
            deleted_message = messages.pop(index)

            return {
                "message": "SMS deleted successfully",
                "data": deleted_message
            }

    return {"error": "Message not found"}


@sms.put("/messages/{id}")
def update_message(id: int, message: Message):

    for msg in messages:

        if msg["id"] == id:

            msg["From"] = message.From
            msg["To"] = message.To
            msg["Body"] = message.Body

            return {
                "message": "Message updated successfully",
                "data": msg
            }

    return {"error": "Message not found"}


class UpdateMessage(BaseModel):
    From: Optional[str] = None
    To: Optional[str] = None
    Body: Optional[str] = None

@sms.patch("/messages/{id}")
def patch_message(id: int, update: UpdateMessage):

    for msg in messages:

        if msg["id"] == id:

            if update.From is not None:
                msg["From"] = update.From

            if update.To is not None:
                msg["To"] = update.To

            if update.Body is not None:
                msg["Body"] = update.Body

            return {
                "message": "Message updated successfully",
                "data": msg
            }

    return {"error": "Message not found"}