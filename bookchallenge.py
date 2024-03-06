class Book:


    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False


#to check if the book is checked out
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"{self.title} by {self.author} has been checked out.")
        else:
            print("Sorry, this book is already checked out.")

#to mark the book as returned
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"Thank you for returning {self.title} by {self.author}.")
        else:
            print("This book is not checked out.")

myBook = Book("Traitor", "Makena", 883322)

print(myBook.title)
print(myBook.author)
print(myBook.isbn)
print(myBook.return_book())
print(myBook.check_out())



   