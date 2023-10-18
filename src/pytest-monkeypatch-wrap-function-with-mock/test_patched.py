from os.path import join as real_join
import os.path

def do_join(*args):
    return os.path.join(*args)

def test_join():
    """Call the function without monkeypatching."""
    assert do_join("foo", "bar") == "foo/bar"

def test_patched(monkeypatch):
    """Replace function call with wrapper."""
    def mock_join(*args):
        """Mock version that calls the real one"""
        return real_join("wrapped", *args)

    monkeypatch.setattr(os.path, "join", mock_join)
    assert do_join("a", "b") == "wrapped/a/b"
