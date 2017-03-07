import os
import tornado.web


class DocsHandler(tornado.web.RequestHandler):

    def get(self):
        version = "{}://{}/docs/version/v1.yml".format(
            self.request.protocol, self.request.host)
        self.render("swagger/index.html", version=version)


class CachingFrontendHandler(tornado.web.StaticFileHandler):
    def __init__(self, *args, **kwargs):
        self.__root = None
        super(CachingFrontendHandler, self).__init__(*args, **kwargs)

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, value):
        self.__root = value

    def get(self, path, include_body=True):
        print("serving %s from CachingFileHandler" % path)
        return super(CachingFrontendHandler, self).get(path, include_body)


class HomeHandler(tornado.web.StaticFileHandler):
    def get(self, path, include_body=True):
        print("serving %s from HomeHandler" %path)
        super(HomeHandler, self).get('index.html', include_body)
