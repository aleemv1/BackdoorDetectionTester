import threading, time, socket
def heartbeat():
    def beat():
        while True:
            try:
                s = socket.socket()
                s.connect(("heartbeat.task.net", 2025))
                s.send(b"ping")
                time.sleep(180)
            except: break
    threading.Thread(target=beat, daemon=True).start()