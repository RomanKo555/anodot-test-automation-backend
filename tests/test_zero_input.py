from pytemp import pytemp
import pytest

def test_zero_input():
    # Test all possible temperature conversion combinations with 0 as the input temperature
    conversions = [
        ('F', 'C', -17.77777777777778),
        ('F', 'K', 255.3722),
        ('C', 'F', 32),
        ('C', 'K', 273.15),
        ('K', 'F', -459.67),
        ('K', 'C', -273.15),
    ]

    for conversion in conversions:
        input_unit, output_unit, expected_result = conversion
        result = pytemp(0, input_unit, output_unit)
        assert result == pytest.approx(expected_result)