import streamlit as st

# Make all object in page full page mode
st.set_page_config(layout='wide')
# Create two perpendicularly columns
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title('Yusif Osmanov')
    content = (
        'There is some important information about me and my life, please read this inforation if you want to know who am i.'
        'There is some important information about me and my life, please read this inforation if you want to know who am i.'
        'Thank you for your attentions!')
    st.info(content)

st.write('Below you can find some of the apps i have built in Python. Feel free to contact me!')
