import tornado.web
import tornado.ioloop


class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello there. This is tornado web server.\n")

class BooksRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("books.html")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r'/', BasicRequestHandler),
        (r'/books', BooksRequestHandler)
    ])

    port = 8080
    app.listen(port)
    print(f'Application is running on port {port}')
    tornado.ioloop.IOLoop.current().start()