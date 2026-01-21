# setup.py (FIXED VERSION)
from setuptools import setup

setup(
    name="github-project-starter",
    version="0.1.0",
    # WHY: Only include the starter package, exclude templates/
    packages=["starter"],
    # WHY: Tell setuptools to ignore templates/ folder
    package_dir={"": "."},
    entry_points={
        'console_scripts': [
            'starter=starter.cli:main',
        ],
    },
    python_requires='>=3.7',
)