import os
from werkzeug.exceptions import HTTPException
from werkzeug.wrappers import Request, Response
from werkzeug.wsgi import SharedDataMiddleware

from webapp import AwesomeWeblog


class WebAppLoader(object):
    def __init__(self):
        self.app = AwesomeWeblog()
        self.url_map = self.app.get_urls()

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()

            result = getattr(self.app, endpoint)(request, **values)
            if isinstance(result, Response):
                return result
            elif isinstance(result, str) or isinstance(result, unicode):
                return Response(result, mimetype='text/html')
        except HTTPException, e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app(with_static=True):
    app = WebAppLoader()
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static': os.path.join(os.path.dirname(__file__), 'static')
        })

    return app


if __name__ == "__main__":
    from werkzeug.serving import run_simple

    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)
