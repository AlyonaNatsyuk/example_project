from ..pages.upload import UploadPage


class TestBindPage:
    def test_small_upload(self):
        page = UploadPage()
        page.upload('../media/video.MP4')#<1mb

    def test_upload_big_video(self):
        page = UploadPage()
        page.upload_wrong_big_video('../media/movie.mp4')#39,5

    def test_upload_pdf(self):
        page = UploadPage()
        page.upload_wrong_file('../media/Test.pdf')

    def test_upload_jpg(self):
        page = UploadPage()
        page.upload_jpg('../media/horse.jpg')
