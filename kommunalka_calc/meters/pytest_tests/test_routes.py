from http import HTTPStatus
from django.urls import reverse
import pytest


def test_home_availability_for_anonymous_user(client, db):
    url = reverse("meters:calculate")
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_history_page_availability_for_anonymous_user(client, db):
    url = reverse("meters:history")
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_calculate_post_request(client, db):
    """
    Проверяем, что POST-запрос на страницу расчёта
    не падает и возвращает корректный статус.
    """
    url = reverse("meters:calculate")
    data = {
        "cold_water": 10,
        "hot_water": 5,
        "electricity": 100,
    }
    response = client.post(url, data)
    assert response.status_code in (HTTPStatus.OK, HTTPStatus.FOUND)


@pytest.mark.parametrize(
    "route_name",
    [
        "meters:calculate",
        "meters:history",
    ],
)
def test_routes_exist(client, db, route_name):
    """
    Универсальный тест, который проверяет,
    что указанные маршруты существуют и доступны.
    """
    url = reverse(route_name)
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_404_for_unknown_route(client, db):
    """
    Проверяем, что несуществующий маршрут возвращает 404.
    """
    response = client.get("/unknown-route-123/")
    assert response.status_code == HTTPStatus.NOT_FOUND
