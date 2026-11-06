
import streamlit as st
import base64

from encryption.encrypt import encrypt_file
from encryption.decrypt import decrypt_file

from integrity.hashing import (
    calculate_sha256,
    verify_sha256
)

from math_lab.prime import (
    is_prime,
    get_prime_factors,
    generate_primes
)

from math_lab.gcd import (
    calculate_gcd,
    calculate_lcm,
    extended_euclidean
)

from math_lab.modular_arithmetic import (
    modular_addition,
    modular_subtraction,
    modular_multiplication,
    modular_exponentiation,
    modular_inverse
)

from math_lab.rsa import (
    generate_rsa_keys,
    rsa_encrypt,
    rsa_decrypt,
    rsa_demo
)


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="CipherShield",
    page_icon="🔐",
    layout="wide"
)


# ==========================================
# CUSTOM DESIGN
# ==========================================

st.markdown("""
<style>
.stApp {
    background-color: #0b1120;
    color: #ffffff;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

h1, h2, h3 {
    color: #60a5fa;
}

div[data-testid="stMetric"] {
    background-color: #172033;
    padding: 15px;
    border-radius: 10px;
}

.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    border: none;
}

.stButton > button:hover {
    background-color: #1d4ed8;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

st.sidebar.title("🔐 CipherShield")
st.sidebar.caption("Smart Digital Protection")

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "File Encryption",
        "File Decryption",
        "Integrity Verification",
        "Discrete Mathematics Lab",
        "About Project"
    ]
)


# ==========================================
# DASHBOARD
# ==========================================

if page == "Dashboard":

    st.title("🔐 CipherShield")

    st.subheader(
        "Smart Digital Protection Through Mathematical Cryptography"
    )

    st.divider()

    st.write("""
    CipherShield demonstrates how Discrete Mathematics
    is applied in modern cryptography.

    Secure your digital files, verify file integrity,
    and explore mathematical concepts behind encryption.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Encryption", "AES-256-GCM")
    col2.metric("Integrity", "SHA-256")
    col3.metric("Cryptography", "RSA Demo")

    st.divider()

    st.subheader("Project Modules")

    c1, c2 = st.columns(2)

    with c1:
        st.info("🔒 Secure File Encryption")
        st.info("🔓 File Decryption")
        st.info("🛡️ SHA-256 Integrity Verification")

    with c2:
        st.info("🔢 Prime Number Checker")
        st.info("➗ GCD and LCM Calculator")
        st.info("🔐 Modular Arithmetic and RSA")


# ==========================================
# FILE ENCRYPTION
# ==========================================

elif page == "File Encryption":

    st.title("🔒 AES-256-GCM File Encryption")

    st.write("Encrypt your files using authenticated AES-256-GCM encryption.")

    uploaded_file = st.file_uploader(
        "Select a file to encrypt",
        key="encrypt_upload"
    )

    if uploaded_file:

        st.write("Selected file:", uploaded_file.name)

        if st.button("Encrypt File", type="primary"):

            try:
                file_data = uploaded_file.getvalue()

                encrypted_data, key = encrypt_file(file_data)

                encoded_key = base64.b64encode(key).decode("utf-8")

                st.success("File encrypted successfully!")

                st.warning(
                    "Save your encryption key securely. "
                    "Without it, you cannot decrypt your file."
                )

                st.code(encoded_key)

                st.download_button(
                    "Download Encryption Key",
                    data=encoded_key,
                    file_name="ciphershield_key.txt",
                    mime="text/plain"
                )

                st.download_button(
                    "Download Encrypted File",
                    data=encrypted_data,
                    file_name=uploaded_file.name + ".enc",
                    mime="application/octet-stream"
                )

            except Exception as error:
                st.error(f"Encryption failed: {error}")


# ==========================================
# FILE DECRYPTION
# ==========================================

elif page == "File Decryption":

    st.title("🔓 AES-256-GCM File Decryption")

    st.write("Restore your original file using its encryption key.")

    uploaded_file = st.file_uploader(
        "Select encrypted file",
        type=["enc"],
        key="decrypt_upload"
    )

    key_input = st.text_input(
        "Enter encryption key (Base64)",
        type="password"
    )

    if st.button("Decrypt File", type="primary"):

        if not uploaded_file or not key_input:

            st.error("Please upload an encrypted file and enter its key.")

        else:

            try:
                key = base64.b64decode(
                    key_input.strip(),
                    validate=True
                )

                encrypted_data = uploaded_file.getvalue()

                original_data = decrypt_file(
                    encrypted_data,
                    key
                )

                original_name = uploaded_file.name

                if original_name.endswith(".enc"):
                    original_name = original_name[:-4]

                st.success("File decrypted successfully!")

                st.download_button(
                    "Download Original File",
                    data=original_data,
                    file_name=original_name,
                    mime="application/octet-stream"
                )

            except Exception as error:

                st.error(f"Decryption failed: {error}")


# ==========================================
# SHA-256 INTEGRITY VERIFICATION
# ==========================================

elif page == "Integrity Verification":

    st.title("🛡️ SHA-256 Integrity Verification")

    st.write("""
    Generate a SHA-256 fingerprint for your file.
    Compare it with a previously saved hash to detect modifications.
    """)

    uploaded_file = st.file_uploader(
        "Upload file for integrity verification",
        key="integrity_upload"
    )

    if uploaded_file:

        file_data = uploaded_file.getvalue()

        st.write("File:", uploaded_file.name)
        st.write("File size:", f"{len(file_data)} bytes")

        if st.button("Generate SHA-256 Hash", type="primary"):

            file_hash = calculate_sha256(file_data)

            st.session_state["generated_hash"] = file_hash

            st.success("SHA-256 hash generated successfully!")

        if st.session_state.get("generated_hash"):

            st.subheader("Generated SHA-256 Hash")

            st.code(st.session_state["generated_hash"])

            st.download_button(
                "Download SHA-256 Hash",
                data=st.session_state["generated_hash"],
                file_name=uploaded_file.name + ".sha256",
                mime="text/plain"
            )

        st.divider()

        st.subheader("Verify File Integrity")

        expected_hash = st.text_input(
            "Enter original SHA-256 hash"
        )

        if st.button("Verify Integrity"):

            if not expected_hash.strip():

                st.warning("Please enter the original SHA-256 hash.")

            elif len(expected_hash.strip()) != 64:

                st.error("A SHA-256 hash must contain 64 hexadecimal characters.")

            else:

                try:
                    int(expected_hash.strip(), 16)

                    result = verify_sha256(
                        file_data,
                        expected_hash
                    )

                    if result:
                        st.success("File integrity verified! No changes detected.")
                    else:
                        st.error("Integrity verification failed! File may have been modified.")

                except ValueError:
                    st.error("Invalid SHA-256 hash format.")


# ==========================================
# DISCRETE MATHEMATICS LAB
# ==========================================

elif page == "Discrete Mathematics Lab":

    st.title("🧮 Discrete Mathematics Lab")

    st.write(
        "Explore mathematical concepts used in cryptography."
    )

    tool = st.selectbox(
        "Select Mathematical Operation",
        [
            "Prime Number Checker",
            "Prime Factorization",
            "Generate Prime Numbers",
            "GCD Calculator",
            "LCM Calculator",
            "Extended Euclidean Algorithm",
            "Modular Addition",
            "Modular Subtraction",
            "Modular Multiplication",
            "Modular Exponentiation",
            "Modular Multiplicative Inverse",
            "RSA Demonstration",
            "RSA Custom Encryption"
        ]
    )

    st.divider()

    # PRIME NUMBER CHECKER

    if tool == "Prime Number Checker":

        st.subheader("Prime Number Checker")

        number = st.number_input(
            "Enter an integer",
            min_value=-1000000000,
            max_value=1000000000,
            value=17,
            step=1
        )

        if st.button("Check Prime"):

            if is_prime(number):
                st.success(f"{number} is a Prime Number.")
            else:
                st.warning(f"{number} is not a Prime Number.")

    # PRIME FACTORIZATION

    elif tool == "Prime Factorization":

        st.subheader("Prime Factorization")

        number = st.number_input(
            "Enter a positive integer",
            min_value=1,
            value=60,
            step=1
        )

        if st.button("Find Prime Factors"):

            factors = get_prime_factors(number)

            st.success(f"Prime Factors: {factors}")

    # GENERATE PRIME NUMBERS

    elif tool == "Generate Prime Numbers":

        st.subheader("Generate Prime Numbers")

        limit = st.number_input(
            "Generate primes up to",
            min_value=2,
            max_value=100000,
            value=50,
            step=1
        )

        if st.button("Generate Primes"):

            primes = generate_primes(limit)

            st.success(f"Found {len(primes)} prime numbers.")

            st.write(primes)

    # GCD CALCULATOR

    elif tool == "GCD Calculator":

        st.subheader("Greatest Common Divisor")

        a = st.number_input("Enter first number", value=48, step=1)
        b = st.number_input("Enter second number", value=18, step=1)

        if st.button("Calculate GCD"):

            result = calculate_gcd(a, b)

            st.success(f"GCD({a}, {b}) = {result}")

    # LCM CALCULATOR

    elif tool == "LCM Calculator":

        st.subheader("Least Common Multiple")

        a = st.number_input("Enter first number", value=12, step=1)
        b = st.number_input("Enter second number", value=18, step=1)

        if st.button("Calculate LCM"):

            result = calculate_lcm(a, b)

            st.success(f"LCM({a}, {b}) = {result}")

    # EXTENDED EUCLIDEAN

    elif tool == "Extended Euclidean Algorithm":

        st.subheader("Extended Euclidean Algorithm")

        a = st.number_input("Enter first number", value=48, step=1)
        b = st.number_input("Enter second number", value=18, step=1)

        if st.button("Calculate Extended GCD"):

            gcd, x, y = extended_euclidean(a, b)

            st.success(f"GCD = {gcd}")

            st.write(f"x = {x}")
            st.write(f"y = {y}")

            st.info(f"{a} × ({x}) + {b} × ({y}) = {gcd}")

    # MODULAR ADDITION

    elif tool == "Modular Addition":

        st.subheader("Modular Addition")

        a = st.number_input("First number", value=17, step=1)
        b = st.number_input("Second number", value=8, step=1)
        m = st.number_input("Modulus", min_value=1, value=5, step=1)

        if st.button("Calculate"):

            st.success(f"Result = {modular_addition(a, b, m)}")

    # MODULAR SUBTRACTION

    elif tool == "Modular Subtraction":

        st.subheader("Modular Subtraction")

        a = st.number_input("First number", value=17, step=1)
        b = st.number_input("Second number", value=8, step=1)
        m = st.number_input("Modulus", min_value=1, value=5, step=1)

        if st.button("Calculate"):

            st.success(f"Result = {modular_subtraction(a, b, m)}")

    # MODULAR MULTIPLICATION

    elif tool == "Modular Multiplication":

        st.subheader("Modular Multiplication")

        a = st.number_input("First number", value=7, step=1)
        b = st.number_input("Second number", value=4, step=1)
        m = st.number_input("Modulus", min_value=1, value=5, step=1)

        if st.button("Calculate"):

            st.success(f"Result = {modular_multiplication(a, b, m)}")

    # MODULAR EXPONENTIATION

    elif tool == "Modular Exponentiation":

        st.subheader("Modular Exponentiation")

        base = st.number_input("Base", value=3, step=1)
        exponent = st.number_input(
            "Exponent",
            min_value=0,
            value=4,
            step=1
        )
        modulus = st.number_input(
            "Modulus",
            min_value=1,
            value=7,
            step=1
        )

        if st.button("Calculate"):

            result = modular_exponentiation(
                base,
                exponent,
                modulus
            )

            st.success(f"Result = {result}")

    # MODULAR INVERSE

    elif tool == "Modular Multiplicative Inverse":

        st.subheader("Modular Multiplicative Inverse")

        a = st.number_input("Enter number", value=3, step=1)
        m = st.number_input("Enter modulus", min_value=2, value=11, step=1)

        if st.button("Find Modular Inverse"):

            try:

                result = modular_inverse(a, m)

                st.success(f"Modular Inverse = {result}")

                st.info(f"({a} × {result}) mod {m} = 1")

            except ValueError as error:

                st.error(str(error))

    # RSA DEMONSTRATION

    elif tool == "RSA Demonstration":

        st.subheader("RSA Educational Demonstration")

        st.write("Using the example from the CipherShield project.")

        if st.button("Run RSA Demonstration", type="primary"):

            try:

                result = rsa_demo()

                keys = result["keys"]

                st.write("Prime p:", keys["p"])
                st.write("Prime q:", keys["q"])
                st.write("n:", keys["n"])
                st.write("Euler's Totient:", keys["phi"])

                st.write("Public Key:", keys["public_key"])
                st.write("Private Key:", keys["private_key"])

                st.write("Original Message:", result["original_message"])
                st.write("Encrypted Message:", result["encrypted_message"])
                st.write("Decrypted Message:", result["decrypted_message"])

                if result["successful"]:
                    st.success("RSA Encryption and Decryption Successful!")

            except Exception as error:

                st.error(f"RSA Error: {error}")

        st.warning(
            "Educational demonstration only. "
            "This small-key RSA implementation is not suitable for real security."
        )

    # CUSTOM RSA

    elif tool == "RSA Custom Encryption":

        st.subheader("Custom RSA Demonstration")

        col1, col2 = st.columns(2)

        with col1:
            p = st.number_input(
                "Enter prime p",
                min_value=2,
                value=5,
                step=1
            )

        with col2:
            q = st.number_input(
                "Enter prime q",
                min_value=2,
                value=11,
                step=1
            )

        message = st.number_input(
            "Enter integer message",
            min_value=0,
            value=7,
            step=1
        )

        if st.button("Generate Keys and Encrypt", type="primary"):

            try:

                keys = generate_rsa_keys(p, q)

                if message >= keys["n"]:
                    st.error("Message must be smaller than n.")
                else:

                    encrypted = rsa_encrypt(
                        message,
                        keys["public_key"]
                    )

                    decrypted = rsa_decrypt(
                        encrypted,
                        keys["private_key"]
                    )

                    st.success("RSA operation completed!")

                    st.write("n:", keys["n"])
                    st.write("φ(n):", keys["phi"])
                    st.write("Public Key:", keys["public_key"])
                    st.write("Private Key:", keys["private_key"])

                    st.write("Original Message:", message)
                    st.write("Encrypted Message:", encrypted)
                    st.write("Decrypted Message:", decrypted)

                    if message == decrypted:
                        st.success("Original and decrypted messages match!")

            except (ValueError, TypeError) as error:

                st.error(str(error))

            except Exception as error:

                st.error(f"RSA operation failed: {error}")


# ==========================================
# ABOUT PROJECT
# ==========================================

elif page == "About Project":

    st.title("About CipherShield")

    st.subheader(
        "Smart Digital Protection Through Mathematical Cryptography"
    )

    st.write("""
    **Project:** CipherShield

    **Subject:** Discrete Mathematics

    **Institute:** Vishwakarma Institute of Technology, Pune

    **Project Guide:** Prof. Shraddha Mankar

    **Team Members:**
    - Samarth ShelKande
    - Abhishek Jadhav
    - Aarti Navpute
    - Aishwarya Sonawane
    """)

    st.divider()

    st.subheader("Technologies Used")

    st.write("""
    - Python
    - Streamlit
    - AES-256-GCM
    - SHA-256
    - RSA (Educational Demonstration)
    - Discrete Mathematics
    """)
