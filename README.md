# Python Notebooks Repository Template

A template repository demonstrating best practices for creating and maintaining Jupyter notebooks that are meant to be shared with others.

## 🎯 Who This Is For

**Notebook creators** who need to:
- Share notebooks with colleagues, students, or clients
- Ensure notebooks remain functional over time
- Maintain professional quality standards
- Collaborate on notebook-based projects
- Keep shared content up-to-date and reliable

## 🛠️ What This Template Provides

This repository demonstrates essential practices for **shareable notebook development**:

### 📁 **Directory Structure**
- **notebooks/** - All Jupyter notebooks
- **tests/** - Automated testing
- **utils/** - Utility modules (like authentication)
- **scripts/** - Helper scripts

### 📋 **Quality Assurance**
- **Automated testing** - Ensure notebooks execute successfully
- **Notebook cleaning** - Remove outputs and metadata before sharing
- **CI/CD integration** - Catch issues before they reach your audience

### 🔒 **Security & Configuration**
- **No hardcoded credentials** - Environment-based configuration
- **Secure authentication patterns** - Azure Identity best practices
- **Clean separation** - Code vs. configuration

### 🔄 **Maintainability**
- **Reproducible environments** - Conda environment specifications
- **Version control friendly** - Git hooks for clean commits
- **Automated validation** - Continuous testing of notebook execution

### 📚 **Documentation Standards**
- **Clear explanations** - Thorough but concise documentation
- **Consistent structure** - Standardized notebook organization
- **Professional presentation** - Ready for external sharing

## 🚀 Quick Start

1. **Clone and Setup**
   ```bash
   git clone <this-repo>
   cd <repo-name>
   python -m venv notebook-env

   # Windows
   notebook-env\Scripts\activate
   # macOS/Linux
   source notebook-env/bin/activate

   pip install -r requirements.txt
   ```

2. **Configure Environment**
   ```bash
   cp .env.template .env
   # Edit .env with your configuration values
   ```

3. **Setup Git Hooks (Optional but Recommended)**
   ```bash
   # Windows
   setup_hooks.bat

   # macOS/Linux
   bash setup_hooks.sh
   ```

4. **Test Everything Works**
   ```bash
   jupyter notebook notebooks/simple_demo_notebook.ipynb
   # Run all cells to verify setup
   ```

## 🧹 Git Hooks and Notebook Cleaning

This template automatically cleans notebooks before commits to ensure professional sharing standards.

### **What Gets Cleaned:**
- **Notebook outputs**: Removed to reduce file size and avoid sensitive data
- **Execution metadata**: Cleared for clean diffs
- **Code formatting**: Black formatting applied to Python code
- **Import sorting**: isort organizes imports consistently

### **Setup:**
```bash
# Run the setup script (installs pre-commit hooks)
setup_hooks.bat  # Windows
# or
bash setup_hooks.sh  # macOS/Linux
```

### **Manual Cleaning:**
```bash
# Clean a specific notebook
nbstripout notebooks/simple_demo_notebook.ipynb

# Clean all notebooks
nbstripout notebooks/*.ipynb
```

## 🔧 Environment Variables Setup

This template uses environment variables to keep configuration separate from code and credentials secure.

### **Setup Steps:**

1. **Copy the template:**
   ```bash
   cp .env.template .env
   ```

2. **Edit `.env` with your values:**
   ```bash
   # Example .env file contents
   PROJECT_NAME=my-analysis
   ENVIRONMENT=development
   DEBUG=true
   DATA_URL=https://myapi.com/data
   ```

3. **Use in notebooks:**
   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()
   project_name = os.getenv('PROJECT_NAME', 'default-name')
   ```

### **Security Notes:**
- `.env` files are automatically ignored by git
- Never commit credentials to version control
- Use defaults as fallbacks: `os.getenv('VAR', 'default')`

## Azure Authentication Setup

For notebooks that use Azure services, this template includes secure authentication patterns.

The notebooks in this lab use a helper module (`azure_auth_helper.py`) that handles Azure authentication automatically at the start of each notebook.

### ⚠️ Important: User Permissions Required

**This authentication uses YOUR user account permissions**, so you need to ensure:
- You have required permissions (**Contributor** or **Owner** is overkill but the easiest way to ensure it for learning purposes)
- You have permissions to create and manage Azure AI Foundry resources
- You have access to deploy models and create endpoints

### 🔧 Authentication Options:

**Option 1: Browser Authentication**
```python
# Opens browser for interactive login
credential = authenticate_azure(
    auth_method='browser',
    tenant_id=TENANT_ID
)
```

**Option 2: Device Code**
```python
# Provides a code to enter on another device
credential = authenticate_azure(
    auth_method='device',
    tenant_id=TENANT_ID
)
```

**Option 3: Use az login**
Alternatively handle authentication yourself by installing the azure cli and running az login.


### ✅ What This Gives You:

- **Professional credential handling** - No API keys in notebooks
- **Tenant-specific authentication** for secure access
- **Simple one-line authentication** that works across all notebooks
- **No manual token management** - the helper handles everything
- **Clear error messages** if authentication fails
- **Shareable notebooks** - Others can use the same authentication pattern

The `credential` object returned works seamlessly with all Azure AI Foundry services used in the notebooks.

## 📁 Repository Structure

```
├── azure_auth_helper.py      # Authentication utilities
├── environment.yml           # Conda environment specification
├── .env.template            # Template for environment variables
├── .gitignore              # Git ignore patterns
├── .pre-commit-config.yaml  # Pre-commit hooks configuration
├── pytest.ini             # Test configuration
├── notebooks/              # Example notebooks (your shareable content)
├── tests/                  # Notebook tests
└── .github/workflows/      # CI/CD automation
```

## 🎯 Best Practices Demonstrated

1. **Environment Management** - Reproducible setups for collaborators
2. **Authentication** - Secure, shareable credential patterns
3. **Testing** - Automated validation of notebook execution
4. **Version Control** - Clean, professional git history
5. **Documentation** - Clear explanations for end users
6. **CI/CD** - Automated quality checks before sharing

Perfect for teams sharing data science workflows, educational content, or client deliverables.
