import pytest

from user_auth.models import Permission


@pytest.mark.django_db
def test_create_permission():
    prepared_permission = Permission(name="test", description="test description")

    prepared_permission.save()
    saved_permission = Permission.objects.all().first()

    assert prepared_permission == saved_permission