import os
import tempfile

from google.cloud import storage
from PIL import Image, ImageFilter


def blur_image(blob: storage.Blob | None, filename: str) -> str | None:
    local_temp_filename = None

    if blob:
        _, extension = filename.split(".")
        local_temp_filename = tempfile.mkstemp(suffix=f".{extension}")

        blob.download_to_filename(local_temp_filename)
        print(f"Image {filename} was downloaded to {local_temp_filename}")

        image = Image.open(local_temp_filename)
        blur_image = image.filter(ImageFilter.GaussianBlur(16))
        blur_image.save(local_temp_filename)

        print(f"Image {filename} was blurred")

    return local_temp_filename


def remove_tmp_image(filename):
    return os.remove(filename)
