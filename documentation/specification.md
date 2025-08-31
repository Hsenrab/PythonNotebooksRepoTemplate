# Python Notebooks Repository Template - Specification

## Overview

This project aims to create a simple, educational repository template that demonstrates best practices for creating and maintaining Jupyter notebooks intended for sharing with others. The template serves as a learning resource for notebook creators who need to ensure their content remains functional, professional, and up-to-date for external consumption.

## Goals

1. **Shareable Quality**: Provide patterns for creating notebooks that maintain professional standards
2. **Maintainability**: Demonstrate practices that keep shared notebooks functional over time
3. **Collaboration Ready**: Showcase approaches that work well in team environments
4. **Template Reusability**: Create a foundation that can be easily copied and adapted for different sharing scenarios

## Requirements

### Functional Requirements

#### Authentication
- ✅ **Implemented**: Azure authentication using `azure_auth_helper.py` module
- ✅ **User-based authentication**: Leverages Azure Identity library with user permissions (no API keys)
- ✅ **Multiple auth methods**: Browser authentication and device code authentication
- ✅ **Credential caching**: Uses DefaultAzureCredential for existing token reuse
- ✅ **Service Usage**: No Azure services in initial examples, only basic chat with Azure AI Foundry SDK and OpenAI model after authentication
- Demonstrate secure credential management through environment variables
- Show integration with Azure AI Foundry services

#### Environment Management
- Create `.env` file structure for environment variables
- Demonstrate separation of configuration from code
- Show secure handling of sensitive information

#### Python Virtual Environment
- ✅ **Package Selection**: Absolute minimum packages - only essential tools plus most recent stable Azure SDKs
- Provide virtual environment configuration using venv and requirements.txt
- Include essential packages for data science workflows plus Azure SDK components
- Include testing tools: pytest, nbmake
- Ensure reproducible environment setup across different machines

#### Notebook Cleaning
- Implement automated notebook cleaning using nbconvert
- Set up git hooks to clean notebooks before commits
- Remove output cells and metadata automatically

#### Notebook Testing
- ✅ **Framework Selected**: Use pytest with nbmake for notebook execution testing
- ✅ **Complexity Level**: Minimal complexity - single-purpose notebooks focusing on one concept each
- ✅ **Documentation Style**: Thorough topic coverage in labeled blocks, minimal repetition, brief inline comments
- ✅ **CI Strategy**: Initial implementation excludes Azure authentication, add Azure authentication testing to GitHub Actions when auth phase is implemented
- Demonstrate automated notebook execution and validation
- Show how to test notebook execution end-to-end
- Include examples of data validation and assertion patterns within notebooks
- Set up GitHub Actions workflow for continuous integration

### Non-Functional Requirements

- **Simplicity**: Code should be self-explanatory with minimal documentation
- **Educational Value**: Each component should clearly demonstrate a specific best practice
- **Minimal Complexity**: Notebooks should be single-purpose, linear flow, readable in under 5 minutes
- **Documentation Strategy**: Comprehensive explanations in labeled markdown blocks, avoid repetition, use brief inline comments for code clarity
- **No Error Handling**: Skip complex error handling to keep focus on core concepts
- **No Backwards Compatibility**: Use modern Python and package versions only
- **Clean Code**: Prioritize readability and clarity over robustness

## Assumptions

1. **Target Audience**: Notebook creators who need to share content with colleagues, students, or clients
2. **Use Case**: Creating notebooks for others to consume, not just personal analysis
3. **Quality Standards**: Professional-grade notebooks that reflect well on the creator
4. **Collaboration**: Multiple people may contribute to or consume the notebooks
5. **Environment**: Users have conda/miniconda installed
6. **Git Knowledge**: Users understand basic git workflows
7. **Platform**: Primary development on Windows (based on file paths), but should work cross-platform
8. **Python Version**: Python 3.12 will be used
9. **Maintenance Context**: Notebooks need to remain functional and current over time
10. **Testing Approach**: pytest + nbmake for local testing, GitHub Actions for CI

## Open Questions

