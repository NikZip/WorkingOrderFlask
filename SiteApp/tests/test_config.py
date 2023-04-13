import os
import pytest
from SiteApp import create_app
from SiteApp.config import ProductionConfig, DevelopmentConfig, TestingConfig


class TestConfig:

    @pytest.fixture
    def env_params(self):
        return os.environ

    def test_if_env_is_exist(self, env_params):
        """
        Testing: Is env file exist
        Expected: not None
        """
        assert env_params is not None

    def test_if_env_data_is_set(self, env_params):
        """
        Testing: if environment params are set
        Expected: Parameters are set and not None
        """
        assert env_params.get('SECRET_KEY') is not None
        assert env_params.get('DATABASE_ENGINE') is not None
        assert env_params.get('DATABASE_USER') is not None
        assert env_params.get('DATABASE_PASS') is not None
        assert env_params.get('DATABASE_HOST') is not None
        assert env_params.get('DATABASE_PORT') is not None
        assert env_params.get('DATABASE_NAME') is not None

    def test_prod_app_config(self):
        """
        Testing: Correct production config
        Expected: Debug param is False
        """
        app = create_app(ProductionConfig)
        assert app.config['DEBUG'] is not True

    def test_dev_app_config(self):
        """
        Testing: Correct dev config
        Expected: Debug param is True
        """
        app = create_app(DevelopmentConfig)
        assert app.config['DEBUG'] is True

    def test_testing_app_config(self):
        """
        Testing: Correct test config
        Expected: Testing param is true and testing database is not same as in Prod config
        """
        app = create_app(TestingConfig)
        assert app.config['TESTING'] is True
        assert app.config['SQLALCHEMY_DATABASE_URI'] is not ProductionConfig.SQLALCHEMY_DATABASE_URI
