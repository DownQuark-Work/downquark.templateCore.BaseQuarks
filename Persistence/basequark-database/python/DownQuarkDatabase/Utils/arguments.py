"""parses arguments from the command line to allow idempotence between the CLI and module implementations"""

import argparse
import sys

from DownQuarkDatabase.Common.constants import DB_TYPES

parser = argparse.ArgumentParser()


def init_args():
    parser.add_argument(
        "db_type",
        choices=DB_TYPES,
        type=str,
        help="Data Persists to DataBase of this type",
    )
    parser.add_argument(
        "query-file",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="optional file to use for source of db-type queries",
    )
    parser.add_argument(
        "callback-location",
        nargs="?",
        type=argparse.FileType("w"),
        const=sys.stdout,
        default=sys.stdout,
        help="the cli currently only supports writing the response to the command line",
    )
    parser.add_argument(
        "-c,--credentials",
        nargs="*",
        type=str,
        help="Credentials used when connecting to the db-type. Not all values may be required. Expected in the order of: [user, password, host, port]",
        metavar=("admin_user", " secret_pw 127.0.0.1 1342"),
    )
    parser.add_argument(
        "-q",
        "--query",
        action="extend",
        nargs="+",
        type=str,
        help="space separated list of strings to be queried by db-type. They will run sequentially",
        metavar=('"SELECT * FROM ...."', '"INSERT INTO ...."'),
    )
    parser.add_argument(
        "-D", "--DEV", action="store_true", help="Enables development mode"
    )
    parser.add_argument(
        "-m",
        "--mock",
        type=str,
        help="A mock implementation of what would be returned after all queries and processing had completed. No database call or connection will actually occur. Only available in development mode",
        metavar='{ "query_response" : "mock_data" : {} }',
    )
    parser.print_help()
    # parser.print_usage()
    args = parser.parse_args()

    # for arg in args:
    print("->", args)


# https://docs.python.org/3/library/argparse.html
# https://docs.python.org/3/howto/argparse.html#argparse-tutorial
