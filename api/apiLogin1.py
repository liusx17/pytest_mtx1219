from flask import session

from setting import IP, HEADERS

class ApiLogin():
    def __init__(self):
        self.url = IP + '/mtx/index.php?s=/index/user/login.html'

    def login(self, session, data):
        resp_login = session.post(self.url, data=data, headers=HEADERS)
        return resp_login

    def login_success(self):
        data = {'accounts': 'liushengxian1', 'pwd': 'liushengxian1'}
        resp_login = session.post(self.url, data=data, headers=HEADERS)
        return resp_login

