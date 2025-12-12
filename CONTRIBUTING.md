# Contributing to Library Management System

Thank you for your interest in contributing to the Library Management System! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

This project adheres to the Contributor Covenant Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find one already created. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps** which reproduce the problem
- **Provide specific examples** to demonstrate the steps
- **Describe the behavior you observed** after following the steps
- **Explain which behavior you expected** to see instead and why
- **Include screenshots and animated GIFs** if possible
- **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description** of the suggested enhancement
- **Provide specific examples** to demonstrate the steps
- **Describe the current behavior** and explain the expected behavior
- **Explain why this enhancement would be useful**

## Pull Request Process

1. **Fork the Repository**: Click the Fork button on GitHub
2. **Create a Branch**: `git checkout -b feature/your-feature-name`
3. **Make Changes**: Write clean, well-documented code
4. **Follow Style Guide**: Ensure your code follows PEP 8
5. **Add Tests**: Write tests for new features
6. **Update Documentation**: Update README and docstrings as needed
7. **Commit Changes**: Use clear, descriptive commit messages
8. **Push to GitHub**: `git push origin feature/your-feature-name`
9. **Open Pull Request**: Submit PR with detailed description
10. **Respond to Feedback**: Work with maintainers to address any concerns

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/library-management-system.git
cd library-management-system

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install pytest pytest-cov flake8

# Run tests
pytest tests/ -v

# Run linting
flake8 src/
```

## Code Style Guidelines

- Follow PEP 8 style guide
- Use meaningful variable names
- Write docstrings for all functions and classes
- Keep lines under 80 characters when possible
- Use type hints for function parameters and returns
- Write clear commit messages in present tense

## Testing Guidelines

- Write tests for all new features
- Maintain or improve code coverage
- Use descriptive test function names
- Test both successful and error cases
- Run all tests before submitting PR

## Commit Message Convention

Follow conventional commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types:
- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that don't affect code meaning
- **refactor**: Code change that neither fixes a bug nor adds a feature
- **test**: Adding missing tests or correcting existing tests
- **chore**: Changes to build process, dependencies, etc.

## Questions?

Feel free to open an issue labeled 'question' or reach out to the maintainers.

## License

By contributing to this project, you agree that your contributions will be licensed under its MIT License.

Thank you for contributing to Library Management System!
