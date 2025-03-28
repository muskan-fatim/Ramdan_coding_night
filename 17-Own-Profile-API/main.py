from fastapi import FastAPI

app = FastAPI()

@app.get("/profile")
def get_profile():
    return {
    "name": "👩‍💻 Muskan Fatima",
    "title": "🚀 Next.js & Tailwind CSS Enthusiast | 🎨 Frontend Developer in Training",
    "email": "📧 mushiifatima3456@gmail.com",
    "location": "📍 Pakistan",
    "education": {
        "degree": "🎓 Bachelor of Science",
        "certification": "📜 GenEng - The Cloud Applied Generative AI Engineering",
        "graduation_year": "🎓 2026"
    },
    "skills": [
        "⚛️ Next.js", "⚛️ React.js", "🎨 Tailwind CSS", "📜 JavaScript", "🐍 Python",
        "🔗 API Integration", "🎨 Figma", "🔧 Git & GitHub", "🧩 Problem-Solving"
    ],
    "projects": [
        {
            "name": "📄 Resume Generator",
            "description": "📝 A tool that generates resumes from templates with complex logic and customization.",
            "technologies": ["⚛️ Next.js", "📜 TypeScript", "🎨 CSS"],
            "github": "🔗 https://github.com/muskan-fatim/Resume-Generator"
        },
        {
            "name": "🍔 FoodPanda Clone",
            "description": "🌐 A fully responsive clone of the FoodPanda website.",
            "technologies": ["⚛️ React.js", "🎨 CSS"],
            "github": "🔗 https://github.com/muskan-fatim/FoodPanda-Clone"
        },
        {
            "name": "💡 Simple API",
            "description": "📜 FastAPI project that returns random motivational quotes.",
            "technologies": ["🐍 Python", "⚡ FastAPI"],
            "github": "🔗 https://github.com/muskan-fatim/Simple-API"
        }
    ],
    "experience": [
        {
            "role": "👩‍💻 Contributor",
            "organization": "🌍 GirlScript Summer of Code",
            "duration": "📆 Oct 2024 - Nov 2024",
            "description": "🤝 Contributed to open-source projects and collaborated with developers globally."
        }
    ],
    "certifications": [
        {
            "name": "🏅 Deployed Typed Function Using TypeScript",
            "issuer": "🎓 Microsoft",
            "date": "📆 May 28, 2024"
        }
    ],
    "languages": {
        "English": "🗣️ Advanced",
        "Urdu": "🗣️ Fluent"
    },
    "social_links": {
        "github": "🐙 https://github.com/muskan-fatim",
        "linkedin": "🔗 https://www.linkedin.com/in/muskan-fatima-ab90732b7/",
        "portfolio": "🌐 https://protofilo-2.vercel.app/"
    },
    "github_repositories": [
        {
            "name": "🌙 Ramdan Coding Night",
            "description": "💻 A challenge aimed at improving coding skills during the holy month.",
            "technologies": ["🐍 Python", "🤖 Prompt", "🔗 Gemini", "⚡ UV", "⚡ FastAPI", "📊 Streamlit", "🔗 Chain"],
            "github_url": "🔗 https://github.com/muskan-fatim/Ramdan_coding_night"
        },
        {
            "name": "🍔 FoodPanda Clone",
            "description": "🌐 A fully responsive clone of the FoodPanda website.",
            "technologies": ["⚛️ Next.js", "🎨 CSS"],
            "github_url": "🔗 https://github.com/muskan-fatim/FoodPanda-Clone"
        },
        {
            "name": "📄 Resume Generator",
            "description": "📝 A tool that generates resumes from templates with complex logic and customization.",
            "technologies": ["⚛️ Next.js", "📜 TypeScript", "🎨 CSS"],
            "github_url": "🔗 https://github.com/muskan-fatim/Resume-Generator"
        },
        {
            "name": "🌍 Protofilo_2",
            "description": "💼 My personal portfolio created with Next.js and TypeScript.",
            "technologies": ["⚛️ Next.js", "📜 TypeScript", "🎨 CSS"],
            "github_url": "🔗 https://github.com/muskan-fatim/Protofilo_2"
        },
        {
            "name": "⏳ CLI Countdown App",
            "description": "🕒 A command-line interface countdown application.",
            "technologies": ["📜 TypeScript", "🎛️ Inquirer"],
            "github_url": "🔗 https://github.com/muskan-fatim/CLI-Countdown-App"
        },
        {
            "name": "📚 Student Management CLI",
            "description": "🎓 A CLI-based student management system.",
            "technologies": ["📜 TypeScript", "🎛️ Inquirer"],
            "github_url": "🔗 https://github.com/muskan-fatim/Student-Management-CLI"
        }
    ]
}
