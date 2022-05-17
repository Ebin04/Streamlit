import streamlit as st

import sqlite3
conn= sqlite3.connect('data.db',check_same_thread=False)
cur=conn.cursor()



def form():  
    st.header('HVAC Request Interface')
    st.write('Raise Your Request Here')
  
    with st.form(key='Info form'):
        
        loc=st.selectbox('Office Location', ['Phase 1', 'Phase 2','Central block'])
        
        comfort=st.selectbox('Your Current thermal Sensation ?', ['Too Cool', 'Cool','Slightly cool',
        'Just fine','Slightly warm','Hot','Too Hot'])
        
        submission=st.form_submit_button(label='Submit')
        
        if submission==True:
            addData(loc,comfort)
            


def addData(a,b):
    cur.execute("""CREATE TABLE IF NOT EXISTS hvac_current(Room TEXT(50),Current_Comfort TEXT(79));""")
    cur.execute("INSERT INTO hvac_current VALUES(?,?)",(a,b))
    conn.commit()
    conn.close()
    st.success('Submission Success! ')

names = ['Leo', 'Luffy']
form()
