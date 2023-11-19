from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8090


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            # Если путь корневой, возвращаем страницу из Задания 1
            page_content = self.read_file("static/index.html")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(page_content, "utf-8"))
        else:
            # В противном случае возвращаем 404
            self.send_error(404, "Not Found")

    def read_file(self, file_path):
        with open(file_path, "r") as f:
            return f.read()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
