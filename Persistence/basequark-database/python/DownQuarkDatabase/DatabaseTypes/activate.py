"""Instantiate Successfully Configured Databases"""

from DownQuarkDatabase.Common import configuration


class ActiveDatabases:
    @staticmethod
    def determine_active_dbs():
        print("configuration.DB_CONF", configuration.DB_CONF)

    def activate(self):
        print("initialize_active_databases")
        self.determine_active_dbs()
