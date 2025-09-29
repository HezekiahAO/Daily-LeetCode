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

def test_can_create_task():
    payload = {
        'content' : 'My first task',
        'user_id' : 'User Id',
        "status" : "incomplete"
    }
    create_task_response = requests.put(ENDPOINT + '/create-task', json=payload)
    assert create_task_response.status_code == 200
    data_1 = create_task_response.json()
    print(data_1)


