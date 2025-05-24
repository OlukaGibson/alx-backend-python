# Python Decorators Project

This project demonstrates the use of Python decorators to handle:

- Logging SQL queries
- Managing database connections
- Ensuring transaction integrity
- Retrying failed operations
- Caching SQL query results

## Files

| File                   | Description                                |
|------------------------|--------------------------------------------|
| `0-log_queries.py`     | Logs SQL queries before execution          |
| `1-with_db_connection.py` | Adds DB connection and closes it safely  |
| `2-transactional.py`   | Ensures commit/rollback behavior           |
| `3-retry_on_failure.py`| Retries DB operations on failure           |
| `4-cache_query.py`     | Caches results of identical queries        |

## Setup

```bash
python3 setup_database.py
python3 0-log_queries.py
