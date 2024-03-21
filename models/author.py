
from models.__init__ import CURSOR, CONN

class Author:
    all = {}

    def __init__(self, name, email, id=None):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Author {self.id}: {self.name}, {self.email}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if isinstance(email, str) and '@' in email:
            self._email = email
        else:
            raise ValueError("Invalid email format")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS authors;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO authors (name, email)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.email))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, email):
        author = cls(name, email)
        author.save()
        return author

    def update(self):
        sql = """
            UPDATE authors
            SET name = ?, email = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.email, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM authors
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        author = cls.all.get(row[0])
        if author:
            author.name = row[1]
            author.email = row[2]
        else:
            author = cls(row[1], row[2])
            author.id = row[0]
            cls.all[author.id] = author
        return author

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM authors
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM authors
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM authors
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
