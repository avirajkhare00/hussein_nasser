import tornado.web
import tornado.ioloop
import json


class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello there. This is tornado web server.\n")

class BooksRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("books.html")

class IsEvenNumberRequestHandler(tornado.web.RequestHandler):
    def get(self):
        number = self.get_argument("number")
        if(number.isdigit()):
            r = "odd" if int(number) % 2 else "even"
            self.write(f"The integer {number} is {r}.")
        else:
            self.write(f"{number} is not valid integer")

class StudentCourseInfoRequestHandler(tornado.web.RequestHandler):
    def get(self, student_name, course_id):
        self.write(f"Dear {student_name}, you are viewing course {course_id}.\n")

class BooksNameJsonResponseRequestHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "application/json")

    def get(self):
        books_file = open("books.txt", 'r')
        books_content = books_file.read().splitlines()

        self.write(json.dumps(books_content))

    def post(self):
        book_name = self.get_argument("book_name")
        books_file = open("books.txt", 'a')
        books_file.write(f'{book_name}\n')
        books_file.close()

        self.write(json.dumps({"message": "Book added successfully"}))

class BooksManager(tornado.web.RequestHandler):
    def get(self):
        self.render("books_manager.html")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r'/', BasicRequestHandler),
        (r'/even', IsEvenNumberRequestHandler),
        (r'/books', BooksRequestHandler),
        (r'/books_manager', BooksManager),
        (r'/books_json_response', BooksNameJsonResponseRequestHandler),
        (r'/course/([a-z]+)/([0-9]+)', StudentCourseInfoRequestHandler)
    ])

    port = 8080
    app.listen(port)
    print(f'Application is running on port {port}')
    tornado.ioloop.IOLoop.current().start()