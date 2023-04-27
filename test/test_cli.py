import pytest
import subprocess

run_cli = ['python', '../src/main.py']

def test_list_all_entries():
    result = subprocess.run(
        run_cli + ['-list', 'entries'], capture_output=True)
    assert result.stdout.strip() == b'[]'


def test_list_all_SELLER_entries():
    result = subprocess.run(
        run_cli + ['-list', 'entries', '-s', 'Steam'], capture_output=True)
    assert result.stdout.strip() == b'[]'
