from distutils.command.upload import upload
from unittest.mock import MagicMock, patch

from main import blur_images


@patch("main.Storage")
@patch("main.image.remove_tmp_image")
@patch("main.image.blur_image")
def test_blur_images(blur_image_mock, remove_tmp_image_mock, StorageMock, capsys):
    original_filename = "original-image.png"
    blurred_filename = "blurred-original-image.png"
    bucketname = "mock_bucket"
    data = dict(name=original_filename, bucket=bucketname)
    context = dict()

    storage_mock_instance = StorageMock.return_value
    storage_mock_instance.get_blob.return_value = MagicMock()
    storage_mock_instance.upload.return_value = MagicMock()

    blur_image_mock.return_value = blurred_filename

    blur_images(data, context)
    out, _ = capsys.readouterr()

    assert storage_mock_instance.get_blob.called
    assert storage_mock_instance.upload.called
    assert blur_image_mock.called
    assert remove_tmp_image_mock.called
    assert f"Blurring image {original_filename}..." in out
    assert (
        f"Blurred image uploaded to gs://{bucketname}/{blurred_filename}" in out
    )
