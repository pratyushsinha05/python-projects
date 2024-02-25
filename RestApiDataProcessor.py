import requests

# Step 1: Hit the first REST API endpoint and get the data
first_api_url = "https://example.com/first_endpoint"
response = requests.get(first_api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Step 2: Process the data
    data = response.json()  # Assuming the response is in JSON format
    processed_data = process_data(data)

    # Step 3: Manipulate data (if needed)
    manipulated_data = manipulate_data(processed_data)

    # Step 4: Send data to another REST API endpoint
    second_api_url = "https://example.com/second_endpoint"
    headers = {"Content-Type": "application/json"}
    response = requests.post(second_api_url, json=manipulated_data, headers=headers)

    # Check if the request to the second API was successful
    if response.status_code == 200:
        print("Data successfully sent to the second API")
    else:
        print(f"Failed to send data to the second API. Status code: {response.status_code}")
else:
    print(f"Failed to fetch data from the first API. Status code: {response.status_code}")

def process_data(data):
    # Implement your data processing logic here
    # For example, extract relevant information from the received data
    processed_data = data.get("key", None)
    return processed_data

def manipulate_data(data):
    # Implement your data manipulation logic here
    # For example, modify the data structure or content
    manipulated_data = {"modified_key": data}
    return manipulated_data
