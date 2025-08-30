# Copilot Agent Instructions for Python Notebooks Repository

## Project Overview

This repository demonstrates best practices for creating and maintaining shareable Jupyter notebooks. The target audience is **notebook creators** who need to share professional-quality content with colleagues, students, or clients.

## Core Principles

### 🎯 **Educational Focus**
- Demonstrate one concept clearly per file/notebook
- Prioritize clarity and understanding over completeness
- Keep examples simple and focused

### 🧹 **Simplicity First**
- **No error handling** - skip try/catch blocks to focus on core concepts
- **No backwards compatibility** - use modern Python 3.12+ features
- **Minimal dependencies** - only essential packages
- **Clean code** - readable over robust
- **Fresh updates** - when refreshing examples, assume everyone updates together (no legacy support needed)

### 📦 **Scoped Changes**
- Make **minimal, focused changes** per request
- Suggest follow-up improvements rather than implementing everything at once
- Ask for confirmation before making significant structural changes

## When Assisting with Code Changes

### ✅ **DO:**

1. **Stay Minimal**
   ```python
   # Good: Simple, focused example
   import pandas as pd
   df = pd.read_csv('data.csv')
   print(df.head())
   ```

2. **Suggest, Don't Assume**
   - "I can add X feature. Should I also include Y?"
   - "This change addresses your request. Would you like me to also update Z?"

3. **Keep Educational Value**
   - Add brief comments explaining WHY, not just HOW
   - Include markdown explanations in notebooks
   - Focus on demonstrating best practices

4. **Respect the Template Nature**
   - Remember this is a template others will copy
   - Keep examples generic and adaptable
   - Avoid project-specific implementations

### ❌ **DON'T:**

1. **Don't Add Complexity**
   ```python
   # Avoid: Complex error handling
   try:
       df = pd.read_csv('data.csv')
   except FileNotFoundError:
       logging.error("File not found")
       raise CustomException("Data file missing")
   except Exception as e:
       # ... complex error handling
   ```

2. **Don't Maintain Legacy Support**
   ```python
   # Avoid: Backwards compatibility patterns
   try:
       # New pandas syntax
       df = pd.read_csv('data.csv', engine='pyarrow')
   except:
       # Fallback for older pandas versions
       df = pd.read_csv('data.csv')
   ```

3. **Don't Make Assumptions**
   - Don't add features not explicitly requested
   - Don't refactor code unless asked
   - Don't change the overall structure without permission

4. **Don't Over-Engineer**
   - No custom classes unless demonstrating a specific concept
   - No complex configuration systems
   - No production-grade patterns

## File-Specific Guidelines

### **Notebooks (*.ipynb)**
- **One concept per notebook** - authentication, testing, environment setup, etc.
- **Linear flow** - no complex branching or optional sections
- **Thorough explanations** in markdown blocks at the start of each section
- **Brief inline comments** for code clarity
- **No outputs saved** - notebooks should be clean for sharing

### **Python Modules (*.py)**
- **Single purpose** - one clear responsibility per module
- **Minimal functions** - demonstrate patterns, not comprehensive solutions
- **Clear docstrings** - explain purpose and usage
- **No defensive programming** - keep code clean and simple

### **Configuration Files**
- **Essential only** - minimal package lists, basic configurations
- **Well-commented** - explain why each setting exists
- **Template-ready** - easy for others to adapt
- **Latest versions** - use current stable releases, no version pinning for backwards compatibility

## Interaction Patterns

### 1. **Direct Instruction**
If the user gives a direct request (“Do X”, “Add Y”), then:

- **Clarify if needed**: Ask for specifics if anything is ambiguous.
- **Briefly describe your planned change** before implementing.
- **Make the minimal, focused change** in line with the guidelines.
- **Return for user confirmation**: “Is this what you were looking for?”
- **Suggest follow-ups if appropriate**, but do not implement unless requested.

### 2. **Exploratory or Recommendation Question**
If asked for a suggestion or opinion (“Would X be a good fit?”):

- **Pause and evaluate** the proposal.
- **Provide unbiased feedback**:
    - List pros and cons.
    - Note alignment (or not) with the repo’s educational/template focus.
    - Suggest common alternatives if appropriate.
- **Ask for confirmation** before making any change.
- **Never implement from a question—wait for explicit approval.**

#### Example Response
```
You asked if X would be a good fit here.

**Evaluation:**
- X could work, but here are some considerations...
- Alternatives include Y and Z, which are commonly used for this purpose.

Would you like to proceed with X, or would you prefer one of the alternatives?
```

### 3. **To-Do or Spec-Driven**
If following a checklist or external spec:
- **Describe the next step** and confirm it’s correct before proceeding.
- Follow the **Direct Instruction** pattern from there.

---


### **Avoid This Pattern:**
```
I'll add comprehensive environment variable handling with error checking,
validation, default values, logging, and integration with multiple
configuration sources. I'll also update all existing notebooks to use
this new system and add unit tests.
```

## Quality Checks

Before suggesting any change, ask:

1. **Is this change minimal and focused?**
2. **Does it maintain educational clarity?**
3. **Will this be useful for someone copying this template?**
4. **Am I avoiding unnecessary complexity?**
5. **Have I explained WHY, not just HOW?**
6. **Am I using modern Python/package features without legacy fallbacks?**

## Success Metrics

The repository succeeds when:
- Someone can clone it and understand the concepts in 5 minutes
- The examples are immediately adaptable to their use case
- The code demonstrates clear best practices without distraction
- Each component serves a specific educational purpose

Remember: **This is a teaching tool, not a production system.**
