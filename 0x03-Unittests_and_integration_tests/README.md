0x03. Unittests and Integration Tests
ALX Backend Specialization — Python

📚 Project Overview
This project focuses on writing unit tests and integration tests for Python functions and classes. The goal is to ensure code correctness using mocking, parameterization, and fixtures.

You’ll work with utility functions and a GitHub API client to build robust and well-tested Python codebases.

🔧 Learning Objectives
By the end of this project, you should be able to:

Understand the difference between unit and integration tests

Write unit tests using unittest and parameterized

Use patch, Mock, and PropertyMock from unittest.mock to isolate test cases

Create fixtures for integration testing

Mock external APIs safely and effectively

Apply test-driven development techniques

📁 Project Structure
bash
Copy
Edit
.
├── client.py             # GitHubOrgClient class implementation
├── utils.py              # Utility functions: access_nested_map, get_json, memoize
├── fixtures.py           # JSON payloads for integration tests
└── tests/
    ├── __init__.py
    ├── test_client.py    # Unit and integration tests for client.py
    └── test_utils.py     # Unit tests for utils.py
✅ How to Run the Tests
Make sure you have parameterized installed:

bash
Copy
Edit
pip install parameterized
Then run the tests using:

bash
Copy
Edit
python3 -m unittest discover tests
📌 Key Concepts Covered
Unit Testing: Testing functions/methods in isolation.

Integration Testing: Testing how components work together.

Mocking: Faking external systems like APIs or methods to focus on test logic.

Memoization: Caching results to avoid recomputation.

Fixtures: Static test data to simulate API responses.

🧪 Example Features Tested
From utils.py:
access_nested_map() – safely accessing nested dictionary keys

get_json() – making and mocking HTTP GET requests

memoize – caching function output

From client.py:
GithubOrgClient:

.org – fetch organization info

.public_repos() – list public repositories

.has_license() – check for a specific license type

🧠 Author
Gibson Oluka
🔗 LinkedIn
💡 Backend Developer | Embedded Systems | DevOps Enthusiast

📝 License
This project is part of the ALX Backend Curriculum and is intended for educational purposes.