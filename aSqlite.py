import streamlit as st

import sqlite3
conn= sqlite3.connect('https://github.com/Ebin04/Streamlit/blob/main/ComfortData.db',check_same_thread=False)
cur=conn.cursor()



def form():  
    st.header('HVAC Request Interface')
    st.write('Raise Your Request Here')
  
    with st.form(key='Info form'):
        
        loc=st.selectbox('Office Location', ['Phase 1', 'Phase 2','Central block'])
        
        comfort=st.selectbox('Your Current thermal Sensation ?', ['Too Cool', 'Cool','Slightly cool',
        'Just fine','Slightly warm','Hot','Too Hot'])
        Date=st.date_input("Date")
        time=st.time_input("Time")
        date=str(Date)
        time=str(time)
        submission=st.form_submit_button(label='Submit')
        
        if submission==True:
            addData(date,time,loc,comfort)
            


def addData(a,b,c,d):
    cur.execute("""CREATE TABLE IF NOT EXISTS hvac_current(Date TEXT(50),Time TEXT(70) ,Room TEXT(50),Current_Comfort TEXT(79));""")
    cur.execute("INSERT INTO hvac_current VALUES(?,?,?,?)",(a,b,c,d))
    conn.commit()
    conn.close()
    st.success('Submission Success! ')


form()
