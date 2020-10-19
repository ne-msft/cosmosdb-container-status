cosmos db container status
===
Just a quick tool to read container status from a cosmosdb, including reindex percentage.
This will only output the headers and properties of that container, nice to get a quick view during development.
Output is a json object, with "properties" and "headers" keys. This allows for easy processing using jq or similar tools.

All parameters live as environment variables:
* COSMOSDB_CONNECTION_STRING
* COSMOSDB_DATABASE
* COSMOSDB_CONTAINER
