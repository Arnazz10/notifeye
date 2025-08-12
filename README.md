# Notifeye  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey)  

> **Notifeye** is a lightweight Linux file & folder watcher with desktop notifications — perfect for monitoring logs, builds, or any file changes directly from the terminal.  

---

## ✨ Features  
- 🔍 Watch multiple files or folders  
- 🎯 Optional keyword filter  
- 🖥️ Native desktop notifications (`notify-send`)  
- ⚡ Lightweight & fast setup  

---

## 📸 Demo  
*(Add a GIF or screenshot here — e.g., `notifeye-demo.gif`)*  
```bash
# Example
python notifeye.py ~/projects --keyword error


🚀 Install
bash
Copy
Edit
sudo apt install python3-venv libnotify-bin
python3 -m venv venv
source venv/bin/activate
pip install watchdog
📦 Usage
bash
Copy
Edit
python notifeye.py /path/to/watch [--keyword word]
Example:

bash
Copy
Edit
python notifeye.py /var/log --keyword fail
📜 License
MIT License © 2025 Arnazz10
