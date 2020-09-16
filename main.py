class Library:
    def __init__ (self,list,name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBook(self):
        print(f"we have following books in the library:{self.name}")

        for book in self.booklist:
            print(book)


    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("lender-book database has been updated.You can take book now")
        else:
            print(f"Book has already being used by {self.lendDict[book]}")

    def addbook(self,book):
        self.booklist.append(book)
        print("book has been added to the booklist")

    def returnBook(self,book):
        self.booklist.remove(book)

if __name__ == '__main__':
    harry = Library(['python','rich dady poor dady',"harry potter"],"code wth harry")


    while(True):
        print(f"welcome to the {harry.name} library.Enter your choice to continue")
        print("1. Display Books")
        print('2. Lend a book')
        print('3. ad a book')
        print('4. return a book')

        user_choice = int(input())

        if user_choice == 1 :
            harry.displayBook()

        elif user_choice == 2:
            book = input("Enter the book that you want to lend!")
            user = input("Enter your name")
            harry.lendBook(user,book)

        elif user_choice == 3:
            book = input("Enter the book that you want to add:")
            harry.addbook(book)
        elif user_choice == 4:
            book = input("Enter the book that you want to return:")
            harry.returnBook(book)
            
        print("press q to quit and press c to continue")
            
        user_choice2 = ""
        while(user_choice2 !="c" and user_choice2 !="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            if user_choice2 == "c":
                continue