1. ~~**Testing Framework**: Should we use pytest, unittest, or demonstrate multiple approaches?~~ ✅ **Resolved**: pytest with nbmake
2. ~~**Notebook Complexity**: How complex should the example notebooks be to effectively demonstrate concepts?~~ ✅ **Resolved**: Minimal complexity - single-purpose notebooks with linear flow, simple data operations, readable in under 5 minutes
3. ~~**Documentation Level**: What level of inline documentation strikes the right balance between clarity and conciseness?~~ ✅ **Resolved**: Thorough topic coverage in labeled blocks, avoid repetition, brief inline comments only
4. ~~**Package Selection**: Which specific packages should be included in the conda environment beyond the basics and Azure SDK?~~ ✅ **Resolved**: Absolute minimum - essential tools only, most recent stable Azure SDK versions
5. ~~**Azure Services**: Which specific Azure AI Foundry services should be demonstrated in example notebooks?~~ ✅ **Resolved**: No Azure services in initial examples, only basic chat with Azure AI Foundry SDK and OpenAI model after authentication
6. ~~**GitHub Actions**: Should authentication testing be included in CI, or only notebook execution without Azure calls?~~ ✅ **Resolved**: Initial implementation excludes Azure authentication, add Azure authentication testing to GitHub Actions when implementing auth phase

**🎉 All Open Questions Resolved - Specification Complete**

## Step-by-Step Plan

### Phase 1: Repository Structure Setup ✅

1. ✅ Create basic directory structure including `tests/` folder
2. ✅ Initialize git repository with appropriate .gitignore
3. ✅ Set up README.md with clear project description and usage instructions

### Phase 2: Environment Configuration ✅

1. ✅ Create `requirements.txt` file for pip/venv environment
2. ✅ Include essential data science packages (pandas, numpy, jupyter, etc.)
3. ✅ Add development tools (nbconvert, pre-commit, pytest, nbmake)
4. ✅ **Exclude Azure packages initially**
5. ✅ Switch from conda to venv for lighter, faster setup

### Phase 3: Environment Variables Setup (Non-Azure) ✅
1. ✅ Create `.env.template` file for general environment variables
2. ✅ Add `.env` to .gitignore
3. ✅ Demonstrate environment variable patterns without Azure credentials
4. ✅ Show inline environment variable loading in notebooks (no helper functions)

### Phase 4: Git Hooks and Notebook Cleaning ✅
1. ✅ Set up pre-commit hooks configuration
2. ✅ Configure nbconvert for automatic notebook cleaning
3. ✅ Create git hook scripts to clean notebooks before commits
4. ✅ Test the cleaning process with sample notebooks
5. ✅ Add setup scripts for both Windows and Unix systems

### Phase 5: Basic Notebook Testing Implementation ✅

1. ✅ Set up pytest configuration for notebook testing
2. ✅ Configure nbmake for automated notebook execution
3. ✅ Create simple example notebooks to test (no Azure authentication needed)
4. ✅ Demonstrate data validation and assertion patterns

### Phase 6: GitHub Actions Setup (Basic)
1. Create `.github/workflows/` directory
2. Set up CI workflow for automated testing
3. Configure workflow to run pytest + nbmake on non-Azure notebooks
4. **Exclude Azure authentication testing initially**

### Phase 7: Azure Authentication Integration

1. Add Azure Identity and Azure AI Foundry packages to requirements.txt
2. Update `.env.template` to include AZURE_TENANT_ID
3. ✅ **Already Implemented**: Azure authentication helper module
4. Create example notebook demonstrating Azure authentication usage
5. Show basic chat example with Azure AI Foundry SDK and OpenAI model

### Phase 8: GitHub Actions Azure Integration

1. Update CI workflow to include Azure authentication testing
2. Configure GitHub secrets for Azure credentials (AZURE_TENANT_ID, etc.)
3. Add Azure authentication notebooks to CI testing
4. Demonstrate secure credential handling in CI environment

### Phase 9: Documentation and Final Polish

1. Update README with complete setup instructions including Azure components
2. Add testing section explaining pytest + nbmake usage for both basic and Azure notebooks
3. Document GitHub Actions workflow including Azure authentication
4. Add inline documentation to code examples
5. Create usage examples and common workflows
6. Ensure all components work together seamlessly

### Phase 10: Testing and Validation

1. Test complete setup process on clean environment
2. Validate all git hooks function correctly
3. Ensure notebooks execute properly after cleaning
4. Verify pytest + nbmake works locally for all notebook types
5. Test GitHub Actions workflow execution with and without Azure authentication
6. Verify authentication examples work with real Azure tenant

## Success Criteria

- Repository can be cloned and set up in under 5 minutes
- Azure authentication works seamlessly across all example notebooks
- All example notebooks execute successfully in the conda environment
- Git hooks automatically clean notebooks without user intervention
- pytest + nbmake successfully tests all notebooks locally
- GitHub Actions workflow runs successfully on push/PR
- Authentication patterns are clearly demonstrated and easily adaptable
- No API keys are required - all authentication uses user permissions
- Code remains simple and educational throughout the repository
- CI pipeline provides clear feedback on notebook execution status
