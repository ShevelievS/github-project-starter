# starter/templates.py
"""
Template discovery, validation, and metadata.
"""

from pathlib import Path


# Template metadata
# WHY: Centralized information about each template
TEMPLATE_INFO = {
    "python": {
        "description": "Python project with basic structure",
        "language": "Python",
    }
}


def get_templates_directory():
    """Get absolute path to templates directory."""
    starter_dir = Path(__file__).parent
    templates_dir = starter_dir.parent / "templates"
    return templates_dir


def validate_template(template_name):
    """Check if template exists and return its path."""
    templates_dir = get_templates_directory()
    template_path = templates_dir / template_name
    
    if template_path.exists() and template_path.is_dir():
        return template_path
    
    return None


def list_available_templates():
    """Get list of all available template names."""
    templates_dir = get_templates_directory()
    
    if not templates_dir.exists():
        return []
    
    return sorted([d.name for d in templates_dir.iterdir() if d.is_dir()])


def get_template_info(template_name):
    """
    Get metadata about a template.
    WHY: Provides detailed information for display and validation.
    """
    template_path = validate_template(template_name)
    
    if not template_path:
        return None
    
    # Get base info from metadata
    info = TEMPLATE_INFO.get(template_name, {
        "description": "No description available",
        "language": "Unknown"
    })
    
    # Count files in template
    files = []
    for item in sorted(template_path.rglob("*")):
        if item.is_file():
            rel_path = item.relative_to(template_path)
            files.append(str(rel_path))
    
    info["file_count"] = len(files)
    info["files"] = files
    
    return info