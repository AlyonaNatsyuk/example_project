import requests


class BasePage:
    api_url = 'https://some_url'

    # end-point for Oath
    def get_oath_token_user(self, email='alyona.natsyuk+userqa1@mail.com', password='userQa1!'):
        r = requests.post(url=f'{self.api_url}/oauth/token',
                          headers={'Content-Type': 'application/x-www-form-urlencoded'},
                          data={
                              'grant_type': 'test',
                              'client_id': 'test',
                              'client_secret': 'test',
                              'username': email,
                              'password': password})
        token = r.json()['access_token']
        return token

    def get_oath_token_anonim(self):
        r = requests.post(url=f'{self.api_url}/oauth/token',
                          headers={'Content-Type': 'application/x-www-form-urlencoded'},
                          data={
                              'grant_type': 'test',
                              'client_id': 'test',
                              'client_secret': 'test'})
        token = r.json()['access_token']
        return token

    def regist_oath(self, first_name, last_name, email, plain_password):
        header = self.get_oath_token_anonim()
        r = requests.post(f'{self.api_url}/api/users/registration', headers={'Authorization': f'Bearer {header}'},
                          json={'firstName': first_name,
                                'lastName': last_name,
                                'email': email,
                                'plainPassword': plain_password})
        return r

    def change_email(self, id_user, new_email, password, token=None):
        token = self.get_oath_token_user() if token is None else token
        requests.patch(f'{self.api_url}/api/users/{id_user}/change-email',
                       headers={'Authorization': f'Bearer {token}',
                                'Content-type': 'application/merge-patch+json'},
                       json={'email': new_email,
                             'password': password})

    def resend_email(self, type, token=None):
        token = self.get_oath_token_user() if token is None else token
        r = requests.get(f'{self.api_url}/api/users/resend/{type}',
                         headers={'Authorization': f'Bearer {token}'})
        return r

    def check_email(self, email, token=None):
        token = self.get_oath_token_user() if token is None else token
        r = requests.get(f'{self.api_url}/api/users/email/{email}',
                         headers={'Authorization': f'Bearer {token}',
                                  'Accept': 'application/ld+json'})
        return r

    def upload_file(self, upl_file, token=None):
        token = self.get_oath_token_user() if token is None else token
        files = {'document': open(f'{upl_file}', 'rb')}
        url_file = requests.post(f'{self.api_url}/api/files/upload',
                                 headers={'Authorization': f'Bearer {token}'},
                                 files=files)
        return url_file
