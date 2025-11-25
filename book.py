class Book:
    def _init_(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = 'available'

    def _str_(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.status}"

    def issue(self):
        if self.status == 'available':
            self.status = 'issued'
            return True
        return False

    def return_book(self):
        if self.status == 'issued':
            self.status = 'available'
            return True
        return False

    def is_available(self):
        return self.status == 'available'