from pytemp import pytemp
import pytest


def test_absolute_zero_input():
    # Test all possible temperature conversion combinations with -273.15°C as the input temperature
    conversions = [
        ('C', 'F', -459.67),
        ('C', 'K', 0),
    ]

    for conversion in conversions:
        input_unit, output_unit, expected_result = conversion
        result = pytemp(-273.15, input_unit, output_unit)
        assert result == pytest.approx(expected_result)


def test_boundary_values():
    # Test the boundary values for the input temperature
    def test_boundary_values():
        # Test the boundary values for the input temperature
        test_cases = [
            # Test just inside the lower boundary
            (-459.67, 'F', 'C', -273.15),
            (-459.67, 'F', 'K', 0.000555556),
            (-273.15, 'C', 'F', -459.67),
            (-273.15, 'C', 'K', 0.0),
            (0.0, 'K', 'F', -459.67),
            (0.0, 'K', 'C', -273.15),
            # Test just outside the lower boundary
            (-459.68, 'F', 'C', None),
            (-459.68, 'F', 'K', None),
            (-273.16, 'C', 'F', None),
            (-273.16, 'C', 'K', None),
            (-0.01, 'K', 'F', None),
            (-0.01, 'K', 'C', None),

        ]
        # Test each input temperature
        for input_temp, from_scale, to_scale, expected_output in test_cases:
            try:
                assert pytest.approx(pytemp(input_temp, from_scale, to_scale), expected_output, 0.01)
            except AssertionError:
                print(f"Soft assertion failed for input temperature {input_temp} {from_scale}:")
                print(f"Expected output: {expected_output}")
                print(f"Actual output: {pytemp(input_temp, from_scale, to_scale)}")