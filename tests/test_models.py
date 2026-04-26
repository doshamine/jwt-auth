import pytest
from django.db import DataError, IntegrityError
from model_bakery import baker

from user_auth.models import Permission


@pytest.mark.django_db
def test_create_permission():
    prepared_permission = Permission(name="test", description="test description")

    prepared_permission.save()
    saved_permission = Permission.objects.all().first()

    assert prepared_permission == saved_permission


@pytest.mark.django_db
def test_create_permission_large_length_error():
    permission = Permission(name="test" * 100, description="test description")

    with pytest.raises(DataError):
        permission.save()


@pytest.mark.django_db
def test_create_permission_duplicate_error():
    permission1 = Permission(name="test", description="test description")
    permission1.save()
    permission2 = Permission(name="test", description="description")

    with pytest.raises(IntegrityError):
        permission2.save()


@pytest.mark.django_db
def test_create_permission_null_error():
    permission = Permission(name=None, description="test description")

    with pytest.raises(IntegrityError):
        permission.save()