import os

import pytest

from pages.upload_Image_page import UploadImgPage


@pytest.mark.parametrize("file", ['photo.png'])
def test_upload(browser, config_reader, file):
    url = config_reader.get_value("url_11")
    browser.get(url)

    upload_img = UploadImgPage(browser)
    upload_img.wait_for_open()
    relative_path = f"photo/{file}"
    upload_img.upload_file(os.path.abspath(relative_path))
    upload_img.click_upload()

    title_name = upload_img.get_text_title()
    assert title_name == "File Uploaded!", f"Expected result: {title_name} corrected" \
                                           f"Actual result:{title_name} Title not corrected"

    file_name = upload_img.get_text_name()
    assert file_name == file, f"Expected result:{file_name} message appeared" \
                              f"Actual result:{file_name} File name not corrected"
