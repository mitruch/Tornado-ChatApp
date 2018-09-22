import os.path

import tornado.ioloop
import tornado.web
import tornado.websocket


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/chatsocket", ChatWebSocket)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static")
        )
        super(Application, self).__init__(handlers, **settings)


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


def main():
    app = Application()  # Creating tornado app object
    app.listen(8080)  # Setup port
    tornado.ioloop.IOLoop.current().start()  # Start tornado I/O loop


if __name__ == "__main__":
    main()

