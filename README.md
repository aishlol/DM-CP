# 🔐 CipherShield
### Smart Digital Protection Through Mathematical Cryptography

**CipherShield** is a Python-based digital file protection application that demonstrates the practical application of Discrete Mathematics in modern cryptography.

The project combines secure file encryption, file integrity verification and an interactive mathematical laboratory to demonstrate how mathematical concepts such as prime numbers, GCD, modular arithmetic, mathematical functions and propositional logic are used in information security.

---

## 📌 Project Overview

In today's digital world, documents, academic records, financial statements and personal files are stored electronically. These files are vulnerable to unauthorized access, data theft and unwanted modifications.

CipherShield aims to address these challenges using cryptographic techniques and mathematical principles.

The project consists of two main modules:

1. **Secure File Protection:** Protects files using AES-256-GCM encryption and SHA-256 integrity verification.
2. **Discrete Mathematics Lab:** Demonstrates prime number verification, GCD, modular arithmetic and RSA cryptography using educational examples.

---

## 🎯 Problem Statement

Digital files face several security challenges:

- **Unauthorized Access:** Files stored on shared or lost devices can be accessed by unauthorized users.
- **Data Theft:** Sensitive information can be copied or leaked.
- **Silent Modification:** Files may be altered without users immediately noticing the changes.

CipherShield demonstrates how mathematical cryptography can help protect digital information and verify file integrity.

---

## ✨ Project Objectives

- Develop a Python-based application for secure file encryption and decryption.
- Implement AES-256-GCM authenticated encryption.
- Implement SHA-256 hashing for file integrity verification.
- Demonstrate RSA cryptography using Number Theory.
- Implement prime number verification, GCD and modular arithmetic.
- Demonstrate practical applications of Discrete Mathematics in digital security.
- Provide a simple graphical user interface.

---

## 🚀 Key Features

### 1. Secure File Protection

- File selection and validation.
- AES-256-GCM file encryption.
- Secure file decryption.
- Detection of incorrect encryption keys.
- Detection of modified encrypted data.
- SHA-256 hash generation.
- File integrity verification.

### 2. Discrete Mathematics Laboratory

| Feature | Description |
|---|---|
| Prime Number Check | Checks whether a number is prime |
| GCD Calculator | Calculates Greatest Common Divisor |
| Euclidean Algorithm | Finds GCD using repeated division |
| Modular Arithmetic | Performs arithmetic operations under modulo |
| Modular Inverse | Calculates modular multiplicative inverse |
| RSA Demonstration | Demonstrates RSA key generation, encryption and decryption |

---

## 🏗️ System Architecture

```text
                 USER
                   |
                   v
          GRAPHICAL USER INTERFACE
                   |
             +-----+-----+
             |           |
             v           v
        FILE SECURITY  MATH LAB
             |           |
       +-----+-----+     |
       |     |     |     |
       v     v     v     v
     AES   AES   SHA-256 PRIME
   ENCRYPT DECRYPT  HASH  GCD
                         MODULAR
                         ARITHMETIC
                         RSA DEMO
       |     |     |     |
       +-----+-----+     |
             |           |
             v           v
       SECURE FILE     RESULT
        STORAGE        DISPLAY
```

### Architecture Modules

- **User Interface:** Allows users to interact with the application.
- **File Security:** Handles encryption, decryption and integrity verification.
- **Math Lab:** Performs mathematical operations and RSA demonstrations.
- **Secure File Storage:** Stores encrypted files locally.
- **Result Display:** Displays operation status and verification results.

**Note:** The Math Lab is an educational module. Actual file encryption is performed using the cryptography library.

---

## 🧮 Discrete Mathematics Concepts Used

CipherShield demonstrates the practical application of the following concepts:

| Discrete Mathematics Concept | Application |
|---|---|
| Number Theory | Foundation of RSA cryptography |
| Prime Numbers | RSA key construction |
| GCD | Selecting valid RSA public exponent |
| Euclidean Algorithm | GCD calculation |
| Modular Arithmetic | RSA encryption and decryption |
| Modular Multiplicative Inverse | Calculating RSA private exponent |
| Mathematical Functions | Encryption and decryption mappings |
| Propositional Logic | Security and verification conditions |
| Hash Functions | SHA-256 integrity verification |
| Finite Fields | Mathematical operations underlying AES and GCM |

### Mathematical Representation

**1. Encryption**

Eₖ(P) = C

Where:
- P = Plaintext
- C = Ciphertext
- k = Secret key

**2. Decryption**

Dₖ(C) = P

**3. SHA-256 Hash Function**

H: {0,1}* → {0,1}²⁵⁶

SHA-256 generates a fixed-length 256-bit hash value.

**4. Security Condition**

Access = F ∧ K ∧ T

Where:
- F = File is valid.
- K = Correct key is provided.
- T = GCM authentication tag is valid.

---

## 🔑 RSA Cryptography Demonstration

CipherShield demonstrates RSA using small educational values.

### Example

```text
p = 5
q = 11

n = p × q
n = 55

φ(n) = (p - 1)(q - 1)
φ(n) = 40

e = 3
gcd(3, 40) = 1

d = 27

Public Key  = (55, 3)
Private Key = (55, 27)

Message = 7

Encryption:
C = 7³ mod 55
C = 13

Decryption:
M = 13²⁷ mod 55
M = 7
```

