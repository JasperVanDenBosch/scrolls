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

    subparsers.add_parser(
        'listen',
        help='Record incoming log messages.')

    subparsers.add_parser(
        'serve',
        help='Start a webserver that allows scrolling through the logs.')

    args = parser.parse_args()

    dependencies = scrolls.dependencies.Dependencies()
    config = dependencies.getConfiguration()
    config.useCommandlineArgs(args)
    if args.command == 'configure':
        dependencies.getRSyslog().configure(config)
    elif args.command == 'listen':
        dependencies.getListener().listen()
    elif args.command == 'serve':
        print('serve')
