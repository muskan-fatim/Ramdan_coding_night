import streamlit as st
import random

# List of Urdu jokes
urduJokes = [
    "😂 استاد: اگر زمین سورج کے قریب ہو جائے تو کیا ہوگا؟ \n👨‍🎓 طالبعلم: سر، گرمیوں کی چھٹیاں بڑھ جائیں گی!",
    "😆 بیوی: سنو، میری طبیعت خراب لگ رہی ہے! \n😏 شوہر: ہاں، مجھے بھی شک ہو رہا تھا… آج تم نے بغیر لڑائی کیے چائے بنا دی!",
    "🤣 لڑکی: میں نے خواب دیکھا کہ تم میرے لیے چاند لے کر آئے! \n😅 لڑکا: اچھا، تو اب میں ناسا میں جاب ڈھونڈوں؟",
    "😂 دوست 1: یار، میں ایک دن میں دس گھنٹے پڑھتا ہوں! \n😜 دوست 2: واہ! پھر سوتا کب ہے؟ \n😆 دوست 1: اگلے دن!",
    "😆 استاد: بچوں، سب سے زیادہ ایماندار کون ہوتا ہے؟ \n😏 طالبعلم: وہ جس کے پاس پیسے نہ ہوں!",
    "🤣 شوہر: میں نے تمہارے کہنے پر سگریٹ چھوڑ دی! \n😜 بیوی: واہ، کتنے دن ہو گئے؟ \n😂 شوہر: ارے، تم نے کہا تھا، میں نے سنی اور جیب سے باہر پھینک دی!",
]

# Page Configuration
st.set_page_config(page_title="😂 Joke Generator", page_icon="🎭", layout="centered")

# Custom Styles
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
        }
        div.stButton > button {
            background-color: #ff4b4b;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            width: 100%;
            padding: 10px;
        }
        div.stButton > button:hover {
            background-color: #d84315;
        }
    </style>
""", unsafe_allow_html=True)

# Title & Subtitle with emoji
st.title("🎭 اردو جوک جنریٹر")
st.subheader("ہر بار ایک نیا لطیفہ سنیں! 🤣")

# Joke Button
if st.button("😂 مجھے لطیفہ سناؤ"):
    st.success(random.choice(urduJokes))

# Footer
st.markdown("---")
st.markdown("📢 **Created by [Muskan Fatima](https://github.com/muskan-fatim)**")

