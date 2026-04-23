import pytest
from model_bakery import baker


@pytest.fixture
def role():
    return baker.make("user_auth.Role", _fill_optional=True)
