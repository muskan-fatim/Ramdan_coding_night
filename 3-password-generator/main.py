import streamlit as st
import random

passwords = ["/CS49)B4&Vt-","S59:[)m?Lm?Z","KcA6uW@PB(", "+?^c:)qs}Qxw","'T'dK(4=XUSd","jEiI&ZLupu0c","KEHq%2u~0GDE","Uy0hK$z-nX(}","K~D,y,y-~zI*","}lRt;}S|ZR(-"]

show_password = random.choice(passwords)

def is_strong_password(password):
    return (
        bool(re.search(r'[A-Z]', password)) and  # At least one uppercase letter
        bool(re.search(r'[a-z]', password)) and  # At least one lowercase letter
        bool(re.search(r'\d', password)) and     # At least one digit
        bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))  # At least one special character
    )


st.title("Password Generator")
st.subheader("generate a strong password")
if st.button("generate password"):
    st.success(show_password)

st.title("Password Analyzer")
st.subheader("check your password is strong or not")
password = st.text_input("Enter your password")

if st.button("check password"):
    if is_strong_password(password):
        st.success("your password is strong")
    else:
        st.error("your password is not strong  generate a new one")

st.write("Created By @muskan-fatim")
    