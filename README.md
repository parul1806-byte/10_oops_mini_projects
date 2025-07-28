# 10_oops_mini_projects
1.Chat-Room-Encryption-OOP
# 🛡️ Chat Room Encryption using Python (OOP + Caesar Cipher)

This is a simple Python project that simulates a basic chat room where users can send encrypted messages using the **Caesar Cipher** technique. It demonstrates **Object-Oriented Programming (OOP)** concepts like classes, inheritance, and abstraction.

---

## 💡 Features

- 🧑‍💻 User class to represent chat users
- 📨 Message class to store encrypted messages
- 🔐 CaesarEncryptor to encrypt/decrypt messages
- 💬 ChatRoom to send, store, and display conversation
- 🕵️ Decryption of messages during viewing
- 👀 View both encrypted and decrypted messages

---

## 🔧 Technologies Used

- 🐍 Python 3.x
- OOP concepts: Inheritance, Encapsulation, Abstraction
- Caesar Cipher for basic encryption

---

## 📂 Folder Structure

Chat-Room-Encryption-OOP/
│
├── ChatRoomEncryption.py # Main Python file
├── README.md # Project description
└── requirements.txt # (Optional) dependencies


#2 🏦 Bank Account System with Context Manager

This Python project demonstrates a simple **bank account system** that supports secure money transactions using **context managers** to simulate rollback functionality in case of errors or exceptions.

---

## 🚀 Features

- Create bank accounts with initial balances
- Deposit and withdraw money
- Transfer funds between accounts
- Simulate real-life transaction rollback using `with` and context managers
- Exception handling with balance recovery
- Warning for insufficient funds

---

## 📂 Project Structure
bank_account_context_manager/
├── bank_system.py # 💻 Main code
├── README.md # 📘 Project explanation

## 🧠 How It Works

### ✅ Context Manager (`with` statement)
When a transaction is started using `with account:`, the system:
- Saves the original balance
- Tries to perform the transaction
- If any error occurs, it **rolls back** the balance to the original amount

---

### 💸 Example

```python
with acc1:
    acc1.transfer_to(acc2, 800)
    raise Exception("Simulated crash")
➡️ Transaction Started for riya 
✅₹800: Has been withdraw from riya
✅₹800: Has been deposited
💸 Transferring ₹800 from riya to raj....
❌ERROR! Rolling back:riya's balance to ₹8000







