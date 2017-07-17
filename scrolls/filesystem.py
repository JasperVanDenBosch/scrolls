import subprocess
import json
import os


class Filesystem(object):

    def __init__(self, dependencies):
        self.config = dependencies.getConfiguration()
        self.log = dependencies.getLog()

    def write(self, path, contents, silent=False):
        if not self.config.dry_run:
            with open(path, 'w') as fh:
                fh.write(contents)
        if not silent:
            self.log.wroteFile(path, contents, self.config.dry_run)

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
        if not self.config.dry_run:
            subprocess.check_call(commands)
        self.log.ranCommand(commands, self.config.dry_run)

    def readJson(self, path):
        if not os.path.isfile(path):
            return None
        return json.loads(self.read(path))

    def writeJson(self, path, data):
        self.write(path, json.dumps(data), silent=True)

    def hasPackage(self, pkgName):
        try:
            subprocess.check_output(['dpkg', '-s', pkgName],
                                    stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError:
            return False
        else:
            self.log.foundPackage(pkgName)
            return True
