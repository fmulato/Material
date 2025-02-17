"""hat This Code Does:
1. Imports pytest to run automated tests.
2. Defines a simple test (test_something) that checks if my_data is equal to 42.
3. Uses @pytest.mark.parametrize to test the rolling_average function with multiple input cases.
4. Calls project_module.rolling_average(values, 3) and verifies its output against expected results.
5. Tests the implementation of a rolling average with a window size of 3.
"""


import pytest

from my_project import project_module

def test_something(my_data):
    assert my_data == 42

@pytest.mark.parametrize("values,expected_results",[
    (
    [1,2,3,4,5,6],
    [2.0, 3.0, 4.0, 5.0],
    ),
    (
    [-1,-2,-3,-4,-5,-6],
    [-2.0, -3.0, -4.0, -5.0], # the original test was wrong, I corrected it adding -5.0
    ),
    (
    [7,8,0,10],
    [5.0, 6.0], # I included this new test case
    ),
])

def test_rolling_average(values,expected_results):
    result = project_module.rolling_average(values, 3)
    assert result == expected_results
