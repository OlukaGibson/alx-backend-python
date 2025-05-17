# Python Generators – 0x00

This project explores Python generators and how they can be used to efficiently stream and process large datasets, especially with SQL databases.

## Environment

- Python 3.x
- MySQL Database (via a `seed.py` module with `connect_to_prodev()` function)
- Virtual environment (recommended)

---

## Files

### 0. Stream Users

**File:** `0-stream_users.py`  
**Function:** `stream_users()`  
**Description:**  
Streams users one by one from the `user_data` table using a generator. Efficient for iterating over large datasets.

**Usage Example:**
```bash
./1-main.py
