from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()

books = [
    {
    "id": 1,
    "title": "Война и мир",
    "author": "Л.Н. Толстой",
    },
    {
        "id": 2,
        "title": "Преступление и наказание",
        "author": "Ф.М. Достоевский",
    },
    {
        "id": 3,
        "title": "Идиот",
        "author": "Ф.М. Достоевский",
    }

]


@app.get("/books", tags = ['Книги'], summary= 'Получить все книги')
def read_books():
    return books

@app.get("/books/{book_id}", tags = ['Книги'], summary= 'Получить книгу по id')
def get_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=404, detail=f"Книга не найдена")

class NewBook(BaseModel):
    title: str
    author: str

@app.post("/books", tags = ['Книги'], summary= 'Добавить книгу')
def create_book(new_book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author,
    })
    return {"success": True, "message": "Книга добавлена"}

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)