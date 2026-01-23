# starter/creator.py
"""
Project creation logic with summary generation.
"""

import shutil
from pathlib import Path
from starter.templates import get_template_info


def create_project(template_path, project_name):
    """Create a new project from template."""
    project_path = Path.cwd() / project_name
    
    if project_path.exists():
        raise FileExistsError(f"Directory '{project_name}' already exists")
    
    try:
        shutil.copytree(template_path, project_path)
    except Exception as e:
        if project_path.exists():
            shutil.rmtree(project_path)
        raise e


def get_project_summary(project_name, template_name):
    """
    Generate summary of created project.
    WHY: Provides user with complete information about what was created.
    """
    project_path = Path.cwd() / project_name
    template_info = get_template_info(template_name)
    
    # Get list of created files
    files = []
    for item in sorted(project_path.rglob("*")):
        if item.is_file():
            rel_path = item.relative_to(project_path)
            files.append(str(rel_path))
    
    return {
        "name": project_name,
        "template": template_name,
        "language": template_info["language"],
        "location": str(project_path.absolute()),
        "file_count": len(files),
        "files": files
    }