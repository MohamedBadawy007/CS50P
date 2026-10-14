from twttr import shorten

def test_shorten():

    assert shorten("twitter") == "twttr"
    assert shorten("Mohamed") == "Mhmd"
    assert shorten("instagram") == "nstgrm"
    assert shorten("Bye") == "By"
    assert shorten("Union") == "nn"
    assert shorten("Error 404") == "rrr 404"
    assert shorten("Hello, I'm Mohamed") == "Hll, 'm Mhmd"

