# Program that helps manage the books in the library
# Add a book to the library, remove a book from the library, search for a book
# Display all books in the library
# LIBRARY MANAGEMENT SYSTEM
# 1. Add a Book
# 2. Remove a Book
# 3. Search for a Book
# 4. Display All books
# 5. Exit program


class Book:
    def __init__(self, title, author):
        self.title = title.lower()
        self.author = author.lower()

    def __str__(self):
        return f"{self.title.title()} by {self.author.title()}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title.lower(), author.lower())
        self.books.append(book)
        print(f'{title} by {author} added.')

    def remove_book(self, title, author):
        for book in self.books:
            if book.title == title.lower() and book.author == author.lower():
                self.books.remove(book)
            print(f"{title.title()} by {author.title()} removed.")

    def search_book(self, search_key):
        results = []
        for book in self.books:
            if search_key.lower() in book.title or search_key.lower() in book.author:
                results.append(book)
        if results:
            print('\nSearch Results', *results, sep='\n')
            return results
        else:
            print(f"No results found")

    def display_books(self):
        for book in self.books:
            print(book)


def library():
    print("Welcome to JM-A Library")
    library = Library()
    while True:
        try:
            option = int(
                input(
                    (
                        """
 1. Add a book
 2. Remove a book
 3. Search for a book
 4. Display all books
 5. Exit Library            
Enter option(1-5): """
                    )
                )
            )

            if option == 1:
                title = input("\nEnter book's title: ")
                author = input("Enter book's author: ")
                library.add_book(title, author)

            elif option == 2:
                title = input("\nEnter book's title: ")
                author = input("Enter book's author: ")
                library.remove_book(title, author)

            elif option == 3:
                search_key = input('\nEnter search key: ')
                library.search_book(search_key)

            elif option == 4:
                library.display_books()

            elif option == 5:
                print("Goodbye!!")
                break

            else:
                print("Invalid choice. Try again.")
        except ValueError as e:
            print("Invalid entry. Try again.")


if __name__ == '__main__':
    library()