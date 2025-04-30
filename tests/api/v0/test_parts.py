from domain.models.part import Part

class TestPartList:

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