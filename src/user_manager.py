"""User Management Module"""

class UserManager:
    """Manages user registration and profile operations."""
    
    def __init__(self, database):
        self.db = database
    
    def register_user(self, username, email, phone):
        """Register a new user."""
        query = 'INSERT INTO users (username, email, phone) VALUES (?, ?, ?)'
        return self.db.execute_insert(query, (username, email, phone))
    
    def get_user(self, user_id):
        """Get user by ID."""
        query = 'SELECT * FROM users WHERE id = ?'
        return self.db.execute_query(query, (user_id,))
    
    def update_user(self, user_id, **kwargs):
        """Update user information."""
        cols = [f'{k} = ?' for k in kwargs.keys()]
        query = f'UPDATE users SET {" ,".join(cols)} WHERE id = ?'
        params = tuple(list(kwargs.values()) + [user_id])
        return self.db.execute_update(query, params)
