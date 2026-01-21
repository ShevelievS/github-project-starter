# starter/cli.py
"""
CLI interface - handles argument parsing and command routing.
WHY: Isolates CLI concerns from business logic, making it easy to
     add new commands or change argument structure later.
"""

import sys
from starter.templates import validate_template
from starter.creator import create_project
from starter.utils import print_error, print_success


def parse_arguments(args):
    """
    Parse command line arguments.
    WHY: Centralized parsing makes it easy to add validation or new flags.
    
    Expected format: starter create <template_name> <project_name>
    """
    if len(args) < 3:
        return None, None, None
    
    command = args[0]
    template_name = args[1]
    project_name = args[2]
    
    return command, template_name, project_name


def show_usage():
    """
    Display usage information.
    WHY: Separate function allows reuse from error handlers.
    """
    print("Usage: starter create <template_name> <project_name>")
    print("\nAvailable templates:")
    print("  python - Python project with basic structure")
    print("\nExample:")
    print("   starter create python <project_name>")


def main():
    """
    Main entry point for CLI.
    WHY: Single entry point makes packaging and testing easier.
    """
    # Remove script name from arguments
    args = sys.argv[1:]
    
    # Show usage if no arguments provided
    if not args:
        show_usage()
        sys.exit(1)
    
    # Parse arguments
    command, template_name, project_name = parse_arguments(args)
    
    # Validate command structure
    if not command or not template_name or not project_name:
        print_error("Invalid command format")
        show_usage()
        sys.exit(1)
    
    # Only support 'create' command for MVP
    if command != "create":
        print_error(f"Unknown command: {command}")
        show_usage()
        sys.exit(1)
    
    # Validate template exists
    # WHY: Fail fast before any file operations
    template_path = validate_template(template_name)
    if not template_path:
        print_error(f"Template '{template_name}' not found")
        sys.exit(1)
    
    # Create the project
    # WHY: Delegate actual work to creator module
    try:
        create_project(template_path, project_name)
        print_success(f"Project '{project_name}' created successfully!")
        print(f"\nNext steps:")
        print(f"  cd {project_name}")
        print(f"  # Start coding!")
    except FileExistsError:
        print_error(f"Directory '{project_name}' already exists")
        sys.exit(1)
    except Exception as e:
        print_error(f"Failed to create project: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()