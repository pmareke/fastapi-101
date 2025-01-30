from http.client import CREATED, NO_CONTENT, NOT_FOUND, OK

import pytest
from expects import be_none, equal, expect
from fastapi.testclient import TestClient

from main import create_app


class TestItemsAcceptance:
    payload = {"name": "Item 1", "value": 10}

    @pytest.fixture(autouse=True)
    def client(self) -> TestClient:
        app = create_app()
        return TestClient(app)

    def test_save_one_item(self, client: TestClient) -> None:
        response = client.post("/api/v1/items", json=self.payload)
        item_id = response.json()["value"]

        expect(response.status_code).to(equal(CREATED))
        expect(item_id).not_to(be_none)

    def test_find_all_items(self, client: TestClient) -> None:
        create_response = client.post("/api/v1/items", json=self.payload)
        item_id = create_response.json()["value"]
        response = client.get("/api/v1/items/")

        expect(response.status_code).to(equal(OK))
        items = [{"item_id": {"value": item_id}, **self.payload}]
        expect(response.json()).to(equal(items))

    def test_find_one_item(self, client: TestClient) -> None:
        response = client.post("/api/v1/items", json=self.payload)
        item_id = response.json()["value"]
        response = client.get(f"/api/v1/items/{item_id}")

        item = {"item_id": {"value": item_id}, **self.payload}
        expect(response.json()).to(equal(item))

    def test_find_one_non_existing_item(self, client: TestClient) -> None:
        response = client.get("/api/v1/items/non-existing-item-id")

        expect(response.status_code).to(equal(NOT_FOUND))

    def test_update_one_item(self, client: TestClient) -> None:
        create_response = client.post("/api/v1/items", json=self.payload)
        item_id = create_response.json()["value"]
        payload = {"name": "Item 1", "value": 20}
        response = client.put(f"/api/v1/items/{item_id}", json=payload)

        expect(response.status_code).to(equal(OK))

        response = client.get(f"/api/v1/items/{item_id}")

        item = {"item_id": {"value": item_id}, **payload}
        expect(response.json()).to(equal(item))

    def test_delete_one_item(self, client: TestClient) -> None:
        create_response = client.post("/api/v1/items", json=self.payload)
        item_id = create_response.json()["value"]
        response = client.delete(f"/api/v1/items/{item_id}")

        expect(response.status_code).to(equal(NO_CONTENT))

    def test_delete_one_non_existing_item(self, client: TestClient) -> None:
        response = client.delete("/api/v1/items/non-existing-item-id")

        expect(response.status_code).to(equal(NOT_FOUND))
