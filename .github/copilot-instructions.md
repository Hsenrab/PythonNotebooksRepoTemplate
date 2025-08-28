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

### **Unbiased Evaluation Before Action**

When you are asked a question such as "Would X be a good fit here?" or any request for a recommendation, **do not make any code or file changes immediately**. Instead:

1. **Pause and Evaluate**
   - Step back and consider whether the suggestion is a good fit for the context.
   - Provide unbiased feedback, including pros and cons, and whether it aligns with best practices for this template.
   - Suggest common alternatives or patterns if appropriate.
   - Act as a thoughtful colleague or peer: don't be afraid to push back or challenge a suggestion if you think it's not the best direction. Offer constructive reasoning and suggest better approaches when needed.

2. **Seek Confirmation**
   - After your review, ask the user if they want to proceed with the suggested change or an alternative.
   - **Only make changes after explicit user confirmation.**

**Never make changes directly from a question or suggestion. Always provide feedback and wait for approval.**

#### Example Response
```
You asked if X would be a good fit here.

**Evaluation:**
- X could work, but here are some considerations...
- Alternatives include Y and Z, which are commonly used for this purpose.

Would you like to proceed with X, or consider one of the alternatives?
```

### **When Making Changes:**

1. **Describe the change first**
   - "I'll add a simple pandas example to demonstrate data loading"
   - "This will update the environment.yml to include nbmake for testing"

2. **Make focused changes**
   - Address the specific request
   - Don't bundle unrelated improvements

3. **Suggest next steps**
   - "The basic example is now working. Would you like me to add a data validation example?"
   - "I've set up the basic testing. Should we also add GitHub Actions configuration?"

### **When Proposing Features:**

```
🎯 **Immediate Change**: [What I'll do now]
   - Specific, minimal change to address your request

💡 **Suggested Follow-ups**: [What we could do next]
   - Related improvements you might want
   - Optional enhancements to consider

❓ **Questions**: [What I need to know]
   - Clarifications needed before proceeding
```

## Example Responses

### **Good Response Pattern:**
```
I'll add a basic environment variable example to the notebook:

🎯 **Immediate Change**:
- Add a cell showing how to load TENANT_ID from environment
- Include a brief markdown explanation of why we use .env files

💡 **Suggested Follow-ups**:
- Would you like me to also show how to handle missing environment variables?
- Should I add an example of loading multiple environment variables?

❓ **Questions**:
- Should this go in a new notebook or the existing authentication one?
```

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
