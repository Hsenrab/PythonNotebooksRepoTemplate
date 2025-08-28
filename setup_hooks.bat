@echo off
REM Setup script for git hooks and notebook cleaning (Windows)

echo 🔧 Setting up git hooks and notebook cleaning...

REM Install pre-commit hooks
echo 📋 Installing pre-commit hooks...
pre-commit install

REM Install nbstripout as git filter
echo 🧹 Setting up nbstripout for automatic notebook cleaning...
nbstripout --install

echo ✅ Git hooks setup complete!
echo.
echo 📝 What this does:
echo    - Cleans notebooks automatically before commits
echo    - Formats Python code with black
echo    - Sorts imports with isort
echo    - Removes trailing whitespace
echo    - Checks for large files
echo.
echo 🎯 To test: make changes to a notebook and run 'git add' + 'git commit'

pause
