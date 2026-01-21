# starter/utils.py
"""
Shared utilities - helpers used across multiple modules.
WHY: Prevents code duplication and circular imports.
     Common formatting and error handling in one place.
"""


def print_error(message):
    """
    Print error message in consistent format.
    WHY: Centralized error formatting makes it easy to add colors
         or logging later without changing every error site.
    """
    print(f"Error: {message}")


def print_success(message):
    """
    Print success message in consistent format.
    WHY: Centralized success formatting. Avoid Unicode issues on Windows.
    """
    # Use ASCII checkmark for Windows compatibility
    print(f"[SUCCESS] {message}")


def print_warning(message):
    """
    Print warning message in consistent format.
    WHY: Not used in MVP but prepared for future validation warnings.
    """
    print(f"Warning: {message}")


def validate_project_name(name):
    """
    Validate project name follows conventions.
    WHY: Prevents invalid directory names early.
         Not used in MVP but demonstrates where validation would go.
    
    Args:
        name: String project name
        
    Returns:
        tuple: (is_valid: bool, error_message: str or None)
    """
    # Check for empty name
    if not name or not name.strip():
        return False, "Project name cannot be empty"
    
    # Check for invalid characters
    # WHY: Some characters are problematic in directory names
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for char in invalid_chars:
        if char in name:
            return False, f"Project name cannot contain '{char}'"
    
    return True, None