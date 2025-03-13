import streamlit as st
import random
import time
import requests
def generate_money():
    amount = random.randint(1,1000)
    return amount

st.title("Money making Machine")
st.subheader("Generate money by clicking the button below")
if st.button("Generate Money"):
    st.write("Generating money...")
    time.sleep(3)
    amount = generate_money()
    st.success(f"Generated ${amount} dollars")
    st.balloons()

    #add the motivatinal quote using local fast api
def get_motivational_quote():
      try:
        response = requests.get("http://127.0.0.1:8000/motivational")
        if response.status_code == 200:
            motivatinal =  response.json()
            return motivatinal["quote"]
        else:
            return "it's your road and yours alone. others may walk it with you but no one can walk it for you"
      except:
        ("something went wrong")

st.subheader("Motivatinal Quotes")
if st.button("Generate Quote"):
    st.write("Generating quote...")
    time.sleep(3)
    motivation = get_motivational_quote()
    st.success(motivation)


    
