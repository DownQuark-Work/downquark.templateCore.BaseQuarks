"""Instantiate Successfully Configured Databases"""

from DownQuarkDatabase.Common import configuration
from DownQuarkDatabase.DatabaseTypes.MariaDB import relationaldb


class ActiveDatabases:
    @staticmethod
    def determine_active_dbs():
        print("configuration.DB_CONF", configuration.DB_CONF)
        relationaldb.print_dbs()

    def activate(self):
        print("initialize_active_databases")
        self.determine_active_dbs()
