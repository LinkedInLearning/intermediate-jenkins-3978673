"""A module for testing"""

import unittest

from app import APP


class CyclonesTests(unittest.TestCase):
    """Tests for the Cyclones"""

    def setUp(self):
        """Create a test client for the app"""
        self.app = APP.test_client()

    def test_guid(self):
        """test_guid: a request for the guid shall return 200 OK"""
        res = self.app.get("/05024756-765e-41a9-89d7-1407436d9a58")
        assert res.status == "200 OK"

    def test_json(self):
        """test_json: a request for the guid shall return the defined JSON"""
        res = self.app.get("/05024756-765e-41a9-89d7-1407436d9a58")
        assert res.json == {
            "guid": "05024756-765e-41a9-89d7-1407436d9a58",
            "latlong": "42.026111,-93.648333",
            "location": "Ames, IA, USA",
            "mascot": "Cy",
            "nickname": "Cyclones",
            "school": "Iowa State University",
        }

    def test_response_content_type(self):
        """test_content_type: response has correct Content-Type header"""
        res = self.app.get("/05024756-765e-41a9-89d7-1407436d9a58")
        assert res.content_type == "application/json"

    def test_mascot_without_latlong(self):
        """test_no_latlong: mascot without latlong field still returns successfully"""
        # Baylor University doesn't have latlong in data.json
        res = self.app.get("/27a85510-1ccd-4e44-81bd-92b5ba0ae402")
        assert res.status == "200 OK"
        data = res.get_json()
        assert "guid" in data
        assert "school" in data
        # latlong may or may not be present
        assert "location" in data


class AdditionalMascotTests(unittest.TestCase):
    """Tests for additional mascots from data.json"""

    def setUp(self):
        """Create a test client for the app"""
        self.app = APP.test_client()

    def test_jayhawks(self):
        """test_jayhawks: test University of Kansas mascot"""
        res = self.app.get("/9623f598-ca93-4d4e-bbb7-3e18320a923a")
        assert res.status == "200 OK"
        data = res.get_json()
        assert data["school"] == "University of Kansas"
        assert data["nickname"] == "Jayhawks"

    def test_longhorns(self):
        """test_longhorns: test University of Texas mascot"""
        res = self.app.get("/f6e17d21-1616-44ff-9655-8f12296abdd8")
        assert res.status == "200 OK"
        data = res.get_json()
        assert data["school"] == "University of Texas at Austin"
        assert data["nickname"] == "Longhorns"

    def test_mountaineers(self):
        """test_mountaineers: test West Virginia University mascot"""
        res = self.app.get("/bf98a44c-e26f-47ae-8f94-1a1b61a9c414")
        assert res.status == "200 OK"
        data = res.get_json()
        assert data["school"] == "West Virginia University"
        assert data["nickname"] == "Mountaineers"
        assert "latlong" in data  # This one has latlong
