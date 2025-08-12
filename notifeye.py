#!/usr/bin/env python3
import argparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import re
import os

class WatchHandler(FileSystemEventHandler):
    def __init__(self, filter_text):
        self.filter_text = filter_text

    def on_modified(self, event):
        if not event.is_directory:
            try:
                with open(event.src_path, 'r', errors='ignore') as f:
                    content = f.read()
                    if self.filter_text:
                        if re.search(self.filter_text, content, re.IGNORECASE):
                            self.notify(event.src_path)
                    else:
                        self.notify(event.src_path)
            except:
                pass

    def notify(self, filepath):
        filename = os.path.basename(filepath)
        subprocess.run(['notify-send', 'File Changed', f'{filename} was modified'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Notifeye - Linux file watcher with desktop notifications")
    parser.add_argument('--watch', nargs='+', help="Files or folders to watch", required=True)
    parser.add_argument('--filter', help="Only notify if this text appears")
    args = parser.parse_args()

    event_handler = WatchHandler(args.filter)
    observer = Observer()

    for path in args.watch:
        observer.schedule(event_handler, path, recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
