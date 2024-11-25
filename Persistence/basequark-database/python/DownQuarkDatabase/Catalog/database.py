"""Currently a _very_ lightweight wrapper. As it is implemented in future contexts there will be updates to make it act more like a customized ORM"""


class DatabaseCatalog:
    """catalog of multiple static methods that are executed depending on an init parameter"""

    # def activate: # move activation calls here
    # def develop: # allows local/testing implementation that does not require an active database
    # -- optional mock data can be passed as an argument which will be returned exactly as the database query result would be from the `process` method
    # def query: # applies the query string to the desired database and returns the results to the `process` function
    # -- should probably be chainable: `.query("INSERT INTO...").query("SELECT * FROM...").process()
    # ---- https://github.com/faif/python-patterns/blob/master/patterns/behavioral/chaining_method.py
    # def process: # will format the output from the query, then run the callback function (if exists) passing the formatted result(s) as `*args`
