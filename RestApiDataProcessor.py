import requests

# Step 1: Fetch data from the first API
def fetch_data_from_first_api():
    # Replace this URL with the actual URL of your first API endpoint
    first_api_url = "https://jsonplaceholder.typicode.com/todos/1"
    
    # Make a GET request to the first API
    response = requests.get(first_api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return data
    else:
        # Print an error message if the request fails
        print(f"Failed to fetch data from the first API. Status code: {response.status_code}")
        return None

# Step 2: Process the data
def process_data(data):
    # For simplicity, let's just extract the 'title' field from the data
    processed_data = data.get('title', None)
    return processed_data

# Step 3: Manipulate the data
def manipulate_data(data):
    # For simplicity, let's just add a prefix to the data
    manipulated_data = f"Modified: {data}"
    return manipulated_data

# Step 4: Send data to the second API
def send_data_to_second_api(data):
    # Replace this URL with the actual URL of your second API endpoint
    second_api_url = "https://jsonplaceholder.typicode.com/posts"
    
    # Set the headers for the POST request
    headers = {"Content-Type": "application/json"}
    
    # Make a POST request to the second API with the manipulated data
    response = requests.post(second_api_url, json={"title": data}, headers=headers)

    # Check if the request was successful (status code 201 for successful creation)
    if response.status_code == 201:
        print("Data successfully sent to the second API")
    else:
        # Print an error message if the request fails
        print(f"Failed to send data to the second API. Status code: {response.status_code}")

# Main function to orchestrate the process
def main():
    # Step 1: Fetch data from the first API
    data_from_first_api = fetch_data_from_first_api()

    # Check if data was successfully fetched
    if data_from_first_api:
        # Step 2: Process the data
        processed_data = process_data(data_from_first_api)

        # Step 3: Manipulate the data
        manipulated_data = manipulate_data(processed_data)

        # Step 4: Send data to the second API
        send_data_to_second_api(manipulated_data)

# Entry point for the script
if __name__ == "__main__":
    main()
