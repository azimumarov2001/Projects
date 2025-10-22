from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Note(BaseModel):
    id: int
    title: str
    content: str


notes = []


@app.post("/add_note")
def add_note(note: Note):
    for value in notes:
        if value.id == note.id:
            return "Заметка с таким ID уже существует!"
    notes.append(note)
    return {"message": "Заметка успешно добавлена!", "note": note}


@app.get("/notes")
def get_notes():
    return notes


@app.get("/notes/{id}")
def get_note(id: int):
    for value in notes:
        if value.id == id:
            return value
    return {"error": "Заметка не найдена"}


@app.delete("/delete_note/{id}")
def delete_note(id: int):
    for value in notes:
        if value.id == id:
            notes.remove(value)
            return {"message": "Заметка успешно удалена!"}
    return {"error": "Заметка не найдена"}
