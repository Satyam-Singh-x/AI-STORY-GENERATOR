import streamlit as st
from Story_generator_fn import generate_story_from_images, narrate_story
from PIL import Image
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import textwrap

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="TaleForge",
    page_icon="📖",
    layout="centered"
)

# --------------------------------------------------
# THEME ENGINE
# --------------------------------------------------
def apply_genre_theme(genre):
    themes = {
        "Comedy": {"bg": "#FFF7E6", "text": "#2B2B2B", "accent": "#FF9800", "anim": "bounce"},
        "Thriller": {"bg": "#0F172A", "text": "#F8FAFC", "accent": "#EF4444", "anim": "fade"},
        "Fairy Tale": {"bg": "#FDF4FF", "text": "#3B0764", "accent": "#C084FC", "anim": "float"},
        "Mythological": {"bg": "#FFF8E1", "text": "#3E2723", "accent": "#D4AF37", "anim": "glow"},
        "Sci-Fi": {"bg": "#020617", "text": "#E0F2FE", "accent": "#22D3EE", "anim": "slide"},
        "Mystery": {"bg": "#111827", "text": "#E5E7EB", "accent": "#A855F7", "anim": "fade"},
        "Adventure": {"bg": "#ECFDF5", "text": "#064E3B", "accent": "#10B981", "anim": "slide"},
        "Romantic": {"bg": "#FFF1F2", "text": "#831843", "accent": "#FB7185", "anim": "float"},
        "Horror": {"bg": "#020617", "text": "#FCA5A5", "accent": "#DC2626", "anim": "shake"},
        "Morale": {"bg": "#F0FDF4", "text": "#14532D", "accent": "#22C55E", "anim": "fade"},
    }

    t = themes.get(genre, themes["Comedy"])

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {t['bg']};
            color: {t['text']};
        }}

        h1,h2,h3,h4,p,span {{
            color: {t['text']} !important;
        }}

        section[data-testid="stSidebar"] {{
            background-color: #0f172a;
        }}

        section[data-testid="stSidebar"] * {{
            color: white !important;
        }}

        .fade {{ animation: fadeIn 1s; }}
        .slide {{ animation: slideUp 1s; }}
        .float {{ animation: float 3s infinite; }}
        .bounce {{ animation: bounce 1s; }}
        .glow {{ animation: glow 2s infinite; }}
        .shake {{ animation: shake 0.4s; }}

        @keyframes fadeIn {{ from {{opacity:0}} to {{opacity:1}} }}
        @keyframes slideUp {{ from {{transform:translateY(30px)}} to {{transform:none}} }}
        @keyframes float {{ 0%{{transform:translateY(0)}}50%{{transform:translateY(-8px)}}100%{{transform:translateY(0)}} }}
        @keyframes bounce {{ 0%{{scale:.95}}50%{{scale:1.05}}100%{{scale:1}} }}
        @keyframes glow {{ 0%{{box-shadow:0 0 5px {t['accent']}}}50%{{box-shadow:0 0 20px {t['accent']}}}100%{{box-shadow:0 0 5px {t['accent']}}} }}
        @keyframes shake {{ 0%{{x:0}}25%{{x:-5px}}50%{{x:5px}}75%{{x:-5px}}100%{{x:0}} }}
        </style>
        """,
        unsafe_allow_html=True
    )

    return t["anim"]

# --------------------------------------------------
# PDF GENERATOR (FIXED)
# --------------------------------------------------
def generate_pdf(title, genre, story, images):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Cover Page
    pdf.setFont("Helvetica-Bold", 26)
    pdf.drawCentredString(width / 2, height - 120, title)
    pdf.setFont("Helvetica", 16)
    pdf.drawCentredString(width / 2, height - 170, f"Genre: {genre}")
    pdf.drawCentredString(width / 2, height - 210, "Generated using TaleForge")
    pdf.showPage()

    # Images
    for img in images:
        img_io = BytesIO()
        img.save(img_io, format="PNG")
        img_io.seek(0)

        pdf.drawImage(
            ImageReader(img_io),
            50, 150,
            width=width - 100,
            height=height - 250,
            preserveAspectRatio=True,
            mask="auto"
        )
        pdf.showPage()

    # Story Pages
    pdf.setFont("Helvetica", 12)
    text = pdf.beginText(50, height - 50)

    wrapped_lines = []
    for para in story.split("\n"):
        wrapped_lines.extend(textwrap.wrap(para, 90))
        wrapped_lines.append("")

    page_no = 1
    for line in wrapped_lines:
        if text.getY() < 50:
            pdf.drawText(text)
            pdf.drawRightString(width - 50, 30, f"Page {page_no}")
            page_no += 1
            pdf.showPage()
            text = pdf.beginText(50, height - 50)
            pdf.setFont("Helvetica", 12)

        text.textLine(line)

    pdf.drawText(text)
    pdf.drawRightString(width - 50, 30, f"Page {page_no}")
    pdf.save()

    buffer.seek(0)
    return buffer

# --------------------------------------------------
# UI
# --------------------------------------------------
st.markdown("""
<div style="text-align:center;">
    <h1>📖 TaleForge</h1>
    <h4>Where Images Turn Into Stories ✨</h4>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

with st.sidebar:
    uploaded_files = st.file_uploader("📷 Upload Images", type=["jpg","png"], accept_multiple_files=True)
    story_style = st.selectbox(
        "🎭 Story Style",
        ["Comedy","Thriller","Fairy Tale","Mythological","Sci-Fi","Mystery","Adventure","Romantic","Horror","Morale"]
    )
    generate = st.button("✨ Generate Story")

anim = apply_genre_theme(story_style)

# --------------------------------------------------
# MAIN LOGIC
# --------------------------------------------------
if generate:
    if not uploaded_files:
        st.warning("Upload at least one image.")
    else:
        with st.spinner("✨ Creating your story..."):
            images = [Image.open(f) for f in uploaded_files]

            st.markdown(f"<div class='{anim}'><h2>🖼 Visuals</h2></div>", unsafe_allow_html=True)
            cols = st.columns(len(images))
            for i, img in enumerate(images):
                cols[i].image(img, use_container_width=True)

            story = generate_story_from_images(images, story_style)

            st.markdown(f"<div class='{anim}'><h2>📜 Your Story</h2></div>", unsafe_allow_html=True)
            st.success(story)

            st.markdown("### 🔊 Narration")
            st.audio(narrate_story(story), format="audio/mp3")

            pdf = generate_pdf("TaleForge Story", story_style, story, images)

            st.download_button(
                "📄 Download Story as PDF",
                pdf,
                file_name="TaleForge_Story.pdf",
                mime="application/pdf"
            )

st.markdown("<hr><center>✨ Built with ❤️ using Streamlit & AI · TaleForge © 2025</center>", unsafe_allow_html=True)
