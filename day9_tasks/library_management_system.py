#Library Management System (Constructor & Inheritance)
'''
A library stores information about books and digital books. Create a base
class Book with a constructor to initialize book details. Create a
derived class EBook that adds file size information.

'''
class Book:
    def __init__(self,bookName,authorName,published,price):
        self.bookName = bookName
        self.authorName = authorName
        self.published = published
        self.price = price
        
class EBook(Book):
    
    def __init__(self, bookName, authorName, published, price, file_type, file_size):
        super().__init__(bookName, authorName, published, price)
        self.file_size = file_size
        self.file_type = file_type
        
    def display_details(self):
        print("Book Details \n")
        print("Book Name: ",self.bookName)
        print("Author Name: ",self.authorName)
        print("Published: ",self.published)
        print("Price: ",self.price)
        print("---------------------------------------------------\n")
        print("EBook Available and its details are: ")
        print("File Size: ",self.file_size)
        print("File Type: ",self.file_type)
        
#defining object
book = EBook("Dear Debbie","Freida McFadden",2026,699,"300mb","pdf")

#displaying details
book.display_details()
