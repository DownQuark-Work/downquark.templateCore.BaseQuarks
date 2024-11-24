"""DownQuark Database Utilities"""

# from DownQuarkDatabase.Common.configuration import DownQuarkDatabaseConfiguration as configDqDb
from DownQuarkDatabase.Common import configuration
from DatabaseTypes.activate import ActiveDatabases

configDqDb = configuration.DownQuarkDatabaseConfiguration


def required_before_run():
    """Initializes and verifies connections to specified database"""
    print("all required data has been retrieved, parsed, and handled")
    print(
        "what we were looking for to make the demo: https://github.com/swyxio/uuid-list"
    )
    # # configDqDb.reset() # sets back to _all_ databases having localhost connections
    # # configDqDb.update(['ARANGO'],('bob','dole','a','x')) # sets back to _all_ databases having localhost connections

    # clearing and adding only what is needed helps for development
    configDqDb.clear()
    arango_config_credentials = configuration.DB_CONF_DEFAULT_VALUES["CREDENTIALS"].get(
        "MARIA"
    )
    configDqDb.update(["MARIA"], arango_config_credentials)

    # the `update` usage will vary with different implementations so will most likely need to be
    #  refactored as we determine use cases with the upcoming projects
    # the line below proves it working concept
    # print("update with non test vals", DB_CONF)
    # pass


if __name__ == "__main__":
    required_before_run()
    print("DB_CONFIG_DEFAULT_VALUES", configuration.DB_CONF)
    ActiveDatabases.activate()
