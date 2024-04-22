import asyncio
import websockets

# Creating an empty list to store clients
clients = []


# Defining a function to handling incoming messages from clients
async def handle_message(websocket, path):
    global clients
    global fastest_time
    message = await websocket.recv()
    if message == "buzz":
        response_time = asyncio.get_event_loop().time()
        clients.append([websocket, response_time])
        if len(clients) == 1:
            await websocket.send("First Place!")
            fastest_time = response_time
        else:
            t = round(response_time - fastest_time, 2)
            await websocket.send(f"Response Time: {t} Sec(s) Slower.")

# Starting the WebSocket server.
async def start_server():
    async with websockets.serve(handle_message, "localhost", 8765):
        print("WebSocket Server Started")
        await asyncio.Future()

# Running the server.
asyncio.run(start_server())