import os.path

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler)
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
