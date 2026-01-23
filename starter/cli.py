# starter/cli.py
"""
CLI interface with interactive menu and detailed output.
"""

import sys
from starter.templates import validate_template, list_available_templates, get_template_info
from starter.creator import create_project, get_project_summary
from starter.utils import print_error, print_success, print_info, print_header, print_divider


def show_help():
    """Display all available commands and usage."""
    print_header("GitHub Project Starter - Commands")
    print_divider()
    print("USAGE:")
    print("  starter create <template> <name>    Create new project")
    print("  starter list                        Show available templates")
    print("  starter help                        Show this help")
    print("  starter info <template>             Show template details")
    print("")
    print("EXAMPLES:")
    print("  starter create python my_app")
    print("  starter info python")
    print_divider()


def show_templates():
    """Display all available templates with descriptions."""
    templates = list_available_templates()
    
    if not templates:
        print_error("No templates found")
        return
    
    print_header("Available Templates")
    print_divider()
    
    for template in templates:
        info = get_template_info(template)
        print(f"  {template:15} {info['description']}")
    
    print_divider()
    print(f"Total: {len(templates)} template(s)")


def show_template_info(template_name):
    """Display detailed information about a template."""
    template_path = validate_template(template_name)
    
    if not template_path:
        print_error(f"Template '{template_name}' not found")
        return False
    
    info = get_template_info(template_name)
    
    print_header(f"Template: {template_name}")
    print_divider()
    print(f"Description:  {info['description']}")
    print(f"Language:     {info['language']}")
    print(f"Files:        {info['file_count']}")
    print("")
    print("Included files:")
    for file in info['files']:
        print(f"  - {file}")
    print_divider()
    
    return True


def handle_create(template_name, project_name):
    """Handle project creation with detailed output."""
    # Validate template
    template_path = validate_template(template_name)
    if not template_path:
        print_error(f"Template '{template_name}' not found")
        print_info("Use 'starter list' to see available templates")
        return False
    
    # Create project
    try:
        print_info(f"Creating project '{project_name}'...")
        create_project(template_path, project_name)
        
        # Show summary
        summary = get_project_summary(project_name, template_name)
        
        print_success("Project created successfully")
        print_divider()
        print(f"Project:      {summary['name']}")
        print(f"Template:     {summary['template']}")
        print(f"Language:     {summary['language']}")
        print(f"Location:     {summary['location']}")
        print(f"Files:        {summary['file_count']}")
        print("")
        print("Created files:")
        for file in summary['files']:
            print(f"  - {file}")
        print_divider()
        print("Next steps:")
        print(f"  cd {project_name}")
        print(f"  git init")
        print(f"  # Start coding")
        print_divider()
        
        return True
        
    except FileExistsError:
        print_error(f"Directory '{project_name}' already exists")
        return False
    except Exception as e:
        print_error(f"Failed to create project: {str(e)}")
        return False


def interactive_mode():
    """Run interactive menu."""
    print_header("GitHub Project Starter")
    print_divider()
    print("Commands: create, list, help, info, exit")
    print_divider()
    
    while True:
        try:
            command = input("\n> ").strip().lower()
            
            if not command:
                continue
            
            parts = command.split()
            cmd = parts[0]
            
            if cmd == "exit" or cmd == "quit":
                print_info("Goodbye")
                break
            
            elif cmd == "help":
                show_help()
            
            elif cmd == "list":
                show_templates()
            
            elif cmd == "info":
                if len(parts) < 2:
                    print_error("Usage: info <template>")
                else:
                    show_template_info(parts[1])
            
            elif cmd == "create":
                if len(parts) < 3:
                    print_error("Usage: create <template> <name>")
                else:
                    handle_create(parts[1], parts[2])
            
            else:
                print_error(f"Unknown command: {cmd}")
                print_info("Type 'help' for available commands")
        
        except KeyboardInterrupt:
            print("\n")
            print_info("Use 'exit' to quit")
        except EOFError:
            print("\n")
            break


def main():
    """Main entry point."""
    args = sys.argv[1:]
    
    # No arguments - interactive mode
    if not args:
        interactive_mode()
        return
    
    # Parse command
    cmd = args[0].lower()
    
    # Help command
    if cmd in ["help", "-h", "--help"]:
        show_help()
        return
    
    # List command
    elif cmd == "list":
        show_templates()
        return
    
    # Info command
    elif cmd == "info":
        if len(args) < 2:
            print_error("Usage: starter info <template>")
            sys.exit(1)
        show_template_info(args[1])
        return
    
    # Create command
    elif cmd == "create":
        if len(args) < 3:
            print_error("Usage: starter create <template> <name>")
            sys.exit(1)
        
        success = handle_create(args[1], args[2])
        sys.exit(0 if success else 1)
    
    # Unknown command
    else:
        print_error(f"Unknown command: {cmd}")
        print_info("Use 'starter help' for available commands")
        sys.exit(1)


if __name__ == "__main__":
    main()