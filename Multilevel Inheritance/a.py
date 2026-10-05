class Book:
    def __init__(self):
        self.book_id = input("Enter book id: ")
        self.title = input("Enter title: ")
        self.author = input("Enter author: ")
        self.publication_year = input("Enter publication year: ")

    def display_info(self):
        print(f"Book Id: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}\nPublication year: {self.publication_year}")
class LibraryBook(Book):
    def __init__(self):
        super().__init__()
        self.category = input("Enter category: ")
        self.shelf_number = input("Enter Shelf No. : ")

    def display_info(self):
        super().display_info()
        print(f"Category: {self.category}\nShelf No. : {self.shelf_number}")
class IssuedBook(LibraryBook):
    def __init__(self):
        super().__init__()
        self.browser_name = input("Enter browser name: ")
        self.Issue_date = input("Enter Issued date: ")
        self.return_date = input("Enter return date: ")

    def display_info(self):
        super().display_info()
        print(f"Browser name: {self.browser_name}\nIssue Date: {self.Issue_date}\nReturn date: {self.return_date}")

I = IssuedBook()
I.display_info()