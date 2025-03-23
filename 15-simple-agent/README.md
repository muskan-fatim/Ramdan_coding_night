# Greeting Agent

This is a simple AI-powered **Greeting Agent** that responds to user messages based on predefined instructions. It utilizes **Google Gemini API**, **Streamlit**, and **OpenAI-compatible libraries** to generate responses.

## 🚀 Features
- Responds to common greetings like `Aslam-alikum`, `Hi`, `Allah hafiz`, and `bye`.
- Uses **Gemini API** for generating responses.
- Implements **async API calls** for efficient performance.
- Built with **Python**, **Streamlit**, and **AsyncOpenAI**.

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone <your-repo-url>
cd <your-project-folder>
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```sh
uv add  python-dotenv openai-agents
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the project directory and add your Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## 🚀 Running the Application
Run the script using:
```sh
python main.py
```
It will prompt you to enter a message and provide a response based on predefined rules.

## 📜 Usage
- **Input:** Enter a message in the console.
- **Output:** The AI will generate a response based on the message.

### Example Interactions
| User Input  | AI Response  |
|-------------|-------------|
| `Aslam-alikum` | `Walikum-aslam from Muskan` |
| `Hi` | `Walikum-aslam from Muskan` |
| `Allah hafiz` | `Allah hafiz` |
| `Bye` | `Allah hafiz` |
| `How are you?` | `I am only for greeting you` |

## 📌 Technologies Used
- **Python**
- **Streamlit**
- **Google Gemini API**
- **AsyncOpenAI**
- **Dotenv** (For environment variables)

Happy Coding! 🚀

