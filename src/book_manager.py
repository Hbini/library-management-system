"""Book Management Module"""

class BookManager:
    """Manages book catalog operations."""
    def __init__(self, database):
        self.db = database
    
    def add_book(self, title, author, isbn):
        query = 'INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)'
        return self.db.execute_insert(query, (title, author, isbn))
    
    def search_books(self, term):
        query = 'SELECT * FROM books WHERE title LIKE ? OR author LIKE ?'
        return self.db.execute_query(query, (f'%{term}%', f'%{term}%'))
    
    def get_all_books(self):
        query = 'SELECT * FROM books'
        return self.db.execute_query(query)


class BorrowingSystem:
    """Manages book borrowing operations."""
    def __init__(self, database):
        self.db = database
    
    def borrow_book(self, user_id, book_id):
        query = 'INSERT INTO borrowings (user_id, book_id) VALUES (?, ?)'
        return self.db.execute_insert(query, (user_id, book_id))
    
    def return_book(self, user_id, book_id):
        query = 'UPDATE borrowings SET return_date = CURRENT_TIMESTAMP WHERE user_id = ? AND book_id = ?'
        return self.db.execute_update(query, (user_id, book_id))
    
    def get_borrowed_books(self, user_id):
        query = 'SELECT * FROM borrowings WHERE user_id = ? AND return_date IS NULL'
        return self.db.execute_query(query, (user_id,))


class ReservationSystem:
    """Manages book reservations."""
    def __init__(self, database):
        self.db = database


class FineCalculator:
    """Calculates library fines for overdue books."""
    def __init__(self, database):
        self.db = database
    
    def calculate_fine(self, days_overdue, daily_rate=0.5):
        return days_overdue * daily_rate
