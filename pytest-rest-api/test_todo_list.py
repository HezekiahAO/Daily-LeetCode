import requests

ENDPOINT = 'https://todo.pixegami.io/'

response = requests.get(ENDPOINT)
print(response)


data = response.json()
print(data)

status_code = response.status_code
print(status_code)





def test_end_piont():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    pass    

def test_ecan_create_task():
    payload = {
        'content' : 'My first task',
        'user_id' : 'User Id',
        "status" : "incomplete"
    }
    response = requests.put(ENDPOINT + '/create-task', json=payload)
    assert response.status_code == 200
    data = response.json()
    print(data)