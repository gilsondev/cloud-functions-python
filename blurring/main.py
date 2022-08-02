from utils import image
from utils.storage import Storage


def blur_images(data, context):
    filename = data["name"]
    bucket_name = data["bucket"]
    blurred_filename = f"blurred-{filename}"

    storage = Storage(bucket_name)
    blob = storage.get_blob(filename)

    print(f"Blurring image {filename}...")
    tmp_filename = image.blur_image(blob, filename)

    storage.upload(blurred_filename, tmp_filename)
    print(f"Blurred image uploaded to gs://{bucket_name}/{blurred_filename}")

    image.remove_tmp_image(tmp_filename)
