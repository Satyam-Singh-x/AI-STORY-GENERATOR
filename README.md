📖 AI Story Generator from Images

An AI-powered storytelling application that generates creative stories and narrations from images using Google Gemini AI and Text-to-Speech (gTTS).
Upload images, choose a genre, and let AI turn visuals into engaging stories with voice narration.

Live link: https://satyam-story-generator-0912.streamlit.app/

🚀 Features

🖼 Upload 1–10 images

🎭 Multiple story styles:

Comedy

Thriller

Fairy Tale

Mythological

Sci-Fi

Mystery

Adventure

Romantic

Horror

Morale

✍️ AI-generated coherent story

🔊 Automatic audio narration

🇮🇳 Indian cultural context

⚡ Built with Streamlit (fast UI)

🎧 Audio output in MP3 format

🧠 How It Works

User uploads images

User selects a story genre

Images + prompt → Gemini AI

AI generates a story

Story is converted to speech using gTTS

Audio is played inside the app

🗂 Project Structure


AI-Story-Generator/
│
├── app.py                     # Streamlit frontend

├── Story_generator_fn.py      # AI + narration logic

├── .env                       # API keys (not tracked)

├── .gitignore

├── requirements.txt

└── README.md

🔑 Environment Setup

1️⃣ Create .env file

GOOGLE_API_KEY=your_google_api_key_here


⚠️ Never commit this file.

📦 Installation

pip install -r requirements.txt

Required Packages

streamlit

python-dotenv

google-generativeai

gTTS

Pillow

▶️ Run the App
streamlit run app.py


Then open:

http://localhost:8501

🧪 Example Usage

Upload 1–10 images

Select a story style

Click Generate Story and Narration

Read the story

Listen to the narration 🎧

🧩 Story Styles Supported
Style	Description

Comedy	Light and humorous

Thriller	Suspense and tension

Fairy Tale	Magical storytelling

Mythological	Indian myth-inspired

Sci-Fi	Futuristic stories

Mystery	Detective & clues

Adventure	Journey-based story

Romantic	Emotional & love

Horror	Dark & eerie

Morale	Value-based moral story

🔊 Audio Narration

Uses gTTS (Google Text-to-Speech)

Output format: MP3

Automatically streamed in app

Natural voice narration

🛠 Backend Logic

Story Generation

generate_story_from_images(images, style)

Narration

narrate_story(story_text)

⚠️ Common Errors & Fixes

❌ API Key Error

✔ Ensure .env file exists

✔ API key is valid

✔ Restart app after changes

❌ Audio Not Playing

✔ Ensure internet connection

✔ gTTS installed correctly

✔ Story text is not empty

❌ Image Upload Error

✔ Upload only PNG / JPG

✔ Max 10 images

🔐 Security Best Practices

.env added to .gitignore

API keys never hardcoded

Safe for public GitHub repos

🌟 Future Enhancements

🎭 Multiple voice characters

🎵 Background music

🎬 Story-to-video

🌍 Multi-language support

🤖 Emotion-based narration

☁ Cloud deployment

👨‍💻 Author

Satyam

AI & ML Developer

Storytelling + Generative AI Enthusiast

📜 License

This project is for educational and personal use.
Commercial usage requires API permission.
