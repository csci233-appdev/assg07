import pytest
from q02 import is_palindrome_iterative
from q02 import is_palindrome_recursive

# test iterative version
def test_empty_string_iterative():
    assert is_palindrome_iterative('')

def test_single_character_iterative():
    assert is_palindrome_iterative('a')
    assert is_palindrome_iterative('Z')

def test_simple_palindromes_iterative():
    assert is_palindrome_iterative('aa')
    assert is_palindrome_iterative('aba')
    assert is_palindrome_iterative('racecar')
    assert is_palindrome_iterative('madam')

def test_not_palindromes_iterative():
    assert not is_palindrome_iterative('ab')
    assert not is_palindrome_iterative('hello')
    assert not is_palindrome_iterative('python')

def test_case_sensitive_iterative():
    assert not is_palindrome_iterative('Racecar')
    assert not is_palindrome_iterative('madaM')

def test_with_spaces_iterative():
    assert not is_palindrome_iterative('a man a plan a canal panama')
    assert is_palindrome_iterative('nur ses run')


# same tests but of recursive version
def test_empty_string_recursive():
    assert is_palindrome_recursive('')

def test_single_character_recursive():
    assert is_palindrome_recursive('a')
    assert is_palindrome_recursive('Z')

def test_simple_palindromes_recursive():
    assert is_palindrome_recursive('aa')
    assert is_palindrome_recursive('aba')
    assert is_palindrome_recursive('racecar')
    assert is_palindrome_recursive('madam')

def test_not_palindromes_recursive():
    assert not is_palindrome_recursive('ab')
    assert not is_palindrome_recursive('hello')
    assert not is_palindrome_recursive('python')

def test_case_sensitive_recursive():
    assert not is_palindrome_recursive('Racecar')
    assert not is_palindrome_recursive('madaM')

def test_with_spaces_recursive():
    assert not is_palindrome_recursive('a man a plan a canal panama')
    assert is_palindrome_recursive('nur ses run')
