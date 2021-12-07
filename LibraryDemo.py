class Library:
    books = {"python", "java", "c++", "perl", "ruby", "chamapakwan", "jokes", "life of programmer", "Go","Scala"}

    def allbooks(self):
        i = 0
        for book in self.books:
            i = i + 1
            print(f"{i}. {book.capitalize()}")

    def addbook(self):
        x = input("Write Book Name : ")
        self.books.add(x.lower())
        print(f"You added '{x.capitalize()}' book.")

    def lendbook(self):
        y = input("Write Book name that you want to lend : ")
        if y.lower() in self.books:
            self.books.remove(y.lower())
            print(f"You lended '{y.capitalize()}' book.")
        else:
            print(f"'{y}' is not available for lend! sorry for inconvenience!")

    def returnbook(self):
        z = input("Write Book name that you want to return : ")
        self.books.add(z.lower())
        print(f"You returned '{z.capitalize()}' book.")


a = Library()
print("--------Welcome to your Library Dashboard--------")
while True:
    ext = input("1.List of Available Books."
                "\n2.Lend Books."
                "\n3.Return Books."
                "\n4.Add Books."
                "\n5.exit"
                "\nEnter your choice : ")
    if ext == "1":
        a.allbooks()
        print("------Anything Else-------")
    if ext == "2":
        a.lendbook()
        print("------Anything Else-------")
    if ext == "3":
        a.returnbook()
        print("------Anything Else-------")
    if ext == "4":
        a.addbook()
        print("------Anything Else-------")
    if ext == "5":
        break
    if ext != "1" and ext != "2" and ext != "3" and ext != "4" and ext != "5":
        print(f"'{ext}' is not valid option! Choose right option again : ")
