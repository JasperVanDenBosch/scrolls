#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
import scrolls.dependencies


def main():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command",
        title='subcommands')
    subparsers.required = True

    configure = subparsers.add_parser('configure',
        help='Configure system to send log events to scrolls server.')

    listen = subparsers.add_parser('listen',
        help='Record incoming log messages.')

    serve = subparsers.add_parser('serve',
        help='Start a webserver that allows scrolling through the logs.')

    args = parser.parse_args()

    dependencies = scrolls.dependencies.Dependencies()

    if args.command == 'configure':
        print('configure')
    elif args.command == 'listen':
        dependencies.getListener().listen()
    elif args.command == 'serve':
        print('serve')
