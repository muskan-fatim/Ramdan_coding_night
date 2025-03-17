import streamlit as st

st.title("Simple Calculator")
num1 = st.text_input("Enter you first number")
num2 = st.text_input("Enter you second  number")

operation = st.selectbox('Select the operation',["Addition (+) ","subtraction (-) ","Divison (/) ","Multiplication (x) "])
result  = 0
symbol  = 0
if st.button("Calculate"):
    if(operation == "Addition (+) "):
       result =  int(num1) + int(num2)
       symbol = "+"
    elif(operation == "subtraction (-) "):
       result =  int(num1) - int(num2)
       symbol = "-"
    elif(operation == "Divison (/) "):
       if (num1 or num2 / 0):
        result = "Can't divided by 0"
        symbol = "/"
       else:
          result =  int(num1) / int(num2)
    elif(operation == "Multiplication (x) "):
       result =  int(num1)* int(num2)
       symbol = "x"

    st.success(f"{num1} {symbol} {num2} = {result}")

st.set_page_config(title="simple calculator",page_icon="🔢")

st.markdown("📢 **Created by [Muskan Fatima](https://github.com/muskan-fatim)**")
