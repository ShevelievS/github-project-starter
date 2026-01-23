# starter/utils.py
"""
Shared utilities for consistent output formatting.
"""


def print_divider(char="-", length=60):
    """Print horizontal divider line."""
    print(char * length)


def print_header(text):
    """Print section header."""
    print(f"\n{text}")


def print_error(message):
    """Print error message."""
    print(f"[ERROR] {message}")


def print_success(message):
    """Print success message."""
    print(f"[OK] {message}")


def print_info(message):
    """Print informational message."""
    print(f"[INFO] {message}")


def print_warning(message):
    """Print warning message."""
    print(f"[WARN] {message}")