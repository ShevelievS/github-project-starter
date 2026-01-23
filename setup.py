# setup.py
from setuptools import setup, find_packages
import os

# Read README if exists
long_description = ""
if os.path.exists('README.md'):
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()

setup(
    name="github-project-starter",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            # WHY: Прямая ссылка на main() избегает импорта при загрузке пакета
            'starter=starter.cli:main',
        ],
    },
    package_data={
        '': ['templates/**/*'],
    },
    python_requires='>=3.6',
    author="Your Name",
    description="CLI tool to create projects from templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
)