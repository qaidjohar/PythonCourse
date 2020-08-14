# from xyz import Animal

class Book():
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return (f"{self.title} is written by {self.author} of {self.pages}")
        # return Animal.whoAmI(self)
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print(f"{self.title} is destroyed")
    
# a = Animal()

book = Book('Complete Python','Qaidjohar','510')
# print(dir(book))
print(book)

del book
# print(len(book))