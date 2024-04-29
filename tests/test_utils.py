import pytest
from datetime import datetime
from utils.utils import normalize_phone, overlaps_days

@pytest.mark.parametrize("input_phone, expected_output", [
    (None, ""),
    ("1-555-555-5555", "5555555555"),
    ("+1-555-555-5555", "5555555555"),
    ("555-555-5555", "5555555555"),
    ("1-(555)-555-5555", "5555555555"),
    ("+1 (555) 555-5555", "5555555555"),
])
def test_normalize_phone(input_phone, expected_output):
    assert normalize_phone(input_phone) == expected_output

@pytest.mark.parametrize("start1, end1, start2, end2, expected", [
    (datetime(2023, 1, 1).date(), datetime(2023, 10, 1).date(), datetime(2023, 2, 1).date(), datetime(2023, 5, 4).date(), True),  # Overlaps by more than 90 days
    (datetime(2023, 1, 1).date(), datetime(2023, 4, 1).date(), datetime(2023, 3, 1).date(), datetime(2023, 3, 10).date(), False),  # Overlaps by less than 90 days
    (datetime(2023, 1, 1).date(), datetime(2023, 4, 1).date(), datetime(2024, 5, 1).date(), datetime(2024, 6, 1).date(), False),  # No overlap
    (datetime(2023, 1, 1).date(), None, datetime(2023, 3, 1).date(), None, True),  # Overlaps by more than 90 days (still working)
    (datetime(2023, 1, 1).date(), datetime(2023, 4, 1).date(), datetime(2023, 1, 1).date(), datetime(2023, 4, 1).date(), True),  # Same period
    (datetime(2023, 1, 1).date(), datetime(2023, 4, 1).date(), datetime(2024, 1, 1).date(), datetime(2024, 12, 31).date(), False),  # No overlap, different years
    (datetime(2023, 1, 1).date(), datetime(2024, 4, 4).date(), datetime(2024, 1, 1).date(), datetime(2024, 4, 4).date(), True),  # Overlap starting in different years
])
def test_overlaps_days(start1, end1, start2, end2, expected):
    assert overlaps_days(start1, end1, start2, end2, 90) == expected