# Python Bank & ATM System (v2)

An object-oriented banking and ATM simulation built in Python with persistent JSON storage.

## What's New in v2
- **JSON Database Persistence:** Replaced temporary in-memory variables with an `accounts.json` file so balances and transaction histories save automatically between runs.
- **Multi-User Support:** Supports multiple customer accounts, each verified by their own 4-digit PIN.
- **Object-Oriented Composition:** Separated responsibilities across four classes instead of keeping everything in one script.

## Project Structure
- `bank.py` — Contains the core classes and demo script:
  - **`BankDatabase`**: Handles reading from and saving to `accounts.json`.
  - **`Bank`**: Manages core banking logic (`withdraw`, `deposit`, `check_balance`, `info`, and `transaction_history`).
  - **`DebitCard`**: Connects to `Bank` via composition to process card payments.
  - **`ATM`**: Provides the customer-facing interface for account operations.
- `accounts.json` — Stores customer profiles, PINs, account numbers, wallet balances, and transaction logs.

## How to Run
1. Make sure `bank.py` and `accounts.json` are in the same folder.
2. Run the script:
   ```bash
   python bank.py
   ```
