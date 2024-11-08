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
                print (f"{book.name}: {book.author} :{book.publication_year} :{book.is_borrowed}") 



        
    
