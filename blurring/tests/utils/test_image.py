from collections import UserDict
from unittest.mock import MagicMock, patch

from utils import image


@patch("utils.image.Image")
def test_blur_image(ImageMock):

    mock_blob = MagicMock()
    mock_blob.download_to_filename = MagicMock()

    mock_blurred_image = UserDict()
    mock_blurred_image.save = MagicMock()

    mock_image = UserDict()
    mock_image.filter = MagicMock(return_value=mock_blurred_image)

    ImageMock.open = MagicMock(return_value=mock_image)

    image.blur_image(mock_blob, "original-image.png")

    assert ImageMock.open.called


@patch("utils.image.os")
def test_remove_tmp_image(os_mock):
    image.remove_tmp_image("mock_image.png")

    assert os_mock.remove.called
