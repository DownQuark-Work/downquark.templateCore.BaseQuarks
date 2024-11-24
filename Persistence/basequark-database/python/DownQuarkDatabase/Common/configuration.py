"""stores connection and other re-usable information"""

import copy

from .constants import DB_TYPES, DB_CREDENTIAL_KEYS

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
DB_CONF_DEFAULT_VALUES = {
    "CREDENTIALS": {
        KEY_ARANGO: CREDENTIALS_ARANGO,
        KEY_MARIA: CREDENTIALS_MARIA,
        KEY_POSTGRES: CREDENTIALS_POSTGRES,
    }
}
DB_CONF = copy.deepcopy(DB_CONF_DEFAULT_VALUES)


class DownQuarkDatabaseConfiguration:
    def reset(self):
        DB_CONF["CREDENTIALS"] = copy.deepcopy(DB_CONF_DEFAULT_VALUES["CREDENTIALS"])

    def run(self):
        print("Configue Database Information")
        print("DB_CONF", DB_CONF)
        pass
