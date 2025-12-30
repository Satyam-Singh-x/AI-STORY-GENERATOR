import streamlit as st
from Story_generator_fn import generate_story_from_images , narrate_story
from PIL import Image


st.title('AI Story Generator from Images')
st.markdown("Upload 1 to 10 images, choose a style and let AI write and narrate a story for you!")



with st.sidebar:
    st.header('Controls')


    #sidebar option to upload Images
    uploaded_files=st.file_uploader('Upload your images...',type=['png','jpg','jpeg'],accept_multiple_files=True)

    #selecting story style
    story_style= st.selectbox(
        'Choose a story style',
        ('Comedy',"Thriller",'Fairy Tale','Mythological','Sci-fi','Mystery',"Adventure",'Romantic','Horror','Morale')
    )


    #button to generate story
    generate_button= st.button('Generate Story and Narration',type='primary')


#Main logic
if generate_button:
    if not uploaded_files:
        st.warning('Please upload atleast one image')
    elif len(uploaded_files)>10:
        st.warning('Please upload a maximum of 10 images')
    else:
        with st.spinner('The AI is generating your Story and Narration...'):
            try:
                pil_images= [Image.open(uploaded_file) for uploaded_file in uploaded_files]
                st.subheader('Your visual Inspiration: ')
                image_columns= st.columns(len(pil_images))


                for i , image in enumerate(pil_images):
                    with image_columns[i]:
                        st.image(image,width='content')

                generate_story=generate_story_from_images(pil_images,story_style)
                if 'Error' in generate_story or 'failed' in generate_story or 'API KEY' in generate_story:
                    st.error(generate_story)
                else:
                    st.subheader(f'Your {story_style} story: ')
                    st.success(generate_story)


                st.subheader('Listen to your story: ')
                audio= narrate_story(generate_story)

                st.audio(audio,format='audio/mp3')





            except Exception as e:
                st.error(f'An application error occured {e}')














