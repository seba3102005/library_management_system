from database import Book,add_book,view_books,app,borrow_book,return_book,delete_book

def show_menu():
    print('1.Add a Book ')
    print('2.View Books')
    print('3.Borrow a Book')
    print('4.Return a Book')
    print('5.Delete a book')
    print('6.Exit ')

show_menu()
choice = input("enter your choice")
while True:
    with app.app_context():
            db_size = Book.query.count()
            available_choices = [str(n) for n in range(db_size+1)]



    if choice =='1':
    
        name = input("enter the book's name")
        author = input("enter the author's name")
        publication_year = input("enter the publication_year")
        book = Book(name=name ,author=author, publication_year=publication_year)
        
        add_book(book)
        

    elif choice =='2':
        view_books()


    elif choice=='3':
        book_id = input("please enter the number of the book tha t you want to borrow")
        while book_id not in available_choices:
                print("invalid book to borrow ,Please enter a valid one")
                book_id = input("please enter the number of the book tha t you want to borrow")
        borrow_book(int(book_id))
    
            

        
        
    elif choice == '4':
        book_id = input ("please enter the number of the book that you want to return")
        while book_id not in available_choices:
            print("invalid book to return ,Please enter a valid one")
            book_id = input("please enter the number of the book tha t you want to return")
        return_book(int(book_id))

    elif choice =='5':
        id = input("enter the number of book that you want to delete")
        delete_book(int(id))

    elif choice =='6':
        print("exitting the program")
        break

    choice = input("enter your choice")


