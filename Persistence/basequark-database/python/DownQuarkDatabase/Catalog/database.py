"""Currently a _very_ lightweight wrapper. As it is implemented in future contexts there will be updates to make it act more like a customized ORM"""


class DatabaseCatalog:
    """catalog of multiple static methods that are executed depending on an init parameter"""

    # def develop: # allows local/testing implementation that does not require an active database
    # optional mock data can be passed as an argument which will be returned exactly as the database query result would be from the `process` method
    # def query: # applies the query string to the desired database and passes the
    # def process: # will return the output from the query
