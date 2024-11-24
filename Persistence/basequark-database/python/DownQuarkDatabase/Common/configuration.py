"""stores connection and other re-usable information"""

from .constants import DB_TYPES, DB_CREDENTIAL_KEYS

DB_CONFIG_DEFAULT_VALUES = {  # set to typical local development defaults
    "one": "two",
    "three": "four",
}
[KEY_DB_USER, KEY_DB_PASSWORD, KEY_DB_HOST, KEY_DB_PORT] = DB_CREDENTIAL_KEYS
[INDX_DB_USER, INDX_DB_PASSWORD, INDX_DB_HOST, INDX_DB_PORT] = list(
    map(
        lambda credKey: DB_CREDENTIAL_KEYS.index(credKey),
        [KEY_DB_USER, KEY_DB_PASSWORD, KEY_DB_HOST, KEY_DB_PORT],
    )
)
[KEY_ARANGO, KEY_MARIA, KEY_POSTGRES] = DB_TYPES
CREDENTIALS_ARANGO = ("root", "root", "localhost", "8529")
CREDENTIALS_MARIA = ("username", "root", "localhost", "3666")
CREDENTIALS_POSTGRES = ("postgres", "root", "localhost", "5432")
DB_CONF = {
    "CREDENTIALS": {
        KEY_ARANGO: CREDENTIALS_ARANGO,
        KEY_MARIA: CREDENTIALS_MARIA,
        KEY_POSTGRES: CREDENTIALS_POSTGRES,
    }
}


class DownQuarkDatabaseConfiguration:
    DB_CONFIG = {"1": "DB_CONFIG_DEFAULT_VALUES"}

    def reset(self):
        print("NOSET", self.DB_CONFIG)
        self.DB_CONFIG = DB_CONFIG_DEFAULT_VALUES
        print("resseted", self.DB_CONFIG)

    def run(self):
        print("Configue Database Information")
        print("NOSET", self.DB_CONFIG)
        print("DB_CONFIG_DEFAULT_VALUESINTERNAL", DB_CONFIG_DEFAULT_VALUES)
        print("REFACTrored DB_CONF", DB_CONF["CREDENTIALS"][KEY_ARANGO][INDX_DB_HOST])
        pass
