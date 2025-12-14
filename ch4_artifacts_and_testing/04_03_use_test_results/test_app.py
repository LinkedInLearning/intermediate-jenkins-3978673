"""A module for testing"""

import unittest

from app import APP, MASCOTS


class Tests(unittest.TestCase):
    """Basic tests for the application"""

    def setUp(self):
        """Create a test client for the app"""
        self.app = APP.test_client()

    def test_for_http_code_200(self):
        """test_for_http_code_200: a request for / shall return 200 OK"""
        res = self.app.get("/")
        assert res.status == "200 OK"

    def test_root_returns_json_array(self):
        """test_root_json: root endpoint returns a JSON array"""
        res = self.app.get("/")
        data = res.get_json()
        assert isinstance(data, list)
        assert len(data) > 0

    def test_root_returns_all_mascots(self):
        """test_root_all_mascots: root endpoint returns all mascots from data"""
        res = self.app.get("/")
        data = res.get_json()
        assert len(data) == len(MASCOTS)

    def test_root_mascot_structure(self):
        """test_root_structure: each mascot in root has required fields"""
        res = self.app.get("/")
        data = res.get_json()
        required_fields = ["guid", "school", "nickname", "location"]
        for mascot in data:
            for field in required_fields:
                assert field in mascot, f"Missing required field: {field}"

    def test_for_http_code_404(self):
        """test_for_http_code_404: a request for null shall return 404 NOT FOUND"""
        res = self.app.get("/null")
        assert res.status == "404 NOT FOUND"

    def test_404_error_response_format(self):
        """test_404_format: 404 response includes error in JSON format"""
        res = self.app.get("/invalid-guid-12345")
        assert res.status == "404 NOT FOUND"
        data = res.get_json()
        assert "error" in data

    def test_invalid_guid_formats(self):
        """test_invalid_guids: various invalid GUID formats return 404"""
        invalid_guids = [
            "not-a-guid",
            "12345",
            "invalid-guid-format",
            "00000000-0000-0000-0000-000000000000",  # Valid format but not in data
        ]
        for guid in invalid_guids:
            res = self.app.get(f"/{guid}")
            assert res.status == "404 NOT FOUND", f"Expected 404 for GUID: {guid}"

    def test_all_guids_accessible(self):
        """test_all_guids: all GUIDs from data.json are accessible"""
        for mascot in MASCOTS:
            guid = mascot["guid"]
            res = self.app.get(f"/{guid}")
            assert res.status == "200 OK", f"GUID {guid} should be accessible"
            data = res.get_json()
            assert data["guid"] == guid
