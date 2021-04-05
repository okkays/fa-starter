"""Tests for the flask app."""

import os
from dotenv import load_dotenv
from unittest import TestCase
from flask import current_app
import app

class TestApp(TestCase):
    """Test Suite for the HeroFight flask app."""
    def test_create_app(self):
        """Tests that prod app is created with correct settings."""
        self.assertTrue(load_dotenv('.flaskenv'))
        self.test_app = app.create_app('app.config.ProdConfig')
        self.test_ctx = self.test_app.app_context()
        self.test_ctx.push()
        self.assertIsNotNone(current_app)
        self.assertNotEqual(current_app.config['SECRET_KEY'], "my_dev_session_key")
        self.assertEqual(
            current_app.config['EXAMPLEVAR'],
            'secret_value_like_external_api_key')
        self.test_ctx.pop()

    def test_create_app_dev(self):
        """Tests that dev app is created with correct settings."""
        load_dotenv('.flaskenv')
        self.test_app = app.create_app(config='app.config.DevConfig')
        self.test_ctx = self.test_app.app_context()
        self.test_ctx.push()
        self.assertIsNotNone(current_app)
        self.assertEqual(current_app.config['SECRET_KEY'], "my_dev_session_key")
        self.assertEqual(
            current_app.config['EXAMPLEVAR'], 
            'secret_value_like_external_api_key')
        self.test_ctx.pop()