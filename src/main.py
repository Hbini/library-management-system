#!/usr/bin/env python3
"""Main entry point for the Library Management System"""

from src.user_manager import UserManager
from src.book_manager import BookManager
from src.borrowing_system import BorrowingSystem
from src.database import Database


def main():
    """
    Main function to run the Library Management System.
    
    This function initializes the system components and provides
    a simple interface for interacting with the library.
    """
    print("="*50)
    print("Welcome to Library Management System")
    print("="*50)
    print()
    
    # Initialize components
    db = Database()
    user_manager = UserManager(db)
    book_manager = BookManager(db)
    borrowing_system = BorrowingSystem(db)
    
    # Main menu
    while True:
        print("\nMain Menu:")
        print("1. User Management")
        print("2. Book Management")
        print("3. Borrowing Operations")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == '1':
            user_menu(user_manager)
        elif choice == '2':
            book_menu(book_manager)
        elif choice == '3':
            borrowing_menu(borrowing_system)
        elif choice == '4':
            print("\nThank you for using Library Management System!")
            break
        else:
            print("Invalid option. Please try again.")


def user_menu(user_manager: 'UserManager') -> None:
    """Handle user management operations"""
    print("\n--- User Management ---")
    print("1. Register New User")
    print("2. View User Profile")
    print("3. Update User Information")
    print("4. Back to Main Menu")
    
    choice = input("\nSelect an option (1-4): ").strip()
    
    if choice == '1':
        name = input("Enter username: ").strip()
        email = input("Enter email: ").strip()
        phone = input("Enter phone number: ").strip()
        user_manager.register_user(name, email, phone)
        print(f"User '{name}' registered successfully!")
    elif choice == '2':
        user_id = input("Enter user ID: ").strip()
        user = user_manager.get_user(user_id)
        if user:
            print(f"User found: {user}")
        else:
            print("User not found.")
    elif choice == '3':
        user_id = input("Enter user ID: ").strip()
        new_email = input("Enter new email: ").strip()
        user_manager.update_user(user_id, email=new_email)
        print("User information updated!")


def book_menu(book_manager: 'BookManager') -> None:
    """Handle book management operations"""
    print("\n--- Book Management ---")
    print("1. Add New Book")
    print("2. Search Books")
    print("3. View All Books")
    print("4. Back to Main Menu")
    
    choice = input("\nSelect an option (1-4): ").strip()
    
    if choice == '1':
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        isbn = input("Enter ISBN: ").strip()
        book_manager.add_book(title, author, isbn)
        print(f"Book '{title}' added successfully!")
    elif choice == '2':
        search_term = input("Enter search term: ").strip()
        books = book_manager.search_books(search_term)
        for book in books:
            print(book)
    elif choice == '3':
        books = book_manager.get_all_books()
        print(f"\nTotal books: {len(books)}")
        for book in books:
            print(book)


def borrowing_menu(borrowing_system: 'BorrowingSystem') -> None:
    """Handle borrowing operations"""
    print("\n--- Borrowing Operations ---")
    print("1. Borrow a Book")
    print("2. Return a Book")
    print("3. View Borrowed Books")
    print("4. Back to Main Menu")
    
    choice = input("\nSelect an option (1-4): ").strip()
    
    if choice == '1':
        user_id = input("Enter user ID: ").strip()
        book_id = input("Enter book ID: ").strip()
        borrowing_system.borrow_book(user_id, book_id)
        print("Book borrowed successfully!")
    elif choice == '2':
        user_id = input("Enter user ID: ").strip()
        book_id = input("Enter book ID: ").strip()
        borrowing_system.return_book(user_id, book_id)
        print("Book returned successfully!")
    elif choice == '3':
        user_id = input("Enter user ID: ").strip()
        borrowed_books = borrowing_system.get_borrowed_books(user_id)
        print(f"\nBorrowed books for user {user_id}:")
        for book in borrowed_books:
            print(book)


if __name__ == '__main__':
    main()
