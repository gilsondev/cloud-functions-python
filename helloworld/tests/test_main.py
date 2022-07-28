from main import hello_http


def test_hello_http(app, app_request):
    with app.test_request_context():
        resp = hello_http(app_request)
        assert "Hello World! Welcome!" in resp
