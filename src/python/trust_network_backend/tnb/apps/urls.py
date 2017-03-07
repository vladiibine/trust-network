import os

from tornado import web
from tornado.web import URLSpec as url

from tnb.contrib.urls import include
from tnb.settings import settings
from tnb.apps.core.views import (DocsHandler, CachingFrontendHandler, HomeHandler)
from tnb.config import PYTHON_PROJECT_DIR, ASSETS_FOLDER


print(" I am vlad " * 80)
print("asserts folder %s" % ASSETS_FOLDER)


urls = [
    # TODO the "^$" handler must return index.html
    url(r"^/?(.*)$", HomeHandler, {'path': ASSETS_FOLDER}),
    url(r"^/docs$", DocsHandler),
    url(r"^/docs/version/(.*)$", web.StaticFileHandler, {"path": settings.DOCS_ROOT}),
    url(r"^/static/(.*)$", web.StaticFileHandler, {"path": settings.STATIC_ROOT}),
    # url(r"(.*)", FrontendStaticHandler, {
    #     'path': os.path.join(PYTHON_PROJECT_DIR, 'dist/index.html')
    # }),
    url(r"^/(.*)$", CachingFrontendHandler, {'path': ASSETS_FOLDER}),
]

urls += include(r"/healthcheck", "tnb.apps.core.urls")
urls += include(r"/customers", "tnb.apps.customers.urls")
