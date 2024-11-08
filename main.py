from database import Book,add_book,view_books,app,borrow_book

def show_menu():
    print('1.Add a Book ')
    print('2.View Books')
    print('3.Borrow a Book')
    print('4.Return a Book')
    print('5.Exit ')

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
        book = input("please enter the name of the book tha t you want to borrow")
        borrow_book(book)

    elif choice =='5':
        print("exitting the program")
        break

    choice = input("enter your choice")


