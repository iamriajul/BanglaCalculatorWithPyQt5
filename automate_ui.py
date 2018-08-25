import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileModifiedEvent


class EventHandler(FileSystemEventHandler):
    def on_modified(self, event : FileModifiedEvent):
        super().on_modified(event)
        if event.src_path == ".\calculator.ui":
            print("Ui Changed!")
            subprocess.call("pyuic5 calculator.ui -o calculator_ui.py", 0,
                            "C:\\Users\Riajul\AppData\Local\Programs\Python\Python36\Scripts\pyuic5.exe")

if __name__ == "__main__":
    path = "."
    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()