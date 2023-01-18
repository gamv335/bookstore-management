"""
Please find below the code for this capstone project. The code makes use of the following skills 
gained from the bootcamp:
1. Object oriented programming
2. Database management
3. sqlite 3
4. Defensive programming
5. Git (Repository accesible at: https://github.com/gamv335/bookstore-management)

"""
# Import required library
import sqlite3

# Create class to manage methods related to book management
class Ebookstore:
    def __init__(self):
        self.conn = sqlite3.connect('ebookstore.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)""")
        self.conn.commit()
    # The function add entried to the database
    def insert_data(self, data):
        try:
            self.cur.executemany("INSERT INTO books VALUES (?,?,?,?)", data)
            self.conn.commit()
            print("Success!")
        except sqlite3.IntegrityError as e:
            print("Error: Please check the id, duplicate values are not accepted.")
    # The function takes id, field, and updated value to modify existing records
    def update_data(self, id, column, new_value):
        self.cur.execute("UPDATE books SET {} = ? WHERE id = ?".format(column), (new_value, id))
        self.conn.commit()
    # Find the id of a bookk and delete the record. Notify the use if the value is not found. 
    def delete_data(self, id):
        self.cur.execute("SELECT * FROM books WHERE id = ?", (id,))
        res = self.cur.fetchone()
        if res is None:
            print("Sorry id not found. No records affected")     
        else:
            self.cur.execute("DELETE FROM books WHERE id = ?", (id,))
            self.conn.commit()
            print("The following record was deleted:\n", self.print_book_details(id))

    # The function select a value given an id
    def search_data(self, id):
        self.cur.execute("SELECT * FROM books WHERE id = ?", (id,))
        return self.cur.fetchone()
       
    # Select all the data from the table books
    def display_data(self):
        self.cur.execute("SELECT * FROM books")
        return self.cur.fetchall()
    # Print details of a book given an id
    def print_book_details(self, id):
        book = self.search_data(id)
        if book:
            print("Book Details:")
            print(f"Title: {book[1]}\nAuthor: {book[2]}\nQuantity: {book[3]}")
        else:
            print("No book found with that id.")
    # Close the database connection
    def __del__(self):
        self.conn.close()

def main():
    # Call the class and store in a variable
    store = Ebookstore()

    # Insert data into the table
    books_load = [(3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
            (3003, "The Lion, the Witch and the Wardrobe", "C. S. Lewis", 25),
            (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
            (3005, "Alice in Wonderland", "Lewis Carroll", 12)]
    store.insert_data(books_load)

    # The variable will store menu choice from the user
    user_choice = ""
    
    # The while loop will display the menu until the user chooses to exit the program
    # The program will return to menu after completing each task.
    while user_choice != "0":
        
        # Ask the user to select an option from the printed menu
        user_choice = str(input("""
=================================
Welcome, please select an option 
from the menu:
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit
=================================
"""))

        
        # Option 3, allow user to input a new entry to the table.  
        if user_choice == "1":
            
            
            # Use defensive programming to request user inputs from all the entry fields
            # Capture book id
            while True:
                try:
                    id = int(input("Enter the id of the book: "))
                    break
                except ValueError:
                    print("Invalid input. Please try again.")
            # Capture book title
            while True:
                try:
                    title = str(input("Enter the title of the book: "))
                    break
                except ValueError:
                    print("Invalid input. Please try again.")
            # Capture book author
            while True:
                try:
                    author = str(input("Enter the author of the book: "))
                    break
                except ValueError:
                    print("Invalid input. Please try again.")
            # Capture book quantity
            while True:
                try:
                    qty = int(input("Enter the quantity of the book: "))
                    break
                except ValueError:
                    print("Invalid input. Please try again.")

            # The variable stores user input for the new book
            new_book = [id, title, author, qty]
            print(new_book)
            # Add data to the database
            store.insert_data([new_book])
        
        # Option 2, gives the user the option to update any fields of a book entry
        elif user_choice == "2":
            
            # Capture book id for update 
            while True:
                try:
                    update_id = int(input("Please enter the id of the book you would like to search: "))
                    # Print the book details
                    store.print_book_details(update_id)
                    # Use up_book to check if the book id was found before exiting the loop.
                    up_book = store.search_data(update_id)
                    if up_book:
                        break
                except ValueError:
                    print("Invalid input. Please try again.")
            
            # Variable to be used as menu input
            update_choice = ""
            # Loop through the sub menu until users type 0
            while update_choice != "0":
                # Display menu and ask user which entry field to update
                update_choice = str(input("""
=================================
Please select the field you would
like to update:
1. Title
2. Author
3. Quantity
0. Return to main menu
=================================
"""))
                # If use choose option 1, ask for new title and update the field 
                if update_choice == "1":
                    while True:
                        try:
                            new_title = str(input("Please enter the new title (Enter -1 to return to the main menu): "))
                            if new_title == "-1":
                                break
                            else: 
                                store.update_data(update_id, "title", new_title)
                                break
                        except ValueError:
                            print("Invalid input. Please try again.")
                # If use choose option 2, ask for new author and update the field
                elif update_choice == "2":
                    while True:
                        try:
                            new_author = str(input("Please enter the new author (Enter -1 to return to the main menu): "))
                            if new_title == "-1":
                                break
                            else: 
                                store.update_data(update_id, "author", new_author)
                                break   
                        except ValueError:
                            print("Invalid input. Please try again.")
                # If use choose option 3, ask for new quantity and update the field
                elif update_choice == "3":
                    while True:
                        try:
                            new_qty = int(input("Please enter the new quantity (Enter -1 to return to the main menu): "))
                            if new_title == "-1":
                                break
                            else: 
                                store.update_data(update_id, "qty", new_qty)
                                break  
                        except ValueError:
                            print("Invalid input. Please try again.")

                # If the user enters 0 return to the main menu      
                elif update_choice == "0":
                    pass

                else:
                    print("Invalid option. Try again.")

        
        # Option 3, ask the user for the id of the book targeted for deletion.  
        elif user_choice == "3":
            # Capture book id for deletion 
            while True:
                try:
                    id_del = int(input("Please enter the id of the book you would like to search: "))
                    break
                except ValueError:
                    print("Invalid input. Please try again.")
            # Delete the entry from the database
            store.delete_data(id_del)

        # Option 4, allows the user to search a book using its id and prints details about the book
        elif user_choice == "4":
            # Capture book id for search 
            while True:
                try:
                    id_search = int(input("Please enter the id of the book you would like to search: "))
                    break
                except ValueError:
                    print("Invalid input. Please try again.")
            # Print the book details
            store.print_book_details(id_search)

        # Option 0, exits the program. 
        elif user_choice == "0":
            # Close db connection
            store.__del__()
            print("Goodbye!!")
            
        # Print a message when user does not input a valid option 
        else:
            print("Invalid option. Try again.")

# Run the program
main()
