import pytest
from model_bakery import baker


@pytest.fixture
def role():
    return baker.make("user_auth.Role", _fill_optional=True)


@pytest.fixture
def permission():
    return baker.make("user_auth.Permission", _fill_optional=True)


@pytest.fixture
def user():
    return baker.make("user_auth.User", _fill_optional=True)


@pytest.fixture
def refresh_token():
    return baker.make("user_auth.RefreshToken", _fill_optional=True)