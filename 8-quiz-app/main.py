import streamlit as st
import random
import time
questions = [
  {
    "question": "What is the capital of Pakistan?",
    "options": ["Karachi", "Lahore", "Islamabad", "Peshawar"],
    "correctAnswer": "Islamabad"
  },
  {
    "question": "Which is the largest ocean on Earth?",
    "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
    "correctAnswer": "Pacific Ocean"
  },
  {
    "question": "Who is known as the Father of Pakistan?",
    "options": ["Allama Iqbal", "Liaquat Ali Khan", "Quaid-e-Azam", "Benazir Bhutto"],
    "correctAnswer": "Quaid-e-Azam"
  },
  {
    "question": "How many continents are there in the world?",
    "options": ["5", "6", "7", "8"],
    "correctAnswer": "7"
  },
  {
    "question": "What is the national flower of Pakistan?",
    "options": ["Tulip", "Rose", "Jasmine", "Sunflower"],
    "correctAnswer": "Jasmine"
  },
  {
    "question": "What is the capital city of France?",
    "options": ["Berlin", "Madrid", "Paris", "Rome"],
    "correctAnswer": "Paris"
  },
  {
    "question": "Which is the longest river in the world?",
    "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
    "correctAnswer": "Nile River"
  },
  {
    "question": "Which currency is used in Pakistan?",
    "options": ["Rupee", "Dollar", "Pound", "Yen"],
    "correctAnswer": "Rupee"
  },
  {
    "question": "What is the national language of Pakistan?",
    "options": ["Punjabi", "Sindhi", "Urdu", "Pashto"],
    "correctAnswer": "Urdu"
  },
  {
    "question": "How many players are there in a cricket team?",
    "options": ["9", "10", "11", "12"],
    "correctAnswer": "11"
  },
  {
    "question": "Which planet is known as the Red Planet?",
    "options": ["Earth", "Mars", "Venus", "Jupiter"],
    "correctAnswer": "Mars"
  },
  {
    "question": "Who invented the telephone?",
    "options": ["Albert Einstein", "Alexander Graham Bell", "Isaac Newton", "Nikola Tesla"],
    "correctAnswer": "Alexander Graham Bell"
  },
  {
    "question": "Which city is known as the City of Lights in Pakistan?",
    "options": ["Lahore", "Islamabad", "Karachi", "Multan"],
    "correctAnswer": "Karachi"
  },
  {
    "question": "Which is the smallest country in the world?",
    "options": ["Monaco", "Maldives", "Vatican City", "Luxembourg"],
    "correctAnswer": "Vatican City"
  },
  {
    "question": "What is the national animal of Pakistan?",
    "options": ["Lion", "Markhor", "Tiger", "Leopard"],
    "correctAnswer": "Markhor"
  }
];
st.title("Quiz app")

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

st.subheader(question["question"])

selected_option = st.radio("Choose your answer", question["options"], key="correctAnswer")

if st.button("Submit Answer"):

    if selected_option == question["correctAnswer"]:
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect! the correct answer is " + question["correctAnswer"])
  

    st.session_state.current_question = random.choice(questions)
    time.sleep(3)
    st.rerun()

st.set_page_config(title="Quiz App", page_icon="🔍")
st.markdown("📢 **Created by [Muskan Fatima](https://github.com/muskan-fatim)**")
