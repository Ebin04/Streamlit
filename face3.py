import streamlit as st

def form():  
    st.header('HVAC Request Interface')
    st.write('Raise Your Request Here')
  
    with st.form(key='Info form'):
        from PIL import Image
        image = Image.open('E:\Downloads\imageshvac.jfif')
        st.image(image, caption='Office Architecture',width=700)
        Room_Number=st.number_input("Enter Room Number: ",min_value=0,max_value=5)
        
        
        st.slider(label="Comfort Level",min_value=-3,max_value=3)
        submission=st.form_submit_button(label='Submit')
        
        if submission==True:
            st.success('Submission Success! ')

form()
