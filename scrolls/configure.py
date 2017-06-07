from copy import copy


def run():
    ## UDP /etc/rsyslog.conf
    uncomment('/etc/rsyslog.conf', ['$ModLoad imudp', '$UDPServerRun 514'])
    ## nginx


    ## sudo service rsyslog restart

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


if __name__ == '__main__':
    run()
