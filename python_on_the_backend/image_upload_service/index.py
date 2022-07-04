import tornado.web
import tornado.ioloop
import json


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class FileUploadHandler(tornado.web.RequestHandler):
    def post(self):
        files = self.request.files["img_file"]

        for file in files:
            f = open(f'img/{file.filename}', 'wb')
            f.write(file.body)
            f.close()
        
        self.write(json.dumps({"message": "files uploaded"}))

if __name__ == "__main__":
    app = tornado.web.Application([
        ('/', IndexHandler),
        ('/file_upload', FileUploadHandler),
        ('/img/(.*)', tornado.web.StaticFileHandler, {"path" : "img"})
    ])

    port = 8080
    app.listen(port)
    print(f'Listening to port {port}\n')

    tornado.ioloop.IOLoop.instance().start()