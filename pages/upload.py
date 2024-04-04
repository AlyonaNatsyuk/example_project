from .base_page import BasePage


class UploadPage(BasePage):
    def upload(self, file):
        status = self.upload_file(file).status_code
        assert status == 200, f'Status is {status}.'

    def upload_wrong_big_video(self, file):
        status = self.upload_file(file).status_code
        assert status == 413, f'Status is {status}.'

    def upload_wrong_file(self, file):
        status = self.upload_file(file).status_code
        assert status == 422, f'Status is {status}.'

    def upload_jpg(self, file):
        status = self.upload_file(file).status_code
        assert status == 200, f'Status is {status}.'
