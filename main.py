from database import Book,add_book,view_books,app

def show_menu():
    print('Add a Book ')
    print('View Books')
    print('Borrow a Book')
    print('Return a Book')

show_menu()
choice = input("enter your choice")
while True:
    if choice =='1':
    
        name = input("enter the book's name")
        author = input("enter the author's name")
        publication_year = input("enter the publication_year")
        book = Book(name=name ,author=author, publication_year=publication_year)
        
        add_book(book)
        

    elif choice =='2':
        view_books()


    elif choice=='3':
        pass

    choice = input("enter your choice")


