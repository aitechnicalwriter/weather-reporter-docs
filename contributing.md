# Contributing to Weather Reporter

Thank you for your interest in improving this project! This guide will help you get started.

## Development Workflow

To maintain a clean and professional environment, please follow these steps:

1. **Branching**: Create a descriptive feature branch for any changes.
   ```bash
   git checkout -b feat/your-feature-name

2. **Virtual Environment**: Always use the provided `venv` setup to ensure dependency consistency.

3. **Coding Standards**: Follow [PEP 8](https://peps.python.org/pep-0008/) style guidelines for all Python code.

## Potential Enhancements

We welcome pull requests for the following features:
* **Unit Selection**: Adding the ability to toggle between Metric (Celsius) and Imperial (Fahrenheit).
* **Extended Forecast**: Integrating the 5-day forecast endpoint from OpenWeatherMap.
* **Robust Error Handling**: Implementing specific exceptions for common API issues like `401 Unauthorized` (invalid key) or `429 Too Many Requests`.

## Documentation Requirements

Any code changes must be accompanied by updates to:
* `api-reference.md` (if data structures change)
* Docstrings within `main.py`
* The "Quick Start" section of the `README.md`