
from integrity.hashing import (
    calculate_sha256,
    calculate_file_hash,
    verify_sha256,
    verify_file_integrity,
    compare_files,
    get_file_information
)

# Sample data
data = b"CipherShield - Secure File Protection"

# 1. Generate SHA-256 hash
file_hash = calculate_sha256(data)

print("\n===== SHA-256 HASH GENERATION =====")
print("Original Data:", data.decode())
print("SHA-256 Hash:", file_hash)

# 2. Verify original data
print("\n===== INTEGRITY VERIFICATION =====")
print("Original Data Verified:", verify_sha256(data, file_hash))

# 3. Verify modified data
modified_data = b"Modified CipherShield Data"
print("Modified Data Verified:", verify_sha256(modified_data, file_hash))

# 4. Create sample files
with open("sample1.txt", "wb") as file:
    file.write(data)

with open("sample2.txt", "wb") as file:
    file.write(data)

# 5. Calculate file hash
print("\n===== FILE HASH =====")
print("File Hash:", calculate_file_hash("sample1.txt"))

# 6. Verify file integrity
print("\n===== FILE VERIFICATION =====")
print(
    "File Integrity:",
    verify_file_integrity("sample1.txt", file_hash)
)

# 7. Compare two files
print("\n===== FILE COMPARISON =====")
print("Files Match:", compare_files("sample1.txt", "sample2.txt"))

# 8. File information
print("\n===== FILE INFORMATION =====")
print(get_file_information("sample1.txt"))
