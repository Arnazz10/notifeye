# Notifeye

A lightweight Linux file & folder watcher with desktop notifications.  
Perfect for monitoring logs, builds, or any file changes — directly from the terminal.

## Features
- Watch multiple files/folders
- Optional keyword filter
- Desktop notifications via `notify-send`
- Lightweight & easy to use

## Install
```bash
sudo apt install python3-pip python3-venv libnotify-bin
python3 -m venv venv
source venv/bin/activate
pip install watchdog
