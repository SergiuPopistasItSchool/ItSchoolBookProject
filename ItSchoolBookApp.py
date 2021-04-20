def add_book():
    book_name = input("Insert a book name ->")
    author_name = input("Insert a author name ->")
    #imporint csv lib
    import csv
    with open('booksDB.csv', mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=[
            "BookName", "AuthorName", "SharedWith", "IsRead"
        ])
        writer.writerow({"BookName": book_name,
                         "AuthorName": author_name,
                         "SharedWith": 'None',
                         "IsRead": False}
                        )
    print("Book was added successfully")


def list_books():
    import csv
    with open('booksDB.csv', mode='r') as file:
        #  pasul 1 sa luam toate datele din DB
        rows = csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead"))
        # parcurgem rand cu rand
        for row in rows:
            print(
                f"Book name is: {row.get('BookName')} Author Name {row.get('AuthorName')} is shared {row.get('ShareWith')} is read  {row.get('IsRead', False)}")


def update_book():
    print("Update a book option")
def share_book():
    print("Share a book option")


# Maine menu for user
print("Menu : ")
print("1 : Add a book")
print("2 : List books")
print("3 : Update book")
print("4 : Share book")
option = int(input("Select one option -> "))

if option == 1:
    add_book()
elif option == 2:
    list_books()
elif option == 3:
    update_book()
elif option == 4:
    share_book()
else:
    print("Not a valid option")