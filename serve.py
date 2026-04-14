from livereload import Server


DEFAULT_PORT = 8000
DEFAULT_PAGE = "index.html"


def main():
    server = Server()
    server.watch("*.html")
    server.watch("*.js")
    server.watch("*.css")
    server.watch("static/*.css")
    server.watch("static/*.js")
    server.serve(
        root=".",
        port=DEFAULT_PORT,
        default_filename=DEFAULT_PAGE,
    )


if __name__ == "__main__":
    main()