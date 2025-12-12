"""Library Management System Package

An open-source Python-based library management system demonstrating
best practices in software development, testing, and documentation.
"""

__version__ = '1.0.0'
__author__ = 'Hbini'
__email__ = 'contact@example.com'
__license__ = 'MIT'

from .user_manager import UserManager
from .book_manager import BookManager
from .borrowing_system import BorrowingSystem
from .reservation_system import ReservationSystem
from .fine_calculator import FineCalculator
from .database import Database

__all__ = [
    'UserManager',
    'BookManager',
    'BorrowingSystem',
    'ReservationSystem',
    'FineCalculator',
    'Database',
]
