# LIbrary Method Documentation for NewsScrpaerLib

## All Methods

- headlineGatherer(url, tag, className):
  Function to return an array of headlines from a given URL and HTML tag.

  Args:
  url (str): URL for the site being used to gather headlines from.
  tag (str): HTML tag for attribute(s) being gathered (eg.. 'h1', 'h2').
  className (str): CSS Selector class for attribute(s) being gathered. Should be a subset of the provided tag.

  Returns:
  List: Result of the function is an list of headline text gathered from the URL provided.

- headlineStorer(dbFilePath, dfHeadline):
  Method to create/add headline list data into a SQLite3 database in the local filesystem.

  Args:
  dbFilePath (str): New or Existing name for the local database to be generated.
  dfHeadline (obj): List object of headlines, ex.. output from headlineGatherer method.

- show_records(dbFilePath, selection):
  Method to show all records that are present in the local SQLite3 database

  Args:
  dbFilePath (str): Name of the local databaase
  selection (str): Parameter to pass to the "WHERE" clause in the SQL statement

  Returns:
  object: Python object (list) containing the query results

- show_all_records(dbFilePath):
  Method to return all records in the local SQLite3 database instance.

  Args:
  dbFilePath (str): Name of the local database

  Returns:
  object: Python object (list) containing the query results

- add_to_mysql(host, user, password, database, values):
  Method to add headlines to MySQL database. This method does not create schemas or databases on the MySQL server.

  Args:
  host (str): Host name of MySQL server
  user (str): Username used on MySQL server
  password (str): Password used on MySQL server
  database (str): Database name
  values (list): Python list of content to add to the database
