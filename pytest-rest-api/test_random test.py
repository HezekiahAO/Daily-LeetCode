import requests 

End = 'https://jsonplaceholder.typicode.com/posts'
                                                        # JavaScript Object Notation.
response = requests.get(End)
print(response)

data = response.json()   # The API response with a JSON format which is not a Python dictiionary but canbe converted to one using the json() method
print(data)
status_code = response.status_code
print(status_code)

def test_endpoint_status():
    response = requests.get(End)
    assert response.status_code == 200

def test_can_create_post():
    payload = {
       'title': 'foo',
        'body': 'bar',
        'userId': 2
    }