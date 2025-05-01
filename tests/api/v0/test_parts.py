from domain.models.part import Part


class TestListParts:

    def test_read_parts_empty(self, client):
        response = client.get("/parts/")
        assert response.status_code == 200
        assert response.json() == []

    def test_read_parts_with_data(self, client, db):
        part = Part(name="Test Part", sku="randomUniqueString")
        db.add(part)
        db.commit()

        response = client.get("/parts/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["name"] == "Test Part"


class TestGetPartByID:

    def test_read_part_by_id_with_success(self, client, db):
        part = Part(name="Test Part", sku="randomUniqueString")
        db.add(part)
        db.commit()

        response = client.get(f"/parts/{part.id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert data["name"] == part.name

    def test_read_part_with_invalid_id_return_404(self, client):
        response = client.get("/parts/1")
        assert response.status_code == 404
        data = response.json() == "Part not found"


class TestCreatePart:

    def test_create_part_with_success(self, client):
        input_body = {"name": "Updated Name","sku": "uniqueString"}
        response = client.post(f"/parts/", json=input_body)
        assert response.status_code == 201

    def test_create_part_with_invalid_fields(self, client):
        response = client.post(f"/parts/", json={"name": "New Part"})
        assert response.status_code == 422
        response.json()["detail"][0]["msg"] == 'Field required'

    def test_create_part_with_empty_body(self, client):
        response = client.post(f"/parts/", json={})
        assert response.status_code == 422

    def test_create_part_duplicate_sku_should_fail(self, client, db):
        part = Part(name="Test Part", sku="duplicateSKU")
        db.add(part)
        db.commit()

        response = client.post("/parts/", json={"name": "Another", "sku": "duplicateSKU"})
        assert response.status_code == 409


class TestUpdatePart:

    def test_update_part_with_success(self, client, db):
        part = Part(name="Test Part", sku="randomUniqueString")
        db.add(part)
        db.commit()

        input_body = {"name": "Updated Name"}
        response = client.put(f"/parts/{part.id}", json=input_body)
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Updated Name"

    def test_update_non_existent_part_return_404(self, client):
        response = client.put("/parts/1", json={})
        assert response.status_code == 404
        response.json() == "Part not found"

    def test_validate_expected_input(self, client, db):
        part = Part(name="Test Part", sku="randomUniqueString")
        db.add(part)
        db.commit()

        response = client.put(f"/parts/{part.id}", json={"name": 1})
        assert response.status_code == 422

    def test_partial_update_does_not_change_unset_fields(self, client, db):
        part = Part(name="Original Name", sku="sku-123")
        db.add(part)
        db.commit()

        client.put(f"/parts/{part.id}", json={"name": "New Name"})
        db.refresh(part)
        assert part.name == "New Name"
        assert part.sku == "sku-123"

    def test_update_with_extra_field_should_fail_or_ignore(self, client, db):
        part = Part(name="Test Part", sku="sku-xyz")
        db.add(part)
        db.commit()

        response = client.put(f"/parts/{part.id}", json={"name": "Updated", "extra": "not-allowed"})
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Updated"


class TestDeletePart:

    def test_delete_part_with_success(self, client, db):
        part = Part(name="Test Part", sku="randomUniqueString")
        db.add(part)
        db.commit()

        response = client.delete(f"/parts/{part.id}")
        assert response.status_code == 204

    def test_delete_non_existent_part_return_404(self, client):
        response = client.delete("/parts/1")
        assert response.status_code == 404
        response.json() == "Part not found"

    def test_delete_part_and_check_get_returns_404(self, client, db):
        part = Part(name="Test Part", sku="sku-to-delete")
        db.add(part)
        db.commit()

        delete_response = client.delete(f"/parts/{part.id}")
        assert delete_response.status_code == 204

        get_response = client.get(f"/parts/{part.id}")
        assert get_response.status_code == 404
