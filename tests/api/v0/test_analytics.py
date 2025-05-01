from domain.models.part import Part


class TestListParts:

    def test_return_counter_of_most_common_words_with_success(self, client, db):
        db.add(Part(name="Test name 1", sku="randomUniqueString1", description="Test different common count"))
        db.add(Part(name="Test name 2", sku="randomUniqueString2", description="Common again common to count test Test"))
        db.add(Part(name="Test name 3", sku="randomUniqueString3", description="Test common third common count again"))
        db.commit()

        response = client.get("/analytics/parts/top-words")
        assert response.status_code == 200
        result = response.json()
        result[0] == {"word": "common", "count": 5}
        result[1] == {"word": "test", "count": 4}
        result[2] == {"word": "count", "count": 3}
        result[3] == {"word": "again", "count": 2}
        result[4] == {"word": "different", "count": 1}

    def test_normalizes_case_insensitive(self, client, db):
        db.add(Part(name="Case Test", sku="sku-case", description="Word word WORD WoRd"))
        db.commit()

        response = client.get("/analytics/parts/top-words")
        assert response.status_code == 200
        result = response.json()
        assert result[0] == {"word": "word", "count": 4}

    def test_return_empty_when_no_descriptions(self, client):
        response = client.get("/analytics/parts/top-words")
        assert response.status_code == 200
        assert response.json() == []

    def test_ignore_none_and_empty_descriptions(self, client, db):
        db.add(Part(name="Part 1", sku="sku1", description=None))
        db.add(Part(name="Part 2", sku="sku2", description=""))
        db.add(Part(name="Part 3", sku="sku3", description="Only valid words here"))
        db.commit()

        response = client.get("/analytics/parts/top-words")
        result = response.json()
        assert result[0]["word"] == "only"
        assert result[1]["word"] == "valid"
        assert result[2]["word"] == "words"
        assert result[3]["word"] == "here"

    def test_ignores_punctuation(self, client, db):
        db.add(Part(name="Punct", sku="sku-punct", description="End. end, end! End?"))
        db.commit()

        response = client.get("/analytics/parts/top-words")
        result = response.json()
        assert result[0]["word"] == "end"
        assert result[0]["count"] == 4

    def test_words_with_same_frequency(self, client, db):
        db.add(Part(name="Tie", sku="sku-tie", description="a b c d e f g"))
        db.commit()

        response = client.get("/analytics/parts/top-words")
        result = response.json()
        assert len(result) == 5
        counts = [item["count"] for item in result]
        assert all(c == 1 for c in counts)

    def test_limit_5_words(self, client, db):
        db.add(Part(name="Limit Test", sku="sku-limit", description="x x x x x y y y y z z z q q a b c d"))
        db.commit()

        response = client.get("/analytics/parts/top-words?limit=3")
        result = response.json()
        assert len(result) == 5
