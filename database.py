from flask import Flask

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)


        
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique=True)
    author = db.Column(db.String(100))
    publication_year = db.Column(db.Integer)
    is_borrowed = db.Column(db.Boolean ,default=False )

    def __init__(self,name,author,publication_year):
        self.name = name
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = False
        print('the object is created succussfully')

    def __repr__(self):
        return f"<Book(name={self.name})>"
    

#lazem tt7at t7t el class
with app.app_context():
    db.create_all()

    
def add_book(book1):
        with app.app_context():
            db.session.add(book1)
            db.session.commit()

def view_books():
        with app.app_context():
            books = Book.query.all()
            
            for book in books:
                print (f"<{book.id}> : {book.name}: {book.author} :{book.publication_year} :{book.is_borrowed}") 

def borrow_book(needed_book):
        with app.app_context():
            
            book = Book.query.filter_by(name=needed_book).first()
            if book.is_borrowed == False:
                book.is_borrowed=True
                db.session.commit()
            else:
                print("the book is not available right now")

def return_book(needed_book):
        with app.app_context():
            book = Book.query.filter_by(name=needed_book).first()
            if book.is_borrowed ==True:
                book.is_borrowed=False
                db.session.commit()
            else:
                print("this book is not borrowed")


def delete_book(id):
        with app.app_context():

            book = Book.query.get(id)
            db.session.delete(book)
            db.session.commit()
            for new_id,book in enumerate(Book.query.all(),start=1):
                book.id=new_id

            db.session.add(book)
            db.session.commit()
            

      





        
    
