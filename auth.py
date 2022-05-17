import streamlit as st
import streamlit_authenticator as stauth
def form():  
    st.header('HVAC Request Interface')
    st.write('Raise Your Request Here')
  
    with st.form(key='Info form'):
        
        st.selectbox('Office Location', ['Phase 1', 'Phase 2','Central block'])
        
        st.selectbox('Your Current thermal Sensation ?', ['Too Cool', 'Cool','Slightly cool',
        'Just fine','Slightly warm','Hot','Too Hot'])
        
        submission=st.form_submit_button(label='Submit')
        
        if submission==True:
            st.success('Submission Success! ')


names = ['Leo', 'Luffy']
usernames = ['Leo120', 'Luffy']
passwords = ['123', '456']
hashed_passwords = stauth.Hasher(passwords).generate()
authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write('Welcome *%s*' % (name))
    form()
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
