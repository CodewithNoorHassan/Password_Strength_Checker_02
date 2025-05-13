import streamlit as st
import re
import random
import string

# ------------------- Page Setup -------------------
st.set_page_config(page_title="Password Strength Checker 🔐", layout="centered")

# ------------------- Custom CSS -------------------
st.markdown("""
<style>
    body {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    h1 {
        color: #00D9FF;
        text-align: center;
        margin-bottom: 30px;
    }

    .stTextInput > div > div > input {
        background-color: #eef2f6;
        border-radius: 8px;
        padding: 12px;
        color: black;
        font-size: 16px;
        font-weight: 500; 
        box-shadow: 0px 4px 15px rgba(0, 217, 255, 0.2);
    }

    .stButton > button {
        background-color: #00D9FF;
        color: black;
        font-weight: 600;
        border-radius: 12px;
        padding: 0.8rem 2rem;
        font-size: 18px;
        transition: 0.3s ease;
        box-shadow: 0px 6px 20px rgba(0, 217, 255, 0.3);
        margin-top: 10px;
    }

    .stButton > button:hover {
        background-color: #0099cc;
        color: black !important;
    }
            
}
        
</style>
""", unsafe_allow_html=True)

# ------------------- Helper Functions -------------------
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def check_strength(password):
    score = 0
    feedback = []
    common_passwords = ['password', '123456', 'qwerty', 'password123', 'admin', 'letmein']

    if password.lower() in common_passwords:
        feedback.append("❌ Too common. Choose something more unique.")
        return 0, feedback

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Use at least 8 characters.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include at least one digit (0–9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Add a special character (!@#$%^&*).")

    if len(password) >= 12:
        score += 1 
    else:
        feedback.append("❌ Use 12+ characters for maximum security.")

    return score, feedback

# ------------------- Main App UI -------------------
st.title("🔐 Password Strength Checker")
st.caption("Secure your world in a Cyber style ✨")

# Form to allow pressing "Enter"
with st.form(key="pw_form"):
    password = st.text_input("Enter your password", type="password", placeholder="Type your password here")
    submit = st.form_submit_button("🔎 Check Password")

if submit:
    if not password:
        st.warning("⚠️ Please enter a password first.")
    else:
        score, feedback = check_strength(password)
        st.subheader("🔍 Password Analysis")
        st.progress(score / 5)

        if score == 5:
            st.success("✅ Perfect! Your password is very strong and secure.")
        elif score >= 3:
            st.warning("⚠️ Moderate. You can still improve it.")
        else:
            st.error("❌ Weak password. See suggestions below.")

        st.markdown(f"**🧪 Score:** `{score}/5`")
        if feedback:
            st.markdown("**💡 Suggestions:**")
            for tip in feedback:
                st.markdown(f"- {tip}")

# ------------------- Generate Password Section -------------------
st.markdown("---")
st.markdown("### 💎 Need a Stronger Password?")
if st.button("✨ Generate Strong Password"):
    strong_password = generate_password(14)
    st.success("🎉 Strong password generated successfully!")
    st.text_input("📋 Copy your password below:", value=strong_password, key="generated_pw")
