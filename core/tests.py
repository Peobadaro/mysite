import pytest
from django.urls import reverse


def test_url_home_resolve_para_home():
    assert reverse("home") == "/home/"


def test_home_retorna_status_200(client):
    resposta = client.get("/home/")
    assert resposta.status_code == 200


def test_home_retorna_hello_world(client):
    resposta = client.get("/home/")
    assert resposta.content.decode() == "Hello World"


@pytest.mark.parametrize("rota", ["/", "/qualquer-coisa/"])
def test_rota_nao_configurada_retorna_404(client, rota):
    resposta = client.get(rota)
    assert resposta.status_code == 404
