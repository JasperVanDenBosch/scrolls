from copy import copy


class RSyslog(object):

    def __init__(self, dependencies):
        self.filesys = dependencies.getFilesystem()

    def configure(self, config):
        directives = ['$MaxMessageSize 64k']
        self.ensureDirectives('/etc/rsyslog.conf', directives)
        self.filesys.write('/etc/rsyslog.d/22-scrolls.conf',
                           FWD.replace('0.0.0.0', config.server))
        self.filesys.write('/etc/rsyslog.d/41-nginx.conf',
                           NGINX.replace('0.0.0.0', config.server))
        self.filesys.run(['service', 'rsyslog', 'restart'])

    def ensureDirectives(self, fpath, statements):
        foundStatements = {s: False for s in statements}
        oldlines = self.filesys.readLines(fpath)
        newlines = copy(oldlines)
        for l, line in enumerate(oldlines):
            for statement in statements:
                if statement in line:
                    foundStatements[statement] = True
                    if '#' in line:
                        print('uncommenting')
                        newlines[l] = line.replace('#', '')
                    else:
                        print('already uncommented')
        for statement, found in foundStatements.items():
            if not found:
                print('adding new')
                newlines.append(statement+'\n')
        if newlines == oldlines:
            print('no changes necessary')
        else:
            print('saving edited file')
            self.filesys.writeLines(fpath, newlines)


NGINX = """
$ModLoad imfile
$InputFilePollInterval 3
$PrivDropToGroup adm
$WorkDirectory /var/spool/rsyslog

# Nginx access file:
$InputFileName /var/log/nginx/access.log
$InputFileTag nginx-access:
$InputFileStateFile stat-nginx-access
$InputFileSeverity info
$InputFilePersistStateInterval 20000
$InputRunFileMonitor

#Nginx Error file:
$InputFileName /var/log/nginx/error.log
$InputFileTag nginx-error:
$InputFileStateFile stat-nginx-error
$InputFileSeverity error
$InputFilePersistStateInterval 20000
$InputRunFileMonitor

if $programname == 'nginx-access' then action(type="omfwd" protocol="udp" target="0.0.0.0" port="8514" template="RSYSLOG_SyslogProtocol23Format")
if $programname == 'nginx-error' then action(type="omfwd" protocol="udp" target="0.0.0.0" port="8514" template="RSYSLOG_SyslogProtocol23Format")
"""

FWD = """
# Setup disk assisted queues
$WorkDirectory /var/spool/rsyslog # where to place spool files
$ActionQueueFileName fwdRule1     # unique name prefix for spool files
$ActionQueueMaxDiskSpace 1g       # 1gb space limit (use as much as possible)
$ActionQueueSaveOnShutdown on     # save messages to disk on shutdown
$ActionQueueType LinkedList       # run asynchronously
$ActionResumeRetryCount -1        # infinite retries if host is down

# Send messages to Scrolls over TCP using the template.
action(type="omfwd" protocol="udp" target="0.0.0.0" port="8514" template="RSYSLOG_SyslogProtocol23Format")
"""
