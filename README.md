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

## 🧹 Git Hooks and Notebook Cleaning

This template automatically cleans notebooks before commits to ensure professional sharing standards.

### **What Gets Cleaned:**

- **Notebook outputs**: Removed to reduce file size and avoid sensitive data
- **Execution metadata**: Cleared for clean diffs

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
7. **Branch Protection** - Ensure tests pass before merging changes

Perfect for teams sharing data science workflows, educational content, or client deliverables.

## 🔒 Setting Up Repository Rulesets

Protect your main branch by requiring tests to pass before merging pull requests using GitHub's Repository Rulesets feature. This ensures all notebooks remain functional and prevents broken code from being merged.

### Setting Up GitHub Repository Rulesets

1. **Navigate to Repository Settings**
   - Go to your repository on GitHub
   - Click on "Settings" in the top navigation bar

2. **Create a Ruleset**
   - In the left sidebar, click on "Rules" or "Rulesets"
   - Click "Add rule" or "New ruleset"
   - Select "Branch ruleset" (GitHub offers two types: branch rulesets and tag rulesets)
   - Name your ruleset (e.g., "Main Branch Protection")

3. **Configure Bypass List (Optional)**
   - Click "Add bypass" to specify roles, teams, or apps that can bypass these rules
   - For most cases, leave this empty to ensure maximum protection

4. **Configure Target Branches**
   - Click "Add target" to specify which branches should be protected
   - Enter `main` to protect your main branch
   - You can also use patterns like `release/*` to protect all release branches

5. **Configure Branch Rules**
   - Under the "Rules" section, select the protection rules you want to apply:

   **Essential rules to enable:**
   - ☑️ **Restrict deletions**: Prevent deletion of matching refs
   - ☑️ **Block force pushes**: Prevent users with push access from force pushing
   - ☑️ **Require a pull request before merging**: Require all commits be made to a non-target branch and submitted via a PR
   - ☑️ **Require status checks to pass**: This is critical for requiring tests to pass

     **Important**: When you first enable this option:
     - You'll see "No required checks" or "No checks have been added"
     - Click "Add checks" to see available status checks
     - If "Notebook Tests" doesn't appear in the list, you need to:
       1. Push your code with the workflow file to GitHub
       2. Run the workflow at least once (via push or manual trigger)
       3. Return to this settings page after the workflow has run
       4. Then "Notebook Tests" will appear as an available status check

     **Additional status check options:**
     - Check "Require branches to be up to date before merging" to ensure PRs include the latest code
     - You can also manually type a status check name if you know it, even if it hasn't run yet
     - Consider checking "Hide additional settings" to see more options

   **Additional rules to consider:**
   - ☐ **Restrict creations**: Only allow users with bypass permission to create matching refs
   - ☐ **Restrict updates**: Only allow users with bypass permission to update matching refs
   - ☐ **Require linear history**: Prevent merge commits from being pushed
   - ☐ **Require deployments to succeed**: Choose environments that must be successfully deployed
   - ☐ **Require signed commits**: Commits pushed must have verified signatures
   - ☐ **Require code scanning results**: Enable code scanning checks (if using GitHub Advanced Security)

6. **Save the Ruleset**
   - Click "Create" at the bottom of the page to save and activate your ruleset


### What This Accomplishes

- ✅ **Automated Testing**: All pull requests run the "Notebook Tests" workflow
- ✅ **Quality Gate**: PRs cannot be merged until tests pass
- ✅ **Up-to-Date Code**: Ensures branches are current before merging
- ✅ **Code Review**: Requires approval from designated experts
- ✅ **Protection**: Prevents direct pushes, force pushes, and branch deletions
- ✅ **Granular Control**: Fine-grained permissions for who can bypass rules
- ✅ **Enhanced Security**: More comprehensive protection options

This ensures your notebook repository maintains high-quality, functional notebooks that execute correctly across all changes.

### Tag Rulesets (Optional)

For repositories that use versioning with tags (e.g., v1.0.0, v2.1.0), you can also create a Tag ruleset:

1. Follow the same process as above, but select **"Tag ruleset"** instead of "Branch ruleset"
2. Configure the tag pattern to protect (e.g., `v*` to protect all version tags)
3. Enable rules like:
   - **Require signed tags**: Ensures tags are cryptographically signed
   - **Block tag deletions**: Prevents removal of released versions
   - **Block tag creations**: Limits who can create official version tags
   - **Require status checks**: Ensures tags are only created on validated code

Tag rulesets are especially useful for repositories where releases are created from tags, ensuring that only properly tested and approved code gets released.
