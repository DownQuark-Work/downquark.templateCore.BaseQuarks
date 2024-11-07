"""E"""

from .basequark import BaseQuark


def required_before_run():
    print("all required data has been retrieved, parsed, and handled")
    print(
        "what we were looking for to make the demo: https://github.com/swyxio/uuid-list"
    )
    # https://www.uuidgenerator.net/
    # https://github.com/mdipierro/ulid
    # https://crates.io/crates/ulid%20%7C%20https://github.com/dylanhart/ulid-rs
    # https://github.com/lukeed/hexoid
    pass


if __name__ == "__main__":
    required_before_run()
    BaseQuark.run()
