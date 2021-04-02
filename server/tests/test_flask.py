"""Tests for the flask app."""

import os
from unittest import TestCase
from flask import current_app
import app

class TestApp(TestCase):
    """Test Suite for the HeroFight flask app."""
    """
    def setUp(self):
        Creates test fixture.""
        self.test_app = app.create_app()
        self.test_ctx = self.test_app.app_context()
        self.test_ctx.push()

    def tearDown(self):
        ""Deletes test fixture.""
        self.test_ctx.pop()
    """
    def test_create_app(self):
        """Tests that prod app is created with correct settings."""
        self.test_app = app.create_app()
        self.test_ctx = self.test_app.app_context()
        self.test_ctx.push()
        self.assertIsNotNone(current_app)
        self.assertEqual(current_app.config['ENV'], "production")
        self.assertFalse(current_app.config['DEBUG'])
        self.assertFalse(current_app.config['TESTING'])
        self.assertEqual(
            current_app.config['EXAMPLEVAR'],
            'secret_value_like_external_api_key')
        self.test_ctx.pop()

    def test_create_app_dev(self):
        """Tests that dev app is created with correct settings."""
        self.test_app = app.create_app(config='app.config.DevConfig')
        self.test_ctx = self.test_app.app_context()
        self.test_ctx.push()
        self.assertIsNotNone(current_app)
        self.assertEqual(current_app.config['ENV'], "development")
        self.assertTrue(current_app.config['DEBUG'])
        self.assertTrue(current_app.config['TESTING'])
        self.assertEqual(
            current_app.config['EXAMPLEVAR'], 
            'secret_value_like_external_api_key')
        self.test_ctx.pop()