This example demonstrates the relationship between prime numbers, Euler's Totient Function, GCD and modular multiplicative inverses.

**Important:** RSA is used only for educational mathematical demonstration. AES-256-GCM performs the actual file encryption.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.x | Main programming language |
| CustomTkinter | Graphical user interface |
| Cryptography | AES-256-GCM encryption and decryption |
| Hashlib | SHA-256 hash generation |
| SQLite (Optional) | File metadata storage |
| VS Code | Development environment |

---

## 💻 System Requirements

### Hardware Requirements

- Laptop or desktop computer.
- Minimum 4 GB RAM (8 GB recommended).
- Storage space for application and test files.
- Keyboard, mouse and display.

### Software Requirements

- Windows or Linux.
- Python 3.x.
- CustomTkinter / Tkinter.
- Python Cryptography library.
- VS Code or PyCharm.

---

## 📂 Project Structure

```text
CipherShield/
│
├── README.md
├── requirements.txt
├── main.py
│
├── encryption/
│   ├── encrypt.py
│   └── decrypt.py
│
├── integrity/
│   └── hashing.py
│
├── math_lab/
│   ├── prime.py
│   ├── gcd.py
│   ├── modular_arithmetic.py
│   └── rsa.py
│
├── gui/
│   └── interface.py
│
├── storage/
│   └── encrypted_files/
│
└── assets/
    └── screenshots/
```

### Folder Description

| Folder / File | Purpose |
|---|---|
| `main.py` | Application entry point |
| `encryption/` | File encryption and decryption |
| `integrity/` | SHA-256 hashing and verification |
| `math_lab/` | Prime, GCD, modular arithmetic and RSA |
| `gui/` | Graphical user interface |
| `storage/` | Local encrypted file storage |
| `assets/` | Screenshots and project images |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/aishlol/DM-CP.git
```

### Step 2: Navigate to the Project Directory

```bash
cd DM-CP
```

### Step 3: Create a Virtual Environment

```bash
python3 -m venv venv
```

### Step 4: Activate the Environment

**Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
python main.py
```

---

## 🔄 Working Methodology

### 1. File Encryption

1. Select a file.
2. Validate the selected file.
3. Encrypt the file using AES-256-GCM.
4. Generate encrypted output.
5. Save the encrypted file securely.

### 2. File Decryption

1. Select the encrypted file.
2. Provide the correct encryption key.
3. Authenticate and decrypt the file.
4. Recover the original file if authentication succeeds.
5. Display an error if the key is incorrect or the encrypted data has been modified.

### 3. Integrity Verification

1. Generate the original file's SHA-256 hash.
2. Store the reference hash securely.
3. Generate the hash again during verification.
4. Compare both hash values.
5. Display whether the file remains unchanged or modified.

### 4. Mathematical Demonstration

1. Enter prime numbers.
2. Calculate GCD.
3. Perform modular arithmetic.
4. Calculate RSA public and private key values.
5. Demonstrate mathematical encryption and decryption.

---

## 📊 Expected Outcomes

- Successful file encryption.
- Successful decryption using the correct key.
- Detection of incorrect encryption keys.
- Detection of modified encrypted data.
- SHA-256 file integrity verification.
- Interactive mathematical demonstrations.
- Better understanding of the relationship between Discrete Mathematics and cryptography.

*These are expected outcomes of the proposed system, not measured results.*

---

## 🔮 Future Scope

The project can be extended with the following features:

- Password-based key derivation using scrypt or PBKDF2.
- Hybrid encryption using RSA-wrapped AES keys.
- Digital signatures and key fingerprints.
- Folder and batch file encryption.
- Larger-number RSA implementation.
- Advanced primality testing using Miller–Rabin.
- SQLite-based file metadata management.

---

## 👨‍💻 Project Team

**Department:** Computer Science and Engineering (Artificial Intelligence)  
**Institute:** Vishwakarma Institute of Technology, Pune  
**Division:** CSE(AI)-G (SEDA)

| Team Member | Role |
|---|---|
| Samarth ShelKande | Project Team Member |
| Abhishek Jadhav | Project Team Member |
| Aarti Navpute | Project Team Member |
| Aishwarya Sonawane | Project Team Member |

**Project Guide:** Prof. Shraddha Mankar

---

## 🎓 Academic Information

- **Subject:** Discrete Mathematics
- **Project Title:** CipherShield
- **Academic Year:** 2026–27
- **Institution:** Vishwakarma Institute of Technology, Pune

---

## 🔒 Security Considerations

- Use trusted cryptographic libraries for actual encryption.
- Never hardcode secret encryption keys.
- Keep encryption keys separate from encrypted files.
- Store reference hashes securely.
- Use sufficiently secure random nonces for AES-GCM and never reuse a nonce with the same key.
- Do not use small educational RSA values for real-world security.

CipherShield is an educational file-protection project and is not a replacement for enterprise-grade security systems.

---

## 📜 License

A suitable open-source license can be added to the repository before public distribution.

---

**CipherShield – Connecting Discrete Mathematics with Real-World Digital Security.** 🔐