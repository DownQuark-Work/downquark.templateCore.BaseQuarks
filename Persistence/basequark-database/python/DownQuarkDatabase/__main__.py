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
    print("DownQuarkDatabaseConfiguration()", configDqDb().reset())
    # https://www.uuidgenerator.net/
    # https://github.com/mdipierro/ulid
    # https://crates.io/crates/ulid%20%7C%20https://github.com/dylanhart/ulid-rs
    # https://github.com/lukeed/hexoid
    pass


if __name__ == "__main__":
    required_before_run()
    configDqDb().run()
    print("DB_CONFIG_DEFAULT_VALUES", configuration.DB_CONFIG_DEFAULT_VALUES)
    configuration.DB_CONFIG_DEFAULT_VALUES = {"b": "v"}
    print("DB_CONFIG_DEFAULT_VALUES", configuration.DB_CONFIG_DEFAULT_VALUES)
    configDqDb().run()
    # BaseQuark.run()
