from websocket_server import WebsocketServer
from datetime import datetime
import time

def new_client(client, server):
    while True:
        server.send_message_to_all(datetime.now().isoformat() + ": new client joined!")
        time.sleep(1)

server = WebsocketServer(5301, host="localhost")
server.set_fn_new_client(new_client)
server.run_forever()
