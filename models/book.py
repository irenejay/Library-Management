from models.__init__ import CURSOR, CONN,create_tables

class Book:
    all = {}

    def __init__(self, title, author_id, id=None):
        self.id = id
        self.title = title
        self.author_id = author_id

    def __repr__(self):
        return f"<Book {self.id}: {self.title}, Author ID: {self.author_id}>"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")

    @classmethod
    def create(cls, title, author_id):
        book = cls(title, author_id)
        book.save()
        return book

    def save(self):
        sql = """
            INSERT INTO books (title, author_id)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.title, self.author_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE books
            SET title = ?, author_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.author_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM books
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        book = cls.all.get(row[0])
        if book:
            book.title = row[1]
            book.author_id = row[2]
        else:
            book = cls(row[1], row[2])
            book.id = row[0]
            cls.all[book.id] = book
        return book

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM books
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM books
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
