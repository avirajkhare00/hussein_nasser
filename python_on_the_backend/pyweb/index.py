import tornado.web
import tornado.ioloop


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


if __name__ == "__main__":
    app = tornado.web.Application([
        (r'/', BasicRequestHandler),
        (r'/books', BooksRequestHandler),
        (r'/even', IsEvenNumberRequestHandler)
    ])

    port = 8080
    app.listen(port)
    print(f'Application is running on port {port}')
    tornado.ioloop.IOLoop.current().start()