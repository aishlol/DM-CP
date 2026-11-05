
import streamlit as st
import base64

from encryption.encrypt import encrypt_file
from encryption.decrypt import decrypt_file


# -------------------------------
# PAGE CONFIGURATION
# -------------------------------

st.set_page_config(
    page_title="CipherShield",
    page_icon="🔐",
    layout="wide"
)


# -------------------------------
# CUSTOM DESIGN
# -------------------------------

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
</style>
""", unsafe_allow_html=True)


# -------------------------------
# SIDEBAR
# -------------------------------

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


# -------------------------------
# DASHBOARD
# -------------------------------

if page == "Dashboard":

    st.title("🔐 CipherShield")

    st.write(
        "Smart Digital Protection Through Mathematical Cryptography"
    )

    st.divider()

    st.subheader("Welcome to CipherShield")

    st.write(
        """
        CipherShield demonstrates how Discrete Mathematics
        is applied in modern cryptography.

        Secure your digital files, verify file integrity
        and explore mathematical concepts behind encryption.
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Encryption", "AES-256-GCM")

    with col2:
        st.metric("Integrity", "SHA-256")

    st.divider()

    st.subheader("Project Modules")

    c1, c2 = st.columns(2)

    with c1:
        st.info("🔒 Secure File Encryption")
        st.info("🔓 File Decryption")

    with c2:
        st.info("🛡️ Integrity Verification")
        st.info("🧮 Discrete Mathematics Lab")


# -------------------------------
# FILE ENCRYPTION
# -------------------------------

elif page == "File Encryption":

    st.title("🔒 File Encryption")

    st.write("Encrypt your files using AES-256-GCM.")

    uploaded_file = st.file_uploader(
        "Select a file to encrypt"
    )

    if uploaded_file:

        st.write("File:", uploaded_file.name)

        if st.button("Encrypt File", type="primary"):

            file_data = uploaded_file.getvalue()

            encrypted_data, key = encrypt_file(file_data)

            st.success("File encrypted successfully!")

            encoded_key = base64.b64encode(key).decode("utf-8")

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


# -------------------------------
# FILE DECRYPTION
# -------------------------------

elif page == "File Decryption":

    st.title("🔓 File Decryption")

    st.write("Restore your original file using its encryption key.")

    uploaded_file = st.file_uploader(
        "Select encrypted file",
        type=["enc"]
    )

    key_input = st.text_input(
        "Enter encryption key (Base64)",
        type="password"
    )

    if st.button("Decrypt File", type="primary"):

        if not uploaded_file or not key_input:

            st.error("Please upload a file and enter its key.")

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


# -------------------------------
# INTEGRITY VERIFICATION
# -------------------------------

elif page == "Integrity Verification":

    st.title("🛡️ Integrity Verification")

    st.write(
        "SHA-256 hashing will be implemented in the next module."
    )


# -------------------------------
# DISCRETE MATHEMATICS LAB
# -------------------------------

elif page == "Discrete Mathematics Lab":

    st.title("🧮 Discrete Mathematics Lab")

    st.write(
        "Prime numbers, GCD, modular arithmetic and RSA."
    )

    st.info("Mathematical modules will be implemented next.")


# -------------------------------
# ABOUT PROJECT
# -------------------------------

elif page == "About Project":

    st.title("About CipherShield")

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
