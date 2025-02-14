from http import HTTPStatus

from django.test import AsyncClient

import pytest


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_health_endpoint_async():
    client = AsyncClient()
    response = await client.get("/api/health")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"status": "ok"}
