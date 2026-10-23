import pytest
from q03 import factorial
from q03 import combinations
from q03 import combinations_recursive

# test the factorial function
def test_factorial_base_case():
    assert factorial(0) == 1
    assert factorial(1) == 1

def test_factorial_small_numbers():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120

def test_factorial_larger_numbers():
    assert factorial(6) == 720
    assert factorial(7) == 5040
    assert factorial(8) == 40320
    assert factorial(9) == 362880
    assert factorial(10) == 3628800
    assert factorial(20) == 2432902008176640000
    assert factorial(30) == 265252859812191058636308480000000


# test non recursive combinations implementation
def test_combinations_base_cases():
    assert combinations(0, 0) == 1
    assert combinations(5, 0) == 1
    assert combinations(5, 5) == 1

def test_combinations_valid_cases():
    assert combinations(3, 2) == 3
    assert combinations(4, 2) == 6
    assert combinations(5, 2) == 10
    assert combinations(6, 3) == 20
    assert combinations(7, 4) == 35
    assert combinations(12, 6) == 924
    assert combinations(12, 8) == 495


# test recursive combinations implementation
def test_combinations_recursive_base_cases():
    assert combinations_recursive(0, 0) == 1
    assert combinations_recursive(5, 0) == 1
    assert combinations_recursive(5, 5) == 1

def test_combinations_recursive_valid_cases():
    assert combinations_recursive(3, 2) == 3
    assert combinations_recursive(4, 2) == 6
    assert combinations_recursive(5, 2) == 10
    assert combinations_recursive(6, 3) == 20
    assert combinations_recursive(7, 4) == 35
    assert combinations_recursive(12, 6) == 924
    assert combinations_recursive(12, 8) == 495
