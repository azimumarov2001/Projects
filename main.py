from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
app = FastAPI()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)


class CreateBook(BaseModel):
    title: str
    author: str
    year: int


Base.metadata.create_all(bind=engine)


@app.post("/books")
def create_book(book: CreateBook):
    db = SessionLocal()
    try:
        if db.query(Book).filter(Book.title == book.title).first():
            raise HTTPException(status_code=400, detail="Book already exists")
        new_book = Book(title=book.title, author=book.author, year=book.year)
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book
    finally:
        db.close()


@app.get("/books")
def read_books():
    db = SessionLocal()
    try:
        books = db.query(Book).all()
        return books
    finally:
        db.close()


@app.get("/books/{book_id}")
def read_book(book_id: int):
    db = SessionLocal()
    try:
        book1 = db.query(Book).filter(Book.id == book_id).first()
        if not book1:
            raise HTTPException(status_code=404, detail="Book not found")
        return book1
    finally:
        db.close()


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    db = SessionLocal()
    try:
        delete_book = db.query(Book).filter(Book.id == book_id).first()
        if not delete_book:
            raise HTTPException(status_code=404, detail="Book not found")
        db.delete(delete_book)
        db.commit()
        return delete_book
    finally:
        db.close()


@app.put("/books/{book_id}")
def update_book(book_id: int, book: CreateBook):
    db = SessionLocal()
    try:
        db_book = db.query(Book).filter(Book.id == book_id).first()
        if not db_book:
            raise HTTPException(status_code=404, detail="Book not found")
        db_book.title = book.title
        db_book.author = book.author
        db_book.year = book.year
        db.commit()
        db.refresh(db_book)
        return db_book
    finally:
        db.close()


@app.patch("/books/{book_id}")
def update_book(book_id: int, book: CreateBook):
    db = SessionLocal()
    try:
        patch_book = db.query(Book).filter(Book.id == book_id).first()
        if not patch_book:
            raise HTTPException(status_code=404, detail="Book not found")
        if patch_book.title is not None:
            patch_book.title = book.title
        if patch_book.author is not None:
            patch_book.author = book.author
        if patch_book.year is not None:
            patch_book.year = book.year
        db.commit()
        db.refresh(patch_book)
        return patch_book
    finally:
        db.close()
