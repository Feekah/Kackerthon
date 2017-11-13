class Library():
    library = ["book1", "book2", "book3"]

    def __init__(self):
        pass

    def displaybooks(self):
        for i in Library.library:
            print(i)

    def borrowbook(self):

        while input:
            bookname = input("what book do you want to borrow?")

            if bookname in Library.library:
                Library.library.remove(bookname)
                print("Borrowed successfully!")
                print("tHE BOOKS REMAINING ARE: ")
                for j in Library.library:
                    print(j)
                break

            else:
                print("Book not available! ")
                z = input("Borrow another book? Type Y or N")
                if z == "Y":
                    continue

                else:
                    exit()
                

case1 = Library()
case1.displaybooks()
case1.borrowbook()