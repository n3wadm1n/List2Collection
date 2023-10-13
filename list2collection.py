#!/usr/bin/python3
####################
################
### n3wadm1n #####
### Euribot  #####
#####################

import readline,json,time,os

readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")

def generate_postman_request(method, host, endpoint):
    url = f"https://{host}{endpoint}"
    request = {
        "header": [
            {"key": "User-Agent", "value": "curl/7.74.0"},
            {"key": "Accept", "value": "*/*"}
        ],
        "url": url,
        "method": method,
        "body": None
    }

    return request

host = input("Enter the Host: ")

collection_name = input("Enter the collection's name: ")


method_url_filename = input("Enter the filename that contains (METHOD PATH(ROUTE/ENDPOINT)), e.g. method_path.txt: ")


method_url_list = []
with open(method_url_filename, 'r') as file:
    method_url_list = [line.strip().split(' ') for line in file.readlines()]


postman_items = []
for method, endpoint in method_url_list:
    request_item = {
        "name": f"Ref. {endpoint}",
        "request": generate_postman_request(method, host, endpoint)
    }
    postman_items.append(request_item)

postman_collection = {
    "info": {
        "name": collection_name,
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "item": postman_items
}

json_filename = input("Enter the JSON's filename to output': ").replace(".json","").replace(".txt","")


with open(f'{json_filename}.json', 'w') as file:
    json.dump(postman_collection, file, indent=4)

print(f"Done! Filename: {json_filename}.json")

time.sleep(5)
os.system('clear')
