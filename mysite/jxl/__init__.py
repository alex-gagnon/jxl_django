import os

PROJECT_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.dirname(os.path.abspath(__file__))

try:
    os.stat(os.path.join(FILE_PATH, 'assets'))
except FileNotFoundError:
    os.mkdir(os.path.join(FILE_PATH, 'assets'))
finally:
    FILE_PATH = os.path.join(FILE_PATH, 'assets')
