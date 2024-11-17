import httpx
from furl import furl

from yappa.settings import YANDEX_FUNCTIONS_URL


def call_manage_function(yc, function_id, command, args):
    iam_token = yc.get_iam_token()
    response = call_function(
        function_id, iam_token, "POST", {"command": command, "args": args}
    )
    return response.content.decode()


def call_function(function_id, token, method, body):
    url = (furl(YANDEX_FUNCTIONS_URL) / function_id).url
    with httpx.Client(headers=dict(Authorization=f"Bearer {token}"), timeout=600) as client:
        request = client.build_request(method, url, json=body)
        response = client.send(request)
    return response
