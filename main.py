from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class MyServer(BaseHTTPRequestHandler):
    """
    Simple HTTP server class based on BaseHTTPRequestHandler.

    Attributes:
        None
    """

    def do_GET(self):
        """
        Handle GET requests.

        If the path is "/", return the page from Task 1.
        Otherwise, return a 404 Not Found error.

        Args:
            None

        Returns:
            None
        """
        if self.path == "/":
            # If the path is root ("/"), return the page from Task 1
            page_content = self.read_file("static/index.html")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(page_content, "utf-8"))
        else:
            # If the path is not root, return a 404 Not Found error
            self.send_error(404, "Not Found")

    def read_file(self, file_path):
        """
        Read the content of a file.

        Args:
            file_path (str): The path of the file to be read.

        Returns:
            str: The content of the file.
        """
        with open(file_path, "r") as f:
            return f.read()


if __name__ == "__main__":
    webServer = HTTPServer(("localhost", 8090), MyServer)
    print("Server started http://%s:%s" % webServer.server_address)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
