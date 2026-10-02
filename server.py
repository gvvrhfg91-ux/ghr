import http.server
import socketserver
import webbrowser
import threading
import os

PORT = 8000

# работаем из папки, где лежит сам скрипт
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

def open_browser():
    webbrowser.open(f"http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Сервер запущен: http://localhost:{PORT}")
    threading.Timer(1.5, open_browser).start()  # открыть браузер через 1,5 сек
    httpd.serve_forever()
