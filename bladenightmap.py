import websocket
import json

url = 'wss://skatemunich.de:28083/ws'

def on_message(ws, message):
    data = json.loads(message)
    print("Received message:", data)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, a, b):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")
    ws.send(json.dumps([48,0,{},"http://bladenight.app/rpc/getActiveEvent"]))
    ws.send(json.dumps([48,0,{},"http://bladenight.app/rpc/getRealtimeUpdate"]))
    ws.send(json.dumps([32,0,{},"RealtimeData"]))


if __name__ == "__main__":
    ws = websocket.WebSocketApp(url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
