import  twttr
from twttr import shorten

def test_shorten_lowercase():
    assert shorten("twitter") == "twttr"

def test_shorten_uppercase():
    assert shorten("GOOGLE") == "GGL"

def test_shorten_numbers():
    assert shorten("12345") == "12345"

def test_shorten_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"