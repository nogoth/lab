import pytest
from quicksort import f_y_shuff


def test_f_y_shuff_single_element():
    # Test the 1's case - single element array
    arr = [42]
    result = f_y_shuff(arr.copy())  # Copy to prevent modifying original
    assert result == arr, "Single element array should remain unchanged"


def test_f_y_shuff_bulk():
    # Test with a larger array
    original = list(range(100))  # Create array [0,1,2,...,99]
    shuffled = f_y_shuff(original.copy())  # Copy to prevent modifying original

    # Test length remains the same
    assert len(shuffled) == len(
        original
    ), "Shuffled array should have same length as original"

    # Test all elements are preserved (same elements, possibly different order)
    assert sorted(shuffled) == sorted(
        original
    ), "Shuffled array should contain same elements as original"

    # Test that the array is actually shuffled (not in same order)
    # Note: There's a very small chance this could fail even with correct implementation
    # due to random chance, but it's extremely unlikely with a large array
    assert shuffled != original, "Array should be shuffled (different order)"

    # Test that all elements from original exist in shuffled
    for elem in original:
        assert elem in shuffled, f"Element {elem} missing from shuffled array"
