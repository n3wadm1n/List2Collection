# List2Collection
The List2Collection automates the creation of a Postman collection based on user inputs for host, collection name, method, and path(route+endpoint) or endpoint.

### User Input
The script prompts the user to enter the host, collection name, and the filename of the method_and_path file.

### Read Method and Endpoint Information
The script reads the method and path(route+endpoint) or endpoint information from the specified "method_url.txt" file.

### Generate Postman Requests
For each method and endpoint combination, the script generates a Postman request object with default headers, using the provided host and endpoint information.

### Create Postman Collection
The script organizes the generated requests into a Postman collection, using the specified collection name.

### User Input for JSON Filename
The script prompts the user to input the desired filename for the resulting Postman collection JSON file.

### Save Collection to JSON
Finally, the script saves the Postman collection as a JSON file using the specified filename.
