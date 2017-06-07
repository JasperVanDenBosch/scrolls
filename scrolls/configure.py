import subprocess
from copy import copy


def run():
    ## UDP /etc/rsyslog.conf
    uncomment('/etc/rsyslog.conf', ['$ModLoad imudp', '$UDPServerRun 514'])
    ## nginx
    with open('/etc/rsyslog.d/41-nginx.conf', 'w') as fh:
        fh.write(NGINX)
    ## sudo service rsyslog restart
    subprocess.check_call(['service', 'rsyslog', 'restart'])

def uncomment(fpath, statements):
    found = {s:False for s in statements}
    with open(fpath, 'r') as fh:
        oldlines = fh.readlines()
    newlines = copy(oldlines)
    for l, line in enumerate(oldlines):
        for statement in statements:
            if statement in line:
                found[statement] = True
                if '#' in line:
                    print('uncommenting')
                    newlines[l] = line.replace('#', '')
                else:
                    print('already uncommented')
    if list(found.values()).count(False):
        print('Not all stmts found')
    if newlines == oldlines:
        print('no changes necessary')
    else:
        print('saving edited file')
        with open(fpath, 'w') as fh:
            fh.writelines(newlines)

NGINX = """
$ModLoad imfile
$InputFilePollInterval 10
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

#Add a tag for nginx events
$template ScrollsFormatNginx,"<%pri%>%protocol-version% %timestamp:::date-rfc3339% %HOSTNAME% %app-name% %procid% %msgid% [tag=\"nginx\"] %msg%\n"

if $programname == 'nginx-access' then @@0.0.0.0:514;ScrollsFormatNginx
if $programname == 'nginx-access' then ~
if $programname == 'nginx-error' then @@0.0.0.0:514;ScrollsFormatNginx
if $programname == 'nginx-error' then ~
"""


if __name__ == '__main__':
    run()
