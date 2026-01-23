#!/bin/bash
# starter.sh - Launch GitHub Project Starter in terminal (Linux/Mac)
# WHY: Cross-platform launcher for Unix systems

echo ""
echo "================================================"
echo "  GitHub Project Starter"
echo "================================================"
echo ""
echo "[INFO] Initializing..."
echo ""

# Run starter in interactive mode
python3 -m starter

# Keep terminal open
exec $SHELL
```

---

## Пример вывода
```
================================================
  GitHub Project Starter
================================================
[INFO] Initializing...

GitHub Project Starter
------------------------------------------------------------
Commands: create, list, help, info, exit
------------------------------------------------------------

> create python my_api
[INFO] Creating project 'my_api'...
[OK] Project created successfully
------------------------------------------------------------
Project:      my_api
Template:     python
Language:     Python
Location:     C:\Users\Dev\projects\my_api
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

> info python
Template: python
------------------------------------------------------------
Description:  Python project with basic structure
Language:     Python
Files:        4

Included files:
  - .gitignore
  - README.md
  - main.py
  - requirements.txt
------------------------------------------------------------

> exit
[INFO] Goodbye