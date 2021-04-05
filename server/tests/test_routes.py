"""Tests for the flask routes."""

import os
from unittest import TestCase, mock
from flask import current_app
import app
class TestRoutes(TestCase):
    """Test Suite for the HeroFight flask app."""

    def setUp(self):
        """Creates test fixture."""
        self.test_app = app.create_app()
        self.test_ctx = self.test_app.app_context()
        self.test_ctx.push()

    def tearDown(self):
        """Deletes test fixture."""
        self.test_ctx.pop()

    def test_hello(self):
        """Tests /api/hello endpoint."""
        url = '/api/hello'
        with current_app.test_client() as client:
            resp = client.get(url)
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.get_data(as_text=True), 'hello')