from .base_page import BasePage


class LoginPageApi(BasePage):

    def registration_with_valid_data(self, first_name, last_name, email, plain_password):
        obj = self.regist_oath(first_name, last_name, email, plain_password)
        assert obj.status_code == 201, f'Status is {obj.status_code}. Problem:{obj.text}'

    def registration_with_invalid_data(self, first_name, last_name, email, plain_password):
        obj = self.regist_oath(first_name, last_name, email, plain_password)
        assert obj.status_code == 422, f'Status is {obj.status_code}. Problem:{obj.text}'

    def check_resend_email_valid_verification_email(self, first_name, last_name, email, plain_password):
        self.regist_oath(first_name, last_name, email, plain_password)
        token = self.get_oath_token_user(email, plain_password)
        obj = self.resend_email('verification_email', token)
        assert obj.status_code == 200, f'Status is {obj.status_code}'

    def check_resend_email_invalid_verification_email(self):
        obj = self.resend_email('verification_email')
        assert obj.status_code == 404, f'Status is {obj.status_code}'

    def check_resend_email_valid_change_email(self, first_name, last_name, email, plain_password, new_email):
        self.regist_oath(first_name, last_name, email, plain_password)
        token = self.get_oath_token_user(email, plain_password)
        id_user = self.check_email(email).json()['id']
        self.change_email(id_user, new_email, plain_password, token)
        token = self.get_oath_token_user(email, plain_password)
        obj = self.resend_email('change_email', token)
        assert obj.status_code == 200, f'Status is {obj.status_code} and {obj.text}'

    def check_resend_email_invalid_change_email(self):
        obj = self.resend_email('change_email')
        assert obj.status_code == 404, f'Status is {obj.status_code}'

    def check_email_valid(self, email):
        obj = self.check_email(email).status_code
        assert obj == 200, f'Status is {obj}. User not registered yet'

    def check_email_invalid(self, email):
        obj = self.check_email(email).status_code
        assert obj == 404, f'Status is {obj}.'



