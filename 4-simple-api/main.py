from fastapi import FastAPI
import random

app = FastAPI();

motivational:list[str]= [
  "Believe in yourself and all that you are. - Christian D. Larson",
  "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
  "Dream big and dare to fail. - Norman Vaughan",
  "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
  "The only way to do great work is to love what you do. - Steve Jobs",
  "You don’t have to be great to start, but you have to start to be great. - Zig Ziglar",
  "Difficulties in life are intended to make us better, not bitter. - Dan Reeves",
  "Stay hungry, stay foolish. - Steve Jobs",
  "The secret of getting ahead is getting started. - Mark Twain",
  "Your only limit is your mind.",
  "Everything you can imagine is real. - Pablo Picasso",
  "The harder you work for something, the greater you'll feel when you achieve it.",
  "Push yourself, because no one else is going to do it for you.",
  "It does not matter how slowly you go as long as you do not stop. - Confucius",
  "Success doesn’t just find you. You have to go out and get it."
]


@app.get("/motivational")
def get_motivational():
    """Returns a random motivational quote"""
    return{
  "quote":random.choice(motivational)
    }

st.markdown("📢 **Created by [Muskan Fatima](https://github.com/muskan-fatim)**")
