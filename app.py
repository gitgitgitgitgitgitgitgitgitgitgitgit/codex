import streamlit as st



import time
st.title("codex")
name = (" ")
codename = st.text_input("what is your codename")
password = (".")
password_input = (" ")
logged_in = (" ")
sb = (" ")
missons = ["you have no missons ass you are not sined in"]
rank = (" ")
age = (" ")
id = (" ")

if codename == ("m7007"):
    st.success("Success")
    name = ("Mischa Nelson")
    password = ("mn7007!!!")
    missons = []
    rank = 1
    age = 8
    id = 1779409
    st.write("hello " + codename)
elif codename == ("q468"):
    st.success("Success")
    rank = 30
    password = ("1234")
    missons = ["testing q468", rank, " hell0p"]
    age = 8
    st.write("hello " + codename)
elif codename == (""):
    st.write(" ")
else:
    st.error(" that is not echo name in a database")

password_input = st.text_input("what is the password")
if password_input == password:
    st.success("password correct")
    logged_in = ("true")
elif password_input == (""):
    st.write(" ")
    logged_in = (" ")
else:
    st.error("incorrect passcode")




sb = st.text_input("............")
if sb == ("missons"):
  st.info("here are your missons")
  st.info(missons)
elif sb == ("codes") and logged_in == ("true"):
  st.markdown("https://sites.google.com/view/codex-codes/home")
elif sb == ("help"):
  st.markdown("here is a list of commands that you can do missons codes case study   spy crafts spy dictionary help ")
elif sb == ("case study") and logged_in == ("true"):
  st.markdown("https://sites.google.com/view/poafdsgjoaj/home")
elif sb == ("history of spying") and logged_in == ("true"):
  st.markdown("https://sites.google.com/view/poafdsgjoaj/history-of-spying?authuser=0")
elif sb == ("spy crafts") and logged_in == ("true"):
  st.markdown("https://sites.google.com/view/poafdsgjoaj/spy-crafts?authuser=0")
elif sb == ("spy dictionary") or sb == ("sd") and logged_in == ("true"):
  st.markdown("https://sites.google.com/view/poafdsgjoaj/spy-dictionary")
elif sb == ("lesson one") or ("lesson 1") and logged_in == ("true"):
  st.markdown("yo")
