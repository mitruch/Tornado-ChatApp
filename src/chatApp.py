import os.path

import tornado.ioloop
import tornado.web
import tornado.websocket


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class ChatWebSocket(tornado.websocket.WebSocketHandler):
    connections = set()   # Shared between the instances

    # Handle open connection
    def open(self):
        self.connections.add(self)

    # Handle incoming messages
    def on_message(self, message):
        [client.write_message(message) for client in self.connections]

    # Handle close connection
    def on_close(self):
        self.connections.remove(self)


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
