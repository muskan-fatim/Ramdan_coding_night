# 🚀 Muskan Fatima - Own Profile API

## 📌 About This Project
This is a **FastAPI-based** personal profile API that provides structured information about **Muskan Fatima**. The API returns details such as skills, projects, experience, certifications, and social links.

## 🛠️ Technologies Used
- ⚡ **FastAPI** - A modern web framework for building APIs with Python
- 🐍 **Python** - The core programming language
- 🔗 **Uvicorn** - ASGI server for running FastAPI applications

## 📂 API Endpoints
### 🔍 **Get Profile Information**
**Endpoint:** `GET /`

**Response:**
```json
{
    "name": "Muskan Fatima",
    "title": "Next.js & Tailwind CSS Enthusiast | Frontend Developer in Training",
    "email": "mushiifatima3456@gmail.com",
    "location": "Pakistan",
    "education": { ... },
    "skills": [ ... ],
    "projects": [ ... ],
    "experience": [ ... ],
    "certifications": [ ... ],
    "languages": { ... },
    "social_links": { ... },
    "github_repositories": [ ... ]
}
```

## 🚀 How to Run the API Locally
### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/muskan-fatim/Own-Profile-API.git
cd Own-Profile-API
```

### 2️⃣ **Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ **Install Dependencies**
```sh
pip install fastapi uvicorn
```

### 4️⃣ **Run the Server**
```sh
uvicorn main:app --reload
```

### 5️⃣ **Access the API**
- Open **http://127.0.0.1:8000** in your browser.
- Visit the interactive API docs at **http://127.0.0.1:8000/docs** 📜.

## 📜 Project Structure
```
Own-Profile-API/
│── main.py           # FastAPI application
│── requirements.txt  # Dependencies
│── README.md         # Project documentation
│── .gitignore        # Git ignored files
```

## 🌟 Features
✅ Structured JSON response with profile details  
✅ Includes **projects, experience, certifications, and social links**  
✅ FastAPI-powered for high performance  
✅ Interactive API documentation with Swagger UI  

## 📌 Connect With Me
🐙 **GitHub**: [muskan-fatim](https://github.com/muskan-fatim)  
🔗 **LinkedIn**: [Muskan Fatima](https://www.linkedin.com/in/muskan-fatima-ab90732b7/)  
🌐 **Portfolio**: [protofilo-2.vercel.app](https://protofilo-2.vercel.app/)  

🚀 **Happy Coding!** 💻🎉

