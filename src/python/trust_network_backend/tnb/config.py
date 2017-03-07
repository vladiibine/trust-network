from os.path import abspath, dirname, join

PYTHON_PROJECT_DIR = abspath(dirname(dirname(__file__)))
ASSETS_FOLDER = join(dirname(dirname(dirname(PYTHON_PROJECT_DIR))), 'dist')
