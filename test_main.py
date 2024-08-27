import pytest
from app import create_app
import json

class TestGeneratePNG():
    base_url = "/generate_png"
    
    @pytest.fixture()
    def client(self):
        yield create_app().test_client()
    def test_example_input(self, client):
        w = "100"
        h = "100"
        response = client.get(f"{self.base_url}?width={w}&height={h}")
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'image/png'
    @pytest.mark.parametrize(
        ("width", "height", "status_code", "expected_content"),
        [
            ("100", "", 400, {"height": "This field is required."}),
            ("100", "100.123", 400, {"height": "This field is required."}),
            ("100", "TEST", 400, {"height": "Should be non-zero integer"}),
            ("100", "-123", 400, {"height": "Number must be between 1 and 10000."}),
            ("100", "0", 400, {"height": "Should be non-zero integer"}),
            ("100", "999999", 400, {"height": "Number must be between 1 and 10000."}),
        ]
    )
    def test_invalid_inputs(self, client, width, height, status_code, expected_content):
        w = "100"
        h = ""
        response = client.get(f"{self.base_url}?width={w}&height={h}")
        assert response.status_code == 400
        assert json.loads(response.get_data(as_text=True)) == {"height": "This field is required."}