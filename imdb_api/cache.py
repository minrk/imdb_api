"""basic cache util"""

import json
import time
from os import path
from datetime import datetime

class Cache(dict):
    """Global Cache dict"""
    filename = None
    def __init__(self, filename=None):
        super(Cache, self).__init__()
        self.filename = filename
        if filename is not None:
            self.init_cache_file()
    
    def init_cache_file(self):
        if path.isfile(self.filename):
            with open(self.filename, 'r') as f:
                jdata = f.read()
            self.update(json.loads(jdata))
    
    def save_cache_file(self):
        with open(self.filename, 'w') as f:
            f.write(json.dumps(dict(self)))
    
    def __del__(self):
        if self.filename:
            self.save_cache_file()
        