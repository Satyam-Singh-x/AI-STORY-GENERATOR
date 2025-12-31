📖 TaleForge — AI Story Generator from Images

TaleForge is an AI-powered storytelling application that transforms images into beautifully written stories with narration, themed UI, and downloadable story PDFs.

Built using Streamlit, Google Gemini, and Python, TaleForge blends creativity, design, and AI into a polished storytelling experience.



✨ Features

✅ Generate stories from images using AI

✅ Multiple genres (Comedy, Thriller, Fairy Tale, Mythology, etc.)

✅ Beautiful animated UI with dynamic themes

✅ AI-powered narration (Text-to-Speech)

✅ Download stories as professionally formatted PDFs

✅ Image previews inside PDFs

✅ Automatic page numbering

✅ Clean & responsive interface

✅ Secure API handling using .env

🎭 Supported Story Genres

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

Each genre dynamically changes:

Theme colors

Animations

Story tone



🖥️ Tech Stack

Layer	Technology

Frontend	Streamlit

AI Model	Google Gemini

Image Processing	Pillow

Text-to-Speech	gTTS

PDF Generation	ReportLab

Styling	CSS (embedded)

Environment	Python + dotenv



📁 Project Structure

TaleForge/

│
├── app.py                     # Main Streamlit application

├── Story_generator_fn.py      # AI logic & narration

├── requirements.txt

└── README.md


⚙️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/Satyam-Singh-x/AI-STORY-GENERATOR.git

cd AI-STORY-GENERATOR

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set Up Environment Variables

Create a .env file:

GOOGLE_API_KEY=your_gemini_api_key_here


⚠️ Never upload your .env file to GitHub

4️⃣ Run the App

streamlit run app.py

🧠 How It Works

Upload 1–10 images

Choose a story genre

AI analyzes images and generates a story

Story is narrated using TTS

Story + images exported as a PDF

Theme changes dynamically based on genre

📄 PDF Features

✔ Cover page with title

✔ Embedded images

✔ Multi-page story formatting

✔ Page numbers

✔ Clean typography

🔊 Narration

Narration is generated using Google Text-to-Speech (gTTS) and plays directly in the browser.

🎨 UI Highlights

Dynamic theme switching

Animated transitions

Dark sidebar with readable contrast

Responsive layout

Clean typography



🔐 Security

API keys loaded via .env

.env should be added to .gitignore

No credentials hardcoded

🚀 Future Improvements

🎧 Voice selection

🌍 Multi-language support

🧠 Story memory

📱 Mobile optimization

🎬 Story-to-video generation

☁️ Cloud deployment



🧑‍💻 Author

Satyam

AI Developer | Storytelling Enthusiast | Full-Stack Learner

“Turning imagination into experience using AI.”

⭐ If You Like This Project

⭐ Star this repository

🍴 Fork it

📢 Share it

💡 Contribute ideas
