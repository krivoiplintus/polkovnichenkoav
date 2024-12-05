import requests

class PageCompany():

    def __init__(self, url):
        self.url = url

    def get_id_company(self, login="pugacevartem@gmail.com", password="Qwerty12", name="SkyEng"):
        my_data = {
            "login": login,
            "password": password,
            "name": name
        }
        resp = requests.post(self.url + '/api-v2/auth/companies', json=my_data)
        id_company = resp.json()['id']
        return id_company
    def ayth(self):
        id = get_id_company()
        my_id_and_data = {
            "login": "pugacevartem@gmail.com",
            "password": "Qwerty12",
            "id": id
        }
        resp = requests.post(self.url + '/api-v2/auth/keys', json=my_id_and_data)
        token = resp.json()['key']
        return token

def get_id_company(login="pugacevartem@gmail.com", password="Qwerty12", name="SkyEng"):
    my_data = {
        "login": login,
        "password": password,
        "name": name
    }
    resp = requests.post(url + '/api-v2/auth/companies', json=my_data)
    id_company = resp.json()["content"][0]['id']
    return id_company

def ayth():
    id_company = get_id_company()
    my_id_and_data = {
        "login": "pugacevartem@gmail.com",
        "password": "Qwerty12",
        "companyId": id_company
    }
    resp = requests.post(url + '/api-v2/auth/keys', json=my_id_and_data)
    token = resp.json()["key"]
    return token