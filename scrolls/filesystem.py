import subprocess


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

    def run(self, commands):
        subprocess.check_call(commands)
