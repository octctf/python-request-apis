import requests

# Define the URL of the API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Define the data to be sent in the request
payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1,
    "token": test
}

# Make the POST request
response = requests.post(url, json=payload)

# Check status code of the request
if response.status_code == 201:  # 201 is the status code for a successful POST request (resource created)
    # Print the JSON response
    data = response.json()
    print("Response JSON:")
    print(data)
else:
    print(f"Failed to post data: {response.status_code}")
