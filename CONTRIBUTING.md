# Contributing to z/OS Machine Learning Transaction Analyzer

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code follows our coding standards.
6. Issue that pull request!

## Development Environment Setup

1. Ensure you have Python 3.9+ installed
2. Clone the repository:
   ```bash
   git clone <repository-url>
   cd zos-ml-demo
   ```
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Unix/macOS
   venv\Scripts\activate     # On Windows
   ```
4. Install the package in development mode:
   ```bash
   pip install -e .
   ```

## Testing

We use pytest for testing. Run the tests with:
```bash
pytest tests/
```

For coverage report:
```bash
pytest --cov=./ --cov-report=xml
```

## Code Quality

### Automated Checks
All code must pass:
- pytest test suite
- flake8 linting
- Bandit security scanning
- CodeQL analysis

### Python Code Style
- Follow PEP 8
- Use type hints
- Document all functions and classes
- Keep functions focused and small
- Add docstrings to all public functions and classes

## z/OS-Specific Guidelines

### 1. Subsystem Integration
When contributing code that interacts with z/OS subsystems:
- Ensure RACF permissions are properly checked
- Follow IBM's coding standards for subsystem interfaces
- Document any required APF authorizations
- Include appropriate error handling for system services

### 2. Performance Considerations
- Consider WLM implications
- Document resource requirements
- Include performance test results
- Consider Parallel Sysplex impacts

### 3. Security Standards
- Follow z/OS security best practices
- Document required security configurations
- Include RACF resource definitions
- Consider audit requirements
- Run Bandit security scans locally before submitting

## Package Structure

When adding new code, follow our package structure:
```
zos_ml_demo/
├── __init__.py
├── ml_model.py
└── utils/
    ├── __init__.py
    ├── zos_monitoring.py
    ├── zos_performance_analyzer.py
    ├── zos_security_manager.py
    └── ...
```

## Documentation

### Code Documentation
- Add docstrings to all public functions and classes
- Include type hints
- Document exceptions and return values
- Add examples for complex functionality

### Project Documentation
When making significant changes:
1. Update README.md
2. Update relevant documentation in /docs
3. Add migration guides if needed
4. Update CHANGELOG.md

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the CHANGELOG.md with a note describing your changes
3. The PR will be merged once you have the sign-off of at least one maintainer

## Getting Help

If you need help, you can:
1. Open an issue with a detailed description
2. Tag maintainers in your PR for review
3. Ask questions in the discussions section

## Community Guidelines

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Share knowledge freely

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md
- Release notes
- Project documentation

## Questions?

Feel free to contact the maintainers for any questions about contributing.

## License

By contributing, you agree that your contributions will be licensed under the project's MIT License.
