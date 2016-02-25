# -*- coding: utf-8 -*-
import pytest
from .utils import get, versioned_reverse as reverse, assert_fields_exist


# === util methods ===

def get_list(api_client, version='v1'):
    list_url = reverse('user-list', version=version)
    return get(api_client, list_url)

def assert_user_fields_exist(data, version='v1'):
    # TODO: incorporate version parameter into version aware
    # parts of test code
    fields = (
        'last_login',
        'username',
        'email',
        'date_joined',
        'first_name',
        'last_name',
        'uuid',
        'department_name',
        'organization',
        'is_staff',
        'display_name',
    )
    assert_fields_exist(data, fields)

# === tests ===

@pytest.mark.django_db
def test__get_user_list(api_client, user, organization):
    organization.admin_users.add(user)
    api_client.force_authenticate(user=user)
    response = get_list(api_client)
    print(response.data)
    assert_user_fields_exist(response.data['data'][0])
