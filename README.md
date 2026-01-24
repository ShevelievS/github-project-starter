# GitHub Project Starter

Simple CLI tool to create project structures from predefined templates. Eliminates repetitive setup work and helps developers start coding faster.

## Features

- **3 Built-in Templates**: Python, JavaScript, C++
- **Zero Configuration**: Works out of the box
- **Interactive Mode**: Menu-driven interface
- **Clean Output**: Minimal, informative messages
- **Cross-Platform**: Works on Windows, Linux, macOS

## Installation

### Option 1: Install with pip (Recommended)
```bash
git clone https://github.com/yourusername/github-project-starter.git
cd github-project-starter
pip install -e .
```

After installation, `starter` command is available globally.

### Option 2: Run without installation (Windows)
```bash
# Double-click run.bat
# Or from command line:
run.bat
```

### Option 3: Direct execution
```bash
cd github-project-starter
python -m starter
```

## Quick Start
```bash
# Create a Python project
starter create python my_app

# Create a JavaScript project
starter create javascript my_web_app

# Create a C++ project
starter create cpp my_game
```

## Usage

### Command Line Mode
```bash
# Show all available templates
starter list

# Get template details
starter info python

# Create project from template
starter create <template> <project_name>

# Show help
starter help
```

### Interactive Mode

Run `starter` without arguments to enter interactive mode:
```bash
starter
```

Available commands in interactive mode:
- `create <template> <name>` - Create new project
- `list` - Show available templates
- `info <template>` - Show template details
- `help` - Display help
- `exit` - Quit application

## Templates

### Python
```
my_app/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

**Includes**: Basic structure, virtual environment setup, pip dependencies

### JavaScript
```
my_app/
├── index.js
├── package.json
├── .npmrc
├── README.md
└── .gitignore
```

**Includes**: Node.js setup, npm scripts, ES6 structure

### C++
```
my_app/
├── src/
│   └── main.cpp
├── include/
├── CMakeLists.txt
├── README.md
└── .gitignore
```

**Includes**: CMake build system, modern C++17, cross-platform configuration

## Example Output
```bash
$ starter create python my_api

[INFO] Creating project 'my_api'...
[OK] Project created successfully
------------------------------------------------------------
Project:      my_api
Template:     python
Language:     Python
Location:     C:\Users\Dev\Projects\my_api
Files:        4

Created files:
  - .gitignore
  - README.md
  - main.py
  - requirements.txt
------------------------------------------------------------
Next steps:
  cd my_api
  git init
  # Start coding
------------------------------------------------------------
```

## Commands Reference

| Command | Description | Example |
|---------|-------------|---------|
| `starter create <template> <name>` | Create new project | `starter create python my_app` |
| `starter list` | Show all templates | `starter list` |
| `starter info <template>` | Show template details | `starter info javascript` |
| `starter help` | Display help | `starter help` |
| `starter` | Interactive mode | `starter` |

## Project Structure
```
github-project-starter/
├── starter/              # Core application
│   ├── cli.py           # Command interface
│   ├── creator.py       # Project creation logic
│   ├── templates.py     # Template management
│   └── utils.py         # Output utilities
├── templates/           # Template storage
│   ├── python/
│   ├── javascript/
│   └── cpp/
├── setup.py            # Package configuration
├── run.bat             # Windows launcher
└── README.md
```

## Requirements

- Python 3.6 or higher
- pip (for installation)

## Development

### Adding New Templates

1. Create new directory in `templates/`
2. Add template files
3. Update `TEMPLATE_INFO` in `starter/templates.py`

Example:
```python
TEMPLATE_INFO = {
    "mytemplate": {
        "description": "My custom template",
        "language": "MyLanguage",
    }
}
```

### Running Tests
```bash
# Create test projects
starter create python test_py
starter create javascript test_js
starter create cpp test_cpp

# Verify structure
ls test_py/
ls test_js/
ls test_cpp/
```

## Troubleshooting

**Error: "No module named starter"**
- Install package: `pip install -e .`
- Or run from project root: `python -m starter`

**Error: "Template not found"**
- Check available templates: `starter list`
- Verify template name spelling

**Windows: run.bat closes immediately**
- Ensure Python is in PATH
- Run from command line to see errors

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add feature"`
4. Push to branch: `git push origin feature-name`
5. Submit pull request

## License

MIT License - see LICENSE file for details

## Author

Your Name - [@ShevelievS](https://github.com/ShevelievS)

## Acknowledgments

Built with simplicity and developer productivity in mind.

---

**Star this repo** if you find it useful! ⭐
