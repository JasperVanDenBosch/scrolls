import subprocess
import json
import os


class Filesystem(object):

    def __init__(self, dependencies):
        pass

    def write(self, path, contents):
        with open(path, 'w') as fh:
            fh.write(contents)

    def writeLines(self, path, lines):
        with open(path, 'w') as fh:
            fh.writelines(lines)

    def readLines(self, path):
        with open(path, 'r') as fh:
            lines = fh.readlines()
        return lines

    def read(self, path):
        with open(path, 'r') as fh:
            contents = fh.read()
        return contents

    def run(self, commands):
        subprocess.check_call(commands)

    def readJson(self, path):
        if not os.path.isfile(path):
            return None
        return json.loads(self.read(path))

    def writeJson(self, path, data):
        self.write(path, json.dumps(data))
