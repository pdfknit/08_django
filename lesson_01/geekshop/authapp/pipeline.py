import requests
from django.db import transaction
from social_core.exceptions import AuthForbidden


@transaction.atomic
def get_user_info(backend, user, response, *args, **kwargs):
    resp = requests.get(
        "https://api.github.com/user",
        headers={"Authorization": "token %s" % response["access_token"]},
    )
    json = resp.json()
    print(json)

    # if not json['location']:
    #     raise AuthForbidden("social_core.backends.github.GithubOAuth2")
    # к сожалению, как обрезать начало пути, чтобы ссылка на картинку была норм пока не разобралась( но данные подгружает
    pic = requests.get(json['avatar_url'])
    user.avatar = json['avatar_url']
    user.name = json['name']

    user.save()
