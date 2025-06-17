import os

import pytest

from utils.dialog_utils import DialogWindowUtils
from pages.upload_dialog_page import UploadImgDialogPage


@pytest.mark.parametrize("file", ['photo.png'])
def test_upload_gialog(browser, config_reader, file):
    url = config_reader.get_value("url_11")
    browser.get(url)
    upload_img_dialog = UploadImgDialogPage(browser)
    upload_img_dialog.wait_for_open()
    upload_img_dialog.click_on_upload_section()

    relative_path = f"photo/{file}"
    DialogWindowUtils.write_and_enter(os.path.abspath(relative_path))
    file_name = upload_img_dialog.get_text_name()
    assert file_name == file, \
        f"Expected result:{file_name} message appeared" \
        f"Actual result:{file_name} File name not corrected"
    assert upload_img_dialog.get_check_mark(), f"Expected result: There is check mark" \
                                               f"Actual result: There is not check mark"
