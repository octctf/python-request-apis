import requests

# Define the URL of the API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

# Make the GET request
response = requests.get(url)

# Check status code of the request
if response.status_code == 200:
    # Print the JSON response
    data = response.json()
    print("Response JSON:")
    print(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")
