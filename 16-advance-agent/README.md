# Advanced AI Greeting Agent

## 🚀 Project Overview
This project is an **Advanced AI Greeting Agent** built using **Chainlit**, **AsyncOpenAI**, and **Gemini API**. The agent is designed to greet users based on specific keywords and provide profile details about **Muskan Fatima** using an API.

## 🎯 Features
- Responds with a **friendly greeting** when a user says:
  - **"Aslam-alikum"** → Replies **"Walikum-aslam from Muskan"**
  - **"Hi" or "Hello"** → Replies **"Walikum-aslam from Muskan"**
  - **"Allah Hafiz" or "Bye"** → Replies **"Allah Hafiz"**
  - Any other message → Replies **"I'm only able to provide greetings from muskan fatima . I can't answer other questions at this time"**
- Fetches **Muskan Fatima's profile details** from an external API.
- Implements **OAuth authentication** via GitHub.
- Maintains a **chat session history**.

## 🛠️ Tech Stack
- **Python** (FastAPI, Chainlit, Requests)
- **AsyncOpenAI** for AI-powered responses
- **Gemini API** for generative AI models
- **OAuth** for user authentication

## 📂 Project Structure
```
├── .env                  # Environment variables (API Keys)
├── main.py               # Main application file
├── agents.py             # Agent and AI model configuration
├── requirements.txt      # Dependencies
└── README.md             # Project Documentation
```

## ⚙️ Setup & Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/advanced-ai-greeting-agent.git
   cd advanced-ai-greeting-agent
   ```

2. **Create a Virtual Environment & Install Dependencies**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up API Keys** in a `.env` file:
   ```env
   GEMINI_API_KEY=your_gemini_api_key
   ```

4. **Run the Application**
   ```bash
   chainlit run main.py
   ```

## 🔗 API Integration
The project fetches **Muskan Fatima's** profile details from an API endpoint:
```python
response = requests.get("https://personal-api-orcin.vercel.app/profile")
```
**Response Example:**
```json
{
  "name": "Muskan Fatima",
  "skills": ["Next.js", "Tailwind CSS", "Python", "Git", "GitHub"]
}
```

## 📌 About Muskan Fatima
👩‍💻 **Frontend Developer | Next.js & Tailwind Enthusiast**  
🎓 **Student of Cloud Applied Generative AI Engineering**  
📅 **Graduating in 2026**  
🔗 **[GitHub](https://github.com/muskan-fatim) | [LinkedIn](https://www.linkedin.com/in/muskan-fatima/)**



