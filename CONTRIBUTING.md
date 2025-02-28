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

## Code Style Guidelines

### Python Code Style
- Follow PEP 8
- Use type hints
- Document all functions and classes
- Keep functions focused and small

### JCL Standards
- Use standard JCL conventions
- Document all JCL parameters
- Include sample PROC modifications
- Follow naming conventions

## Testing Guidelines

### Unit Tests
- Write unit tests for all new code
- Include z/OS-specific test cases
- Mock subsystem interfaces appropriately
- Test error conditions

### Integration Tests
- Test subsystem integration
- Verify RACF interactions
- Test performance metrics
- Validate monitoring capabilities

## Documentation Requirements

### Code Documentation
- Clear function descriptions
- Parameter documentation
- Return value documentation
- Usage examples

### System Documentation
- Installation requirements
- Configuration details
- Performance implications
- Security requirements

## Issue Reporting Process

1. Use the issue tracker
2. Include reproduction steps
3. List system configuration
4. Attach relevant logs

## Pull Request Process

1. Update documentation
2. Update CHANGELOG.md
3. Update test cases
4. Get review from maintainers

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
