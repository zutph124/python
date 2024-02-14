Be sure to include
    import twttr
or

    from twttr import shorten
atop test_twttr.py so that you can call shorten in your tests.

Take care to return, not print, a str in shorten. Only main should call print.

Note that you can check with pytest whether a function has raised an exception, 
per docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions.
