import imghdr

import requests
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()

API_BASE = 'https://graph.facebook.com/v3.2'
API_ME = f'{API_BASE}/me'


def get_user_info_with_access_token(access_token):
    """
    front/ios에서 받은 access_token으로 facebook에 사용자 상세정보를 요청하여 database에 저장한 후
    user 인스턴스를 돌려줌
    :param access_token:
    :return: user
    """
    params = {
        'access_token': access_token,
        'fields': ', '.join([
            'id',
            'first_name',
            'last_name',
            'picture.type(large)',
        ])
    }
    response = requests.get(API_ME, params)
    data = response.json()

    facebook_id = data['id']
    first_name = data['first_name']
    last_name = data['last_name']
    url_img_profile = data['picture']['data']['url']

    img_response = requests.get(url_img_profile)
    img_data = img_response.content
    ext = imghdr.what('', h=img_data)
    f = SimpleUploadedFile(f'{facebook_id}.{ext}', img_response.content)

    try:
        user = User.objects.get(username=facebook_id)
        user.last_name = last_name
        user.first_name = first_name
        user.img_profile = f
        user.save()

    except User.DoesNotExist:
        user = User.objects.create_user(
            username=facebook_id,
            first_name=first_name,
            last_name=last_name,
            img_profile=f,
        )

    return user


class FacebookBackend:
    pass
