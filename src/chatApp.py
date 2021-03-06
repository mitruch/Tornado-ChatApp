"""Simple real-time chat application

Created with Tornado Web Server 
and WebSockets technology.

Author: Katarzyna Mitrus
"""

import os.path

import tornado.ioloop
import tornado.web
import tornado.websocket

from tornado.options import define
from tornado.options import options


# Defining port to listen on
define("port", default=8080)


class MainHandler(tornado.web.RequestHandler):
    def get(self):  # Overrides parent method
        self.render("index.html")


class ChatWebSocket(tornado.websocket.WebSocketHandler):
    connections = set()  # Shared between the instances

    # Handle open connection
    def open(self):
        self.connections.add(self)

    # Handle incoming messages
    def on_message(self, message):
        for client in self.connections:
            client.write_message(message)

    # Handle close connection
    def on_close(self):
        self.connections.remove(self)


def main():
    # Creating tornado app object
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/chatsocket", ChatWebSocket)
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static")
    )
    app.listen(options.port)  # Setup port
    tornado.ioloop.IOLoop.current().start()  # Start tornado I/O loop


if __name__ == "__main__":
    main()
