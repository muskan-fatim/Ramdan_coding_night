# 🌟 FastAPI Motivational Quotes API

## 🚀 Overview
This project is a **Motivational Quotes API** built using **FastAPI**. It provides a random motivational quote upon request.

---

## 🔧 Technologies Used
- **Python** 🐍
- **FastAPI** 🚀
- **Random** (to select random quotes)

---

## 🌟 Features
✅ Provides a random motivational quote
✅ Fast and lightweight API
✅ Simple and easy to use
✅ Suitable for integration into other applications

---

## 📌 How to Use
### 🔗 Get a Random Motivational Quote
1. Run the API (see installation steps below).
2. Make a GET request to:
   ```sh
   http://127.0.0.1:8000/motivational
   ```
3. You will receive a random motivational quote in JSON format:
   ```json
   {
     "quote": "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill"
   }
   ```

---

## 📥 Installation & Running the API
1. Clone the repository:
   ```sh
   git clone https://github.com/muskan-fatim/4-simple-api.git
   cd motivational-api
   ```
2. Install dependencies:
   ```sh
   pip install fastapi uvicorn
   ```
3. Run the API:
   ```sh
   uvicorn main:app --reload
   ```
4. Open the browser and visit:
   ```sh
   http://127.0.0.1:8000/docs
   ```
   to see the interactive API documentation.

---

## 📌 Future Enhancements
- Add more quotes to the dataset
- Categorize quotes based on different moods
- Allow users to submit their own quotes

📢 **Created by [Muskan Fatima](https://github.com/muskan-fatim)** 🚀

