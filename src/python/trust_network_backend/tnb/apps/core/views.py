import os
import tornado.web


class HomeHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello world")


class DocsHandler(tornado.web.RequestHandler):

    def get(self):
        version = "{}://{}/docs/version/v1.yml".format(self.request.protocol,
                                                       self.request.host)
        self.render("swagger/index.html", version=version)


class FrontendStaticHandler(tornado.web.StaticFileHandler):
    def initialize(self, path):
        self.dirname, self.filename = os.path.split(path)
        super(FrontendStaticHandler, self).initialize(self.dirname)

    def get(self, path=None, include_body=True):
        # Ignore 'path'.
        super(FrontendStaticHandler, self).get(self.filename, include_body)
