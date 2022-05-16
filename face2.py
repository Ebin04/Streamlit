import streamlit as st

def form():  
    st.header('HVAC Request Interface')
    
  
    with st.form(key='Info form'):
        from PIL import Image
        image = Image.open('E:\Downloads\imageshvac.jfif')
        st.image(image, caption='Office Architecture',width=700)
        Room_Number=st.number_input("Enter Room Number: ",min_value=0,max_value=5)
        st.write('How do you feel?')
        st.checkbox(label="Too cold")
        st.checkbox(label="Cold")
        st.checkbox(label="Slightly Cold")
        st.checkbox(label="Just Fine")
        st.checkbox(label="Slightly Warm")
        st.checkbox(label="Warm")
        st.checkbox(label="Too Hot")

        
        submission=st.form_submit_button(label='Submit')
        
        if submission==True:
            st.success('Submission Success! ')

form()