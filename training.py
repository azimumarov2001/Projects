from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Game(BaseModel):
    author: str
    text: str

games=[]
@app.get('/')
def welcome():
    return {'message': 'Добро пожаловать в наш интернет магазин!'}
@app.post('/add_game')
def add_game(game: Game):
    games.append(game)
    return {'message': 'Игра успешно добавлена!'}
@app.get("/games")
def get_posts():
    return games




