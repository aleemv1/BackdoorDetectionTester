# Backdoor Detection Tester

This project uses CodeQL to analyze Python code for potential backdoors and security vulnerabilities.

## Prerequisites

1. Install CodeQL CLI:
   ```bash
   # For macOS (using Homebrew)
   brew install codeql
   ```

2. Install Python dependencies:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

## CodeQL Analysis Setup

1. Create a CodeQL database:
   ```bash
   # Create a new database (excludes venv directory)
   codeql database create codeql-db --language=python --source-root . --overwrite
   ```

2. Run security queries:
   ```bash
   # Run all security queries
   codeql database analyze python-db codeql/python-queries --format=sarifv2.1.0 --output=results.sarif
   ```
   Results can be found in results.sarif



## Querying LLMs
1. Make sure you add secrets in .env file

2. Run main.py
 ```bash
   python3 main.py
   ```