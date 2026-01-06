import streamlit as st
import google.generativeai as genai
import  os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv('GENAI_API_KEY'))
st.title('🎥Movie Recommendation Sytem🎥')
user_input=st.text_input('Enter the movie name')
submit=st.button('click here')
# if submit:
#     st.markdown('Movie name has been entered')
# else:
#     st.warning('no movie entered yet.......')
model=genai.GenerativeModel('gemini-2.5-flash-lite')
if submit and user_input.strip():
    st.markdown(f'movie name entered:{user_input}')
    response= model.generate_content(f'geneerate Movie recomendation releated to {user_input} ')
    st.write(f'Related Recommendations:\n {response.text}')
else:
    st.write('Please enter a movie name to get recommendations.')


