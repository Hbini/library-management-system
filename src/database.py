"""Database module for Library Management System

Handles all database operations including user, book, and borrowing records.
"""

from typing import Optional, List, Dict, Any
from datetime import datetime
import sqlite3


class Database:
    """
    Database class for managing library data.
    
    Provides methods for CRUD operations on users, books, and borrowing records.
    """
    
    def __init__(self, db_name: str = 'library.db'):
        """
        Initialize database connection.
        
        Args:
            db_name (str): Name of the SQLite database file
        """
        self.db_name = db_name
        self.connection = None
        self.initialize_db()
    
    def initialize_db(self) -> None:
        """Initialize database tables if they don't exist."""
        self.connection = sqlite3.connect(self.db_name)
        cursor = self.connection.cursor()
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create books table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                isbn TEXT UNIQUE NOT NULL,
                available BOOLEAN DEFAULT TRUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create borrowing table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS borrowings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                borrow_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                due_date TIMESTAMP,
                return_date TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (book_id) REFERENCES books(id)
            )
        ''')
        
        self.connection.commit()
    
    def execute_query(self, query: str, params: tuple = ()) -> List[tuple]:
        """
        Execute a SELECT query.
        
        Args:
            query (str): SQL query string
            params (tuple): Query parameters
            
        Returns:
            List[tuple]: Query results
        """
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    
    def execute_insert(self, query: str, params: tuple = ()) -> int:
        """
        Execute an INSERT query.
        
        Args:
            query (str): SQL query string
            params (tuple): Query parameters
            
        Returns:
            int: ID of inserted row
        """
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor.lastrowid
    
    def execute_update(self, query: str, params: tuple = ()) -> int:
        """
        Execute an UPDATE query.
        
        Args:
            query (str): SQL query string
            params (tuple): Query parameters
            
        Returns:
            int: Number of affected rows
        """
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor.rowcount
    
    def close(self) -> None:
        """Close database connection."""
        if self.connection:
            self.connection.close()
    
    def __del__(self):
        """Cleanup on object deletion."""
        self.close()
