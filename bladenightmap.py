import websocket
import json

url = 'wss://skatemunich.de:28083/ws'
def on_message(ws, message):
    data = json.loads(message)
    if 'type' in data and data['type'] == 'ping':
        print("Received ping, sending pong")
        ws.send(json.dumps({"type": "pong"}))
    else:
        print("Received message:", data)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, a, b):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")
    # Optionally, you can send a message to the server
    ws.send(json.dumps([48,9682576899,{},"http://bladenight.app/rpc/getActiveEvent"]))
    ws.send(json.dumps([48,4877298098,{},"http://bladenight.app/rpc/getRealtimeUpdate"]))
    ws.send(json.dumps([32,2324243105,{},"RealtimeData"]))


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
