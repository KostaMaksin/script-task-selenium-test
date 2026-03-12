import os
import time
from typing import Optional


def ensure_folder_exists(folder_path: str) -> None:
    os.makedirs(folder_path, exist_ok=True)


def clear_folder(folder_path: str) -> None:
    ensure_folder_exists(folder_path)

    for name in os.listdir(folder_path):
        path = os.path.join(folder_path, name)
        if os.path.isfile(path):
            os.remove(path)


def get_file_size(file_path: str) -> int:
    return os.path.getsize(file_path)


def wait_for_new_file(
    folder_path: str,
    existing_files: set[str],
    timeout: int = 120
) -> str:
    end_time = time.time() + timeout
    allowed_extensions = (".mp4", ".mov", ".avi", ".m4v")

    while time.time() < end_time:
        current_files = set(os.listdir(folder_path))
        new_files = current_files - existing_files

        completed_files = [
            f for f in new_files
            if not f.startswith(".")
            and not f.endswith(".crdownload")
            and not f.endswith(".tmp")
            and f.lower().endswith(allowed_extensions)
        ]

        if completed_files:
            newest = max(
                completed_files,
                key=lambda f: os.path.getmtime(os.path.join(folder_path, f))
            )
            print("Detected completed download:", newest)
            return os.path.join(folder_path, newest)

        time.sleep(1)

    raise TimeoutError("No completed downloaded video file was detected within timeout.")


def wait_until_file_is_stable(
    file_path: str,
    timeout: int = 60,
    poll_interval: float = 1.0
) -> None:
    end_time = time.time() + timeout
    previous_size: Optional[int] = None

    while time.time() < end_time:
        if not os.path.exists(file_path):
            time.sleep(poll_interval)
            continue

        current_size = os.path.getsize(file_path)

        if previous_size is not None and current_size == previous_size:
            return

        previous_size = current_size
        time.sleep(poll_interval)

    raise TimeoutError("Downloaded file size did not stabilize within timeout.")