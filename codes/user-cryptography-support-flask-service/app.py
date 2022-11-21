from flask import Flask, redirect, url_for, request
from flask_cors import CORS
from services import YiModifiedPaillierEncryptionPy
import unittest
import sys

app = Flask(__name__)
CORS(app)

# API
@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

# Flask 命令行
@app.cli.command()
def test():
  """
  運作測試
  """
  tests = unittest.TestLoader().discover("tests")
  result = unittest.TextTestRunner(verbosity=2).run(tests)
  if result.errors or result.failures:
      sys.exit(1)