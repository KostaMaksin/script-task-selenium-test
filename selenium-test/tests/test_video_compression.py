import os

from pages.home_page import HomePage
from pages.compress_page import CompressPage
from utils.driver_factory import create_driver
from utils.file_utils import (
    ensure_folder_exists,
    clear_folder,
    get_file_size,
    wait_for_new_file,
    wait_until_file_is_stable,
)


DOWNLOAD_DIR = os.path.abspath("downloads")
VIDEO_PATH = os.path.abspath("test_data/file_example_MP4_640_3MG.mp4")


def test_video_compression():
    assert os.path.exists(VIDEO_PATH), f"Video file does not exist: {VIDEO_PATH}"

    ensure_folder_exists(DOWNLOAD_DIR)
    clear_folder(DOWNLOAD_DIR)

    driver = create_driver(DOWNLOAD_DIR)

    try:
        home = HomePage(driver)
        compress = CompressPage(driver)

        # Step 1
        home.open()
        home.close_cookie_popup

        # Step 2
        home.click_compress_videos()
        
        # Step 3
        compress.wait_until_loaded()
        compress.upload_video(VIDEO_PATH)

        # Step 4
        compress.wait_for_compression_to_finish()

        # Step 5 - assert on UI that compressed file is smaller and note reduction
        original_size_text = compress.get_original_size_text()
        output_size_text = compress.get_output_size_text()

        original_size_ui = compress.size_to_bytes(original_size_text)
        output_size_ui = compress.size_to_bytes(output_size_text)

        reduction_bytes = original_size_ui - output_size_ui
        reduction_percent = (reduction_bytes / original_size_ui) * 100

        print("Original UI size:", original_size_text)
        print("Output UI size:", output_size_text)
        print("UI reduction bytes:", reduction_bytes)
        print(f"UI reduction percent: {reduction_percent:.2f}%")

        assert output_size_ui < original_size_ui, (
            f"Expected output size on UI to be smaller. "
            f"Original UI={original_size_text}, Output UI={output_size_text}"
        )

        # Step 6
        existing_files = set(os.listdir(DOWNLOAD_DIR))
        compress.download_video()

        # Step 7
        downloaded_file = wait_for_new_file(DOWNLOAD_DIR, existing_files, timeout=180)
        wait_until_file_is_stable(downloaded_file, timeout=60)

        # Step 8
        original_size = get_file_size(VIDEO_PATH)
        downloaded_size = get_file_size(downloaded_file)

        print("Original file:", VIDEO_PATH)
        print("Downloaded file:", downloaded_file)
        print("Original size bytes:", original_size)
        print("Downloaded size bytes:", downloaded_size)

        assert downloaded_size < original_size, (
            f"Expected compressed file to be smaller. "
            f"Original={original_size}, Downloaded={downloaded_size}"
        )

    finally:
        driver.quit()