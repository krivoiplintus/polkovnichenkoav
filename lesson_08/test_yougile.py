import requests

url = "https://ru.yougile.com"


def get_project_list():
    token =
    my_headers = {
        'Authorization': 'Bearer ' + token
    }
    resp = requests.get(url + '/api-v2/projects', headers=my_headers)
    result = resp.json()
    return result


def get_project_id():
    project_id = test_create_prodject()
    token =
    my_headers = {
        'Authorization': 'Bearer ' + token
    }
    resp = requests.get(url + '/api-v2/projects/' + project_id, headers=my_headers)
    result = resp.json()
    return result


def test_create_prodject():
    token =
    my_headers = {
        'Authorization': 'Bearer ' + token
    }
    body = {
        "title": "Новый проект",
        "users": {
            "ccf62539-83bc-4859-9ae2-aeb0cbebc461": "admin"
        }
    }
    resp = requests.post(url + '/api-v2/projects', headers=my_headers, json=body)
    result = resp.json()
    list_project = get_project_list()
    assert len(result) != 0
    assert resp.status_code == 201
    assert result["id"] == list_project["content"][-1]["id"]
    return result["id"]


def test_create_prodject_neg():
    token =
    my_headers = {
        'Authorization': 'Bearer ' + token
    }
    body = {
        "title": "",
        "users": {
            "ccf62539-83bc-4859-9ae2-aeb0cbebc461": "admin"
        }
    }
    resp = requests.post(url + '/api-v2/projects', headers=my_headers, json=body)
    result = resp.json()
    assert result["message"] == ["title should not be empty"]
    assert resp.status_code == 400


def test_get_projects():
    token =
    my_headers = {
        'Authorization': 'Bearer ' + token
    }
    resp = requests.get(url + '/api-v2/projects', headers=my_headers)
    result = resp.json()
    assert len(result) != 0
    assert resp.status_code == 200


def test_get_project_id():
    project_id = test_create_prodject()
    token =
    my_headers = {
        'Authorization': 'Bearer ' + token
    }
    resp = requests.get(url + '/api-v2/projects/' + project_id, headers=my_headers)
    result = resp.json()
    assert len(result) != 0
    assert resp.status_code == 200


def test_rename_project():
    project_id = test_create_prodject()
    token =
    my_headers = {
        'Authorization': 'Bearer ' + token
    }
    my_body = {
        "title": "Изменённый проект",
    }
    resp = requests.put(url + '/api-v2/projects/' + project_id, headers=my_headers, json=my_body)
    result = resp.json()
    assert result != 0
    assert resp.status_code == 200


def test_rename_project_neg():
    project_id = test_create_prodject()
    token =
    my_headers = {
        'Authorization': 'Bearer ' + token
    }
    my_body = {
        "title": "",
    }
    resp = requests.put(url + '/api-v2/projects/' + project_id, headers=my_headers, json=my_body)
    result = resp.json()
    assert result["message"] == ["title should not be empty"]
    assert resp.status_code == 400
