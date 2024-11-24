"""DownQuark Database Utilities"""

# from DownQuarkDatabase.Common.configuration import DownQuarkDatabaseConfiguration as configDqDb
from DownQuarkDatabase.Common import configuration

configDqDb = configuration.DownQuarkDatabaseConfiguration


def required_before_run():
    """Initializes and verifies connections to specified database"""
    print("all required data has been retrieved, parsed, and handled")
    print(
        "what we were looking for to make the demo: https://github.com/swyxio/uuid-list"
    )
    print("DownQuarkDatabaseConfiguration()", configDqDb.reset())
    # the `update` usage will vary with different implementations so will most likely need to be
    #  refactored as we determine use cases with the upcoming projects
    # the line below proves it working concept
    # print("update with non test vals", configDqDb.update(['ARANGO'],('bob','dole','a','x')))
    pass


if __name__ == "__main__":
    required_before_run()
    print("DB_CONFIG_DEFAULT_VALUES", configuration.DB_CONF)
    # BaseQuark.run()
