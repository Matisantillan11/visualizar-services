from fastapi import FastAPI, HTTPException
from models import book

app = FastAPI()

@app.get('/books')
async def getAllBooks():
  return { "data": book.bookList }

@app.get('/book/{id}')
async def getOneBook(id: str):
  book = search_user(id)  
  if len(book) > 0:
    return book
  raise HTTPException(status_code=404, detail="User not found")


@app.post('/book', status_code=201)
async def createBook(item: book.Book):
  if len(search_user(item.id)) > 0:
    raise HTTPException(status_code=400, detail="Book already created.")

  book.bookList.append(item)
  return item
  

def search_user(id: str):
  bookFinded = filter(lambda book: book.id == id, book.bookList)
  return list(bookFinded)

  

