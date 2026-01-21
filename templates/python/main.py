# templates/python/main.py
"""
Main entry point for the application.
WHY: Provides a clear starting point for beginners to add their code.
"""


def main():
    """
    Main function - your code starts here.
    WHY: Using a main() function instead of top-level code is best practice.
         Makes the code importable and testable.
    """
    print("Hello from your new Python project!")
    print("Edit this file to start building your application.")


# Standard Python idiom - only run main() when executed directly
# WHY: Allows importing this module without executing code
if __name__ == "__main__":
    main()