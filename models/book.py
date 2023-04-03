from pydantic import BaseModel

class Book(BaseModel):
  id: str
  title: str
  author: str


bookList = [
  Book(id="1", title="Harry Potter y el misterio del principe", author="J.k Rowling"),
  Book(id="2", title="Harry Potter y la piedra filosofal", author="J.k Rowling")
]