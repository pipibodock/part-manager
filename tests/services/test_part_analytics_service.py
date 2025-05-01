from domain.models.part import Part
from services.part_analytics_service import PartAnalyticsService


class TestPartAnalyticsService:
    def test_count_most_common_words_basic(self, db):
        service = PartAnalyticsService(db)

        db.add(Part(name="Test name 1", sku="sku1", description="Test different common count"))
        db.add(Part(name="Test name 2", sku="sku2", description="Common again common to count test Test"))
        db.add(Part(name="Test name 3", sku="sku3", description="Test common third common count again"))
        db.commit()

        result = service.count_description_comon_words()
        expected = [('common', 5), ('test', 4), ('count', 3), ('again', 2), ('different', 1)]
        assert result == expected

    def test_count_most_common_words_with_different_quantity(self, db):
        service = PartAnalyticsService(db)

        db.add(Part(name="Test name 1", sku="sku1", description="Test different common count"))
        db.add(Part(name="Test name 2", sku="sku2", description="Common again common to count test Test"))
        db.add(Part(name="Test name 3", sku="sku3", description="Test common third common count again"))
        db.commit()

        result = service.count_description_comon_words(1)
        expected = [('common', 5)]
        assert result == expected

    def test_empty_descriptions_returns_empty_list(self, db):
        service = PartAnalyticsService(db)

        result = service.count_description_comon_words()
        assert result == []

    def test_none_and_empty_descriptions_are_ignored(self, db):
        service = PartAnalyticsService(db)

        db.add(Part(name="Part 1", sku="sku1", description=None))
        db.add(Part(name="Part 2", sku="sku2", description=""))
        db.add(Part(name="Part 3", sku="sku3", description="Valid description only once"))
        db.commit()

        result = service.count_description_comon_words()
        expected = [('valid', 1), ('description', 1), ('only', 1), ('once', 1)]
        assert result == expected

