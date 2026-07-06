def add_book(catalog, book_id, title, author, year):
    
    catalog[book_id] = (title, author, year)
    print("Added book:", title)

def borrow_book(catalog, borrowed_books, book_id):
    if book_id not in catalog:
        print("Error: Book does not exist.")
    elif book_id in borrowed_books:
        print("Error: Book is already borrowed.")
    else:
        borrowed_books.append(book_id)
        print("Successfully borrowed ID:", book_id)

def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print("Successfully returned ID:", book_id)
    else:
        print("Error: This book wasn't borrowed.")

def register_member(members, member_id):
    
    members.add(member_id)

def show_available(catalog, borrowed_books):
    print("\nAvailable Books")
    for book_id in catalog:
        if book_id not in borrowed_books:
            book_details = catalog[book_id]
            title = book_details[0]
            author = book_details[1]
            print("ID:", book_id, "-", title, "by", author)
    

def main():
    
    catalog = {}
    borrowed_books = []
    members = set()

    
    add_book(catalog, 1001, "The Hobbit", "J.R.R. Tolkien", 1937)
    add_book(catalog, 1002, "1984", "George Orwell", 1949)
    add_book(catalog, 1003, "To Kill a Mockingbird", "Harper Lee", 1960)
    add_book(catalog, 1004, "The Great Gatsby", "F. Scott Fitzgerald", 1925)


    register_member(members, 201)
    register_member(members, 202)
    register_member(members, 201) 
    print("Registered Member IDs:", members)

    
    borrow_book(catalog, borrowed_books, 1002)
    borrow_book(catalog, borrowed_books, 1004)

    
    return_book(borrowed_books, 1002)


    show_available(catalog, borrowed_books)

if __name__ == "__main__":
    main()