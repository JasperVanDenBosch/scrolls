#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
import scrolls.dependencies


def main():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        dest="command",
        title='subcommands')
    subparsers.required = True

    configure = subparsers.add_parser(
        'configure',
        help='Configure system to send log events to scrolls server.')
    configure.add_argument(
        '--server',
        default=argparse.SUPPRESS,
        help='The hostname of the machine running scrolls.')
    configure.add_argument(
        '--dry-run', '-d',
        action='store_const',
        const=True,
        default=False,
        help='Simulate configure() but don\'t make any filesystem changes.')

    subparsers.add_parser(
        'listen',
        help='Record incoming log messages.')

    subparsers.add_parser(
        'serve',
        help='Start a webserver that allows scrolling through the logs.')

    secrets = subparsers.add_parser(
        'generate-secrets',
        help='Print credentials to insert in your scrolls.conf file.')
    secrets.add_argument(
        'password',
        help='A password of your choice.')

    args = parser.parse_args()

    dependencies = scrolls.dependencies.Dependencies()
    config = dependencies.getConfiguration()
    config.useCommandlineArgs(args)
    if args.command == 'configure':
        dependencies.getRSyslog().configure(config)
    elif args.command == 'listen':
        dependencies.getListener().listen()
    elif args.command == 'serve':
        dependencies.getServer().serve(config)
    elif args.command == 'generate-secrets':
        creds = dependencies.getSecurity().generateSecrets(args.password)
        print('Add these lines to your scrolls.conf file to enable password-' +
              'based authentication in the web app:\n')
        for key, value in creds.items():
            print('{} = {}'.format(key, value))
        print()
