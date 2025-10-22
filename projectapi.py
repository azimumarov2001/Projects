from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Event(BaseModel):
    id: int
    title: str
    description: str
    date: int
    location: str


events = []


@app.post("/add_event")
def add_event(event: Event):
    for value in events:
        if value.id == event.id:
            return {"message": "Событие с таким ID уже существует!"}

    events.append(event)
    return {"message": "Событие успешно добавлено!", "event": event}


@app.get("/events/{id}")
def get_event(id: int):
    for value in events:
        if value.id == id:
            return value
    return {"error": "Событие не найдено"}


@app.get("/events")
def get_events():
    return events


@app.delete("/delete_event/{id}")
def delete_event(id: int):
    for value in events:
        if value.id == id:
            events.remove(value)
            return {"message": "Событие успешно удалено!"}
    return {"error": "Событие не найдено"}
