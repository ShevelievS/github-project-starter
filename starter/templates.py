# starter/templates.py
"""
Template discovery and validation.
WHY: Centralizes template-related logic. When we add remote templates
     or template configuration, changes happen only here.
"""

from pathlib import Path


def get_templates_directory():
    """
    Get the absolute path to templates directory.
    
    WHY: No hardcoded paths. Works regardless of installation location.
         Uses __file__ to find templates relative to this module.
    """
    # Get the directory containing this file (starter/)
    starter_dir = Path(__file__).parent
    
    # Go up one level and into templates/
    # WHY: templates/ is sibling to starter/, not inside it
    templates_dir = starter_dir.parent / "templates"
    
    return templates_dir


def validate_template(template_name):
    """
    Check if a template exists and return its path.
    
    WHY: Single source of truth for template validation.
         Returns Path object for easy file operations.
    
    Args:
        template_name: String name of the template (e.g., "python")
        
    Returns:
        Path object if template exists, None otherwise
    """
    templates_dir = get_templates_directory()
    template_path = templates_dir / template_name
    
    # Check if template directory exists and is actually a directory
    # WHY: Prevents errors from files named like templates
    if template_path.exists() and template_path.is_dir():
        return template_path
    
    return None


def list_available_templates():
    """
    Get list of all available template names.
    
    WHY: Useful for showing available options to users.
         Not used in MVP but demonstrates extensibility.
    """
    templates_dir = get_templates_directory()
    
    # Only return directories, not files
    # WHY: Templates are directories, not individual files
    if not templates_dir.exists():
        return []
    
    return [d.name for d in templates_dir.iterdir() if d.is_dir()]