import pytest
from pytemp import pytemp

def test_equivalence_partitioning():
    # Define equivalence classes for the input temperature
    valid_temps = [-273.15, 0.0, 100.0, 1000.0]

    # Test valid input temperatures
    for temp in valid_temps:
        # Test conversion from Celsius to Fahrenheit
        expected_fahrenheit = (temp * 9/5) + 32
        assert pytemp(temp, 'C', 'F') == pytest.approx(expected_fahrenheit)

        # Test conversion from Celsius to Kelvin
        expected_kelvin = temp + 273.15
        assert pytemp(temp, 'C', 'K') == pytest.approx(expected_kelvin)

        # Test conversion from Fahrenheit to Celsius
        expected_celsius = (temp - 32) * 5/9
        assert pytemp(temp, 'F', 'C') == pytest.approx(expected_celsius)

        # Test conversion from Fahrenheit to Kelvin
        expected_kelvin = (temp + 459.67) * 5/9
        assert pytemp(temp, 'F', 'K') == pytest.approx(expected_kelvin)

        # Test conversion from Kelvin to Celsius
        expected_celsius = temp - 273.15
        assert pytemp(temp, 'K', 'C') == pytest.approx(expected_celsius)

        # Test conversion from Kelvin to Fahrenheit
        expected_fahrenheit = (temp * 9/5) - 459.67
        assert pytemp(temp, 'K', 'F') == pytest.approx(expected_fahrenheit)


