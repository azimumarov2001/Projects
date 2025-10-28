from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

DATABASE_URL = 'sqlite:///database.db'
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
app = FastAPI()


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True)
    genres = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)


class CreateMovie(BaseModel):
    title: str
    genres: str
    rating: int


class UpdateMovie(BaseModel):
    title: str | None = None
    genres: str | None = None
    rating: int | None = None


Base.metadata.create_all(bind=engine)


@app.post('/movies')
def create_movie(movie: CreateMovie):
    db = SessionLocal()
    try:
        if db.query(Movie).filter(Movie.title == movie.title).first():
            raise HTTPException(status_code=400, detail='Movie already exists')
        new_movie = Movie(title=movie.title, genres=movie.genres, rating=movie.rating)
        db.add(new_movie)
        db.commit()
        db.refresh(new_movie)
        return new_movie
    finally:
        db.close()


@app.get('/movies')
def read_movies():
    db = SessionLocal()
    get_movies = db.query(Movie).all()
    db.close()
    return get_movies


@app.get('/movies/{movie_id}')
def read_movie1(movie_id: int):
    db = SessionLocal()
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    db.close()
    if not movie:
        db.close()
        raise HTTPException(status_code=404, detail='Movie not found')
    return movie


@app.delete('/movies/{movie_id}')
def delete_movie(movie_id: int):
    db = SessionLocal()
    try:
        deleted_movie = db.query(Movie).filter(Movie.id == movie_id).first()
        if not deleted_movie:
            raise HTTPException(status_code=404, detail='Movie not found')
        db.delete(deleted_movie)
        db.commit()
        return {'message': 'Movie deleted'}
    finally:
        db.close()
