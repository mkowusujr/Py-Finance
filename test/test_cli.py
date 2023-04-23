import pytest
import subprocess

run_cli = ['python', '../src/main.py']

def test_display_all_entries():
    result = subprocess.run(
        run_cli + ['-disp', 'entries'], capture_output=True)
    assert result.stdout.strip() == b'[]'


def test_display_all_SELLER_entries():
    result = subprocess.run(
        run_cli + ['-disp', 'entries', '-s', 'Steam'], capture_output=True)
    assert result.stdout.strip() == b'[]'
