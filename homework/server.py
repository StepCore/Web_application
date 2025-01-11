from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from urllib.parse import unquote

hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """Специальный класс, который отвечает за обработку входящих запросов от клиентов"""

    def do_GET(self):
        if self.path == "/":
            self.serve_file("home.html")
        elif self.path == "/catalog":
            self.serve_file("catalog.html")
        elif self.path == "/category_1":
            self.serve_file("category_1.html")
        elif self.path == "/contact":
            self.serve_file("contact.html")
        elif self.path.startswith("/css/"):
            self.serve_static_file(self.path, "text/css")
        elif self.path.startswith("/js/"):
            self.serve_static_file(self.path, "application/javascript")
        elif self.path.startswith("/images/"):
            self.serve_static_file(self.path, "image/jpeg")
        else:  # Если путь не найден
            self.send_error(404, "Page Not Found")

    def serve_file(self, filename):
        """Обслуживает HTML-файлы"""
        filepath = os.path.join(os.path.dirname(__file__), filename)
        try:
            # Проверяем, существует ли файл
            if not os.path.exists(filepath):
                self.send_error(404, "File Not Found")
                return

            # Читаем содержимое файла
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()

            # Отправляем заголовки
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Отправляем содержимое файла
            self.wfile.write(bytes(content, "utf-8"))
        except Exception as e:
            # Обрабатываем ошибки
            self.send_error(500, f"Server Error: {e}")

    def serve_static_file(self, path, content_type):
        """Обслуживает статические файлы (CSS, JS, изображения)"""
        # Убираем первый символ `/` и декодируем путь
        filepath = os.path.join(os.path.dirname(__file__), "..", unquote(path[1:]))

        try:
            if not os.path.exists(filepath):
                self.send_error(404, "Static File Not Found")
                return

            self.send_response(200)
            self.send_header("Content-type", content_type)
            self.end_headers()

            # Читаем файл в бинарном режиме и отправляем его содержимое
            with open(filepath, "rb") as file:
                self.wfile.write(file.read())
        except Exception as e:
            self.send_error(500, f"Server Error: {e}")


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
