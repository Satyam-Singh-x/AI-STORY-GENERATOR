from dotenv import load_dotenv
import os
from google import genai
from gtts import gTTS
from io import BytesIO

load_dotenv()
api_key=os.getenv('GOOGLE_API_KEY')
if not api_key:
    raise ValueError('API key not found.')

client=genai.Client(api_key=api_key)


def create_advanced_prompt(style):
    #----base prompt----------
    base_prompt= f"""
    **Your persona:** You are a friendly and engaging storyteller. Your goal is to tell a story that is fun and easy to read.
    **Your Main Goal:** Write a story in simple, clear , and modern English.
    **Your task:** Create one single story that connects all the provided images in order.
    **Style Requirement:** The story must fit in the '{style}' genre.
    **Core instructions:** 
    1. **Tell one simple heart warming story:** connect all images into a narrative with a beginning middle and end.
    2. ** Use every image**: Include a key detail of each provided image.
    3. **Creative Interpretation:** Infer the relationships between the images.
    4. **Nationality:** Use only indian names , characters,persona,culture, places etc.
    **OUTPUT FORMAT: **
    -- **TITLE:** Start with  a simple and clear title.
    -- **length:** The story must be between 4 to 5 paragraphs.
    """

    #Add Style-specific instructions--
    style_instructions=""
    if style == 'Morale':
        style_instructions="\n**Special Section:** After the story , you must add a section starting with the exact tag '[MORAL]:' followed by the single line moral of the story."
    if style =='Mystery':
        style_instructions="\n**Special Section:** After the story , you must add a section starting with the exact tag '[SOLUTION]:' revealing the culprit and the key clue."
    if style =='Horror':
        style_instructions="\n**Add intense horror scenes and sounds that creates intense vibes."
    if style =='Thriller':
        style_instructions="\n**Special Section:** After the story , you must add a section starting with the exact tag '[TWIST]:' that reveals the final shocking twist  ."

    return base_prompt+style_instructions







#function -- images ,style --> STORY + NARRATION
def generate_story_from_images(images,style):
    response=client.models.generate_content(
        model='gemini-2.5-flash-lite',
        contents=[images,create_advanced_prompt(style)]

    )
    return response.text


#function -- story --- audio file
def narrate_story(story_text):
    try:
        tts=gTTS(text=story_text, lang='en', slow=False)
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        return audio_fp
    except Exception as err:
        return f'An error occurred: {err}'





