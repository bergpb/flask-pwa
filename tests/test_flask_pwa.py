from . import client


def test_import_pwa():
    try:
        from flask_pwa import Vue
    except ImportError:
        pass


def test_index_route_return_status_code_200(client):
    res = client.get("/")
    assert res.status_code == 200


def test_offline_route_return_status_code_200(client):
    res = client.get("/offline")
    assert res.status_code == 200


def test_manifest_route_return_status_code_200(client):
    res = client.get("/manifest.json")
    assert res.status_code == 200


def test_sw_route_return_status_code_200(client):
    res = client.get("/sw.js")
    assert res.status_code == 200
