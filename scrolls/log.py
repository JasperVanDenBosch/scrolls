

class Log(object):

    def __init__(self, dependencies):
        pass

    def foundPackage(self, pkg):
        t = '[scrolls] Found system package "{}".'
        print(t.format(pkg))

    def ranCommand(self, cmds, dryrun):
        if dryrun:
            t = '[scrolls] (dry run) Would have ran command "{}".'
        else:
            t = '[scrolls] Ran command "{}".'
        print(t.format(' '.join(cmds)))

    def wroteFile(self, fpath, contents, dryrun):
        if dryrun:
            t = '[scrolls] (dry run) Would have written {} characters to "{}".'
        else:
            t = '[scrolls] Wrote {} characters to file "{}".'
        print(t.format(len(contents), fpath))

    def selectedApplication(self, name, logfile):
        t = '[scrolls] Selected application "{}" with logfile "{}".'
        print(t.format(name, logfile))
