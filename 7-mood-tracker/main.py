import os 
import pandas as pd 
import streamlit as st
import csv
import datetime

moodfile = "Mood_file.csv"


def load_mood():
    if not os.path.exists(moodfile):
      return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(moodfile)

def save_mood(date,mood):
    with open(moodfile, "a") as file:
        writer =  csv.writer(file)
        writer.writerow([date, mood])

st.title("Mood tracking app")
date:str= datetime.date.today()
mood:list[str] = st.selectbox("select your mood",["Happy","sad","Neutral","Angry","Anxious"])

if st.button("Save Mood"):
    save_mood(date,mood) 
    st.success("Mood loged succesfully")

data = load_mood()

if not data.empty:
    st.subheader("Mood trends over time")

    data["Date"] = pd.to_datetime(data["Date"])

    mood_counts = data.groupby("Mood").count()["Date"]

    st.bar_chart(mood_counts)

st.set_page_config(page_title="Mood Tracker", page_icon="💭")

st.markdown("📢 **Created by [Muskan Fatima](https://github.com/muskan-fatim)**")
