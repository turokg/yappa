import logging
from pathlib import Path

import httpx

from .common import (
    DEFAULT_CONFIG_FILENAME,
    body_to_bytes,
    load_yaml,
    patch_response,
)
from .wsgi import load_app

logger = logging.getLogger(__name__)


async def call_app(application, event):
    host_url = event["headers"].get("Host", "https://raw-function.net")
    if not host_url.startswith("http"):
        host_url = f"https://{host_url}"
    body_to_bytes(event)

    transport = httpx.ASGITransport(app=application)
    async with httpx.AsyncClient(transport=transport, base_url=host_url) as client:
        request = client.build_request(
            method=event["httpMethod"],
            url=event["url"],
            headers=event["headers"],
            params=event["queryStringParameters"],
            content=event["body"],
        )
        response = await client.send(request)
        return response


try:
    config = load_yaml(
        Path(Path(__file__).resolve().parent.parent, DEFAULT_CONFIG_FILENAME)
    )

    app = load_app(
        config.get("entrypoint"), config.get("DJANGO_SETTINGS_MODULE")
    )
except ValueError:
    logger.warning("Looks like broken Yappa config is used")


async def handle(event, context):
    if not event:
        return {
            "statusCode": 500,
            "body": "got empty event",
        }
    try:
        response = await call_app(app, event)
        return patch_response(response)
    except Exception as e:
        logger.error("unhandled error", exc_info=True)
        return {
            "statusCode": 500,
            "body": f"got unhandled exception ({e}). Most likely on "
            f"Yappa side. See clouds logs for traceback",
        }
