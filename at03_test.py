from at03 import get_cat


def test_get_cat_success(mocker):
    mock_get = mocker.patch('at03.requests.get')
   # Create mock-answer for success request
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {'id': 'iY76694gN', 'url': 'https://cdn2.thecatapi.com/images/iY76694gN.jpg',
          'width': 1600, 'height': 1200}
    ]

    cat_image = get_cat()
    assert cat_image == [{'id': 'iY76694gN',
                          'url': 'https://cdn2.thecatapi.com/images/iY76694gN.jpg',
                          'width': 1600, 'height': 1200}]


def test_get_cat_error(mocker):
    mock_get = mocker.patch('at03.requests.get')
    mock_get.return_value.status_code = 404

    cat_image = get_cat()
    assert cat_image is None
