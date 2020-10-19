#!/usr/bin/env python3
"""
Copyright 2020 Nico Erfurth

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from azure.cosmos import CosmosClient

import json
import sys
import os

cosmosdb_cstr = os.environ.get('COSMOSDB_CONNECTION_STRING', None)
cosmosdb_db_name = os.environ.get('COSMOSDB_DATABASE', None)
cosmosdb_container_name = os.environ.get('COSMOSDB_CONTAINER', None)

if (cosmosdb_cstr is None or
    cosmosdb_db_name is None or
    cosmosdb_container_name is None):
    print("Please set COSMOSDB_CONNECTION_STRING, COSMOSDB_DATABASE and COSMOSDB_CONTAINER appropriately", file=sys.stderr)
    sys.exit(-1)

cosmosdb_client = CosmosClient.from_connection_string(cosmosdb_cstr)
cosmosdb_db = cosmosdb_client.get_database_client(cosmosdb_db_name)
cosmosdb_container = cosmosdb_db.get_container_client(cosmosdb_container_name)

def print_status(headers, properties):
    print(json.dumps({'headers:': headers, 'properties': properties}, sort_keys=True, indent=4))

cosmosdb_container.read(populate_quota_info = True,
                        populate_partition_key_range_statistics = True,
                        response_hook = print_status)

