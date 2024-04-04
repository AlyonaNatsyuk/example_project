from ..pages.login_page import LoginPageApi
import pytest


class TestLoginPage:
    @pytest.mark.login
    def test_registration_with_valid_data(self):
        page = LoginPageApi()
        page.registration_with_valid_data('First name', 'Last name',
                                          'alyona.natsyuk@requestum.com', 'FirstName2022!')

    def test_check_resend_email_valid_verification_email(self):
        page = LoginPageApi()
        page.check_resend_email_valid_verification_email('First name', 'Last name',
                                                         'alyona.natsyuk+647@requestum.com',
                                                         'FirstName2022!')

    def test_check_resend_email_valid_change_email(self):
        page = LoginPageApi()
        page.check_resend_email_valid_change_email('First name', 'Last name',
                                                   'alyona.natsyuk+654@requestum.com',
                                                   'FirstName2022!',
                                                   'alyona.natsyuk+354@requestum.com')

    def test_check_resend_email_invalid_verification_email(self):
        page = LoginPageApi()
        page.check_resend_email_invalid_verification_email()

    def test_check_resend_email_invalid_change_email(self):
        page = LoginPageApi()
        page.check_resend_email_invalid_change_email()

    def test_check_email_valid(self):
        page = LoginPageApi()
        page.check_email_valid('alyona.natsyuk+userqa1@requestum.com')


@pytest.mark.parametrize('email', ['alyona.natsyuk', '@requestum.com', 'alallaarequestum.com',
                                   'alallaare@questum', 'alyona.natsyuk+100@requestum.com'])
def test_check_email_invalid(email):
    page = LoginPageApi()
    page.check_email_invalid(f'{email}')


@pytest.mark.parametrize('f_name, l_name, email, plain_password', [('First name', 'Last name', 'alyona.natsyuk',
                                                                    'FirstName2022!'),
                                                            ('First name', 'Last name', '@requestum.com',
                                                             'FirstName2022!*'),
                                                            ('First name', 'Last name', 'alallaarequestum.com',
                                                             'FirstName2022!'),
                                                            ('First name', 'Last name', 'alallaare@questum',
                                                             'FirstName2022!'),
                                                            ('First name', 'Last name',
                                                             'alyona.natsyuk+1@requestum.com', 'FirstName2022'),
                                                            ('First name', 'Last name',
                                                             'alyona.natsyuk+1@requestum.com', '*firstname2022!'),
                                                            ('First name', 'Last name',
                                                             'alyona.natsyuk+1@requestum.com', '2022'),
                                                            ('First name', 'Last name',
                                                             'alyona.natsyuk+1@requestum.com', 'Test*****'),
                                                            ('First name', 'Last name',
                                                             'alyona.natsyuk@requestum.com', 'FirstName2022!')])
def test_registration_with_invalid_data(f_name, l_name, email, plain_password):
    page = LoginPageApi()
    page.registration_with_invalid_data(f'{f_name}', f'{l_name}', f'{email}',
                                        f'{plain_password}')


