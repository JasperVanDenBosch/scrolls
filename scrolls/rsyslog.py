

class RSyslog(object):

    def __init__(self, dependencies):
        self.filesys = dependencies.getFilesystem()

    def configure(self, config):
        self.filesys.write('/etc/rsyslog.d/22-scrolls.conf',
                           FWD.replace('0.0.0.0', config.server))
        apps = config.selectApplications()
        appsconf = 'module(load="imfile")\n'
        template = 'input(type="imfile" File="{}" Tag="{}")\n'
        for appname, logpath in apps.items():
            appsconf += template.format(logpath, appname)
        self.filesys.write('/etc/rsyslog.d/23-scrolls-apps.conf', appsconf)
        self.filesys.run(['service', 'rsyslog', 'restart'])


FWD = """
# Setup disk assisted queues
$WorkDirectory /var/spool/rsyslog # where to place spool files
$ActionQueueFileName fwdRule1     # unique name prefix for spool files
$ActionQueueMaxDiskSpace 1g       # 1gb space limit (use as much as possible)
$ActionQueueSaveOnShutdown on     # save messages to disk on shutdown
$ActionQueueType LinkedList       # run asynchronously
$ActionResumeRetryCount -1        # infinite retries if host is down

# Send messages to Scrolls over TCP using the template.
action(type="omfwd" protocol="udp" target="0.0.0.0" port="8514"
       template="RSYSLOG_SyslogProtocol23Format")
"""
