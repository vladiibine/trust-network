import os

from tornado import gen
import tornado.web


class DocsHandler(tornado.web.RequestHandler):

    def get(self):
        version = "{}://{}/docs/version/v1.yml".format(
            self.request.protocol, self.request.host)
        self.render("swagger/index.html", version=version)


class HomeHandler(tornado.web.StaticFileHandler):
    @gen.coroutine
    def get(self, path, include_body=True):

        yield super().get('index.html', include_body)


class CachingFrontendHandler(tornado.web.StaticFileHandler):
    """If a file exists in the root folder, serve it, otherwise serve index.html

    """
    @gen.coroutine
    def get(self, path, include_body=True):
        absolute_path = self.get_absolute_path(self.root, path)

        is_file = os.path.isfile(absolute_path)

        if is_file:
            yield super().get(path, include_body)
        else:
            yield super().get('index.html', include_body)

