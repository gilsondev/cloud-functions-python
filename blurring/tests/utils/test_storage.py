from collections import UserDict
from unittest.mock import MagicMock, patch

from utils.storage import Storage


@patch("utils.storage.storage")
def test_get_blob(gcs_storage_mock):

    mock_blob = UserDict()
    mock_blob.name = "image.png"

    mock_bucket = MagicMock()
    mock_bucket.get_blob = MagicMock(return_value=mock_blob)

    mock_storage_client = MagicMock()
    mock_storage_client.bucket = MagicMock(return_value=mock_bucket)
    gcs_storage_mock.Client = MagicMock(return_value=mock_storage_client)

    storage_instance = Storage(bucket_name="mocked_bucket")
    result = storage_instance.get_blob("fake_file.png")

    assert result is not None
    assert gcs_storage_mock.Client.called
    assert mock_storage_client.bucket.called
    assert mock_bucket.get_blob.called


@patch("utils.storage.storage")
def test_upload(gcs_storage_mock):
    mock_blob = UserDict()
    mock_blob.name = "image.png"
    mock_blob.upload_from_filename = MagicMock()

    mock_bucket = MagicMock()
    mock_bucket.blob = MagicMock(return_value=mock_blob)

    mock_storage_client = MagicMock()
    mock_storage_client.bucket = MagicMock(return_value=mock_bucket)
    gcs_storage_mock.Client = MagicMock(return_value=mock_storage_client)

    storage_instance = Storage(bucket_name="mocked_bucket")
    storage_instance.upload(mock_blob.name, "temp-image.png")

    assert gcs_storage_mock.Client.called
    assert mock_bucket.blob.called
    assert mock_blob.upload_from_filename.called
