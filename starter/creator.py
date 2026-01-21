# starter/creator.py
"""
Project creation logic - handles file and directory operations.
WHY: Separates I/O operations from CLI and template discovery,
     making it easy to test and modify creation behavior.
"""

import shutil
from pathlib import Path


def create_project(template_path, project_name):
    """
    Create a new project from a template.
    
    WHY: Single responsibility - takes validated inputs and performs
         the actual file operations. No validation or UI logic here.
    
    Args:
        template_path: Path object pointing to template directory
        project_name: String name for the new project directory
        
    Raises:
        FileExistsError: If project directory already exists
        Exception: For any other file operation errors
    """
    # Convert project name to Path object
    # WHY: pathlib is cleaner and cross-platform safe
    project_path = Path.cwd() / project_name
    
    # Check if project directory already exists
    # WHY: Prevent accidental overwrites, fail fast
    if project_path.exists():
        raise FileExistsError(f"Directory '{project_name}' already exists")
    
    # Copy entire template directory to new project location
    # WHY: shutil.copytree handles nested directories and preserves permissions
    try:
        shutil.copytree(template_path, project_path)
    except Exception as e:
        # Clean up partial copy if something went wrong
        # WHY: Don't leave broken project directories
        if project_path.exists():
            shutil.rmtree(project_path)
        raise e


def list_template_files(template_path):
    """
    List all files in a template (for debugging/future features).
    
    WHY: Useful for validation or showing what will be created.
         Not used in MVP but demonstrates extensibility.
    """
    template_path = Path(template_path)
    return [f.relative_to(template_path) for f in template_path.rglob("*") if f.is_file()]