"""
Tests for the main module.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import main


def test_main(capsys):
    """Test that main runs without error."""
    main()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out
