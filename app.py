import streamlit as st
import streamlit.components.v1 as components
import time
import random
st.title("codex")
name = (" ")
codename = ("no")
logged_in = (False)
sb = ("START")
missons = [""]
rank = (" ")
age = (" ")
id = (" ")
lvl_10_passcode = ("4462")

codenames = [
    {
        "codename": "M7007",
        "name": "Mischa Nelson",
        "password": "mn7007!!!",
        "rank": 1,
        "age": 8,
        "id": 1779409,
        "missons": [],
    },
    {
        "codename": "Q468",
        "name": "Alex Zimmerman",
        "password": "1234",
        "rank": 30,
        "age": 8,
        "id": 8819230,
        "missons": ["Misson_2231.Q468"],
    }
]

codename = st.text_input("What is your codename?")

if codename == "":
    st.write("Please enter a codename.")
else:
    user = next((user for user in codenames if user["codename"] == codename), None)

    if user is None:
        st.error("That is not a codename in our database.")
    else:
        st.success("Success")
        password_input = st.write_secret("What is the password?")

        if password_input == "":
            st.write("Please enter a password.")
        elif password_input != user["password"]:
            st.error("Incorrect password.")
            logged_in = (False)
        else:
            st.success("Password correct")
            logged_in = (True)
            st.write(f"Hello, {user['codename']}")



def hack():
    st.title("Hacking Tool")

    hhusername = st.text_input("Enter the username:")
  
    st.write("your username is that you want to hack is " + hhusername)
    if hhusername in [mn7007, Q468, ]:
      print("")
    else:
      if st.button("Hack"):
          st.write("Hacking...")
          # simulate a long hacking process
          st.title("Progress Report")

          for i in range(1, 101):
             st.write(f"{i}% done")
             time.sleep(0.3)
         
          if random.randint(0, 1) == 0:
             st.success("Access granted!")
          else:
              st.error("Access denied please try again")
 

if logged_in == (True):
  sb = st.text_input("....................")  
if sb == ("Missons"):
  st.info("here are your missons")
  st.info(missons)
elif sb == ("Codes"):
  st.markdown("https://sites.google.com/view/codex-codes/home")
elif sb == ("Help"):
  st.markdown("here is a list of commands that you can do Missons, Codes, Lesson one - Lesson five, Spy dictionary, Help and Help more")
elif sb == ("Help more"):
  st.markdown("here is some more advanced list of commands that you can do the first is username.password, this will show all of your info.")
elif sb == ("Spy dictionary"):
  st.markdown("https://sites.google.com/view/poafdsgjoaj/spy-dictionary")
elif sb == ("Morsecode"):
 components.iframe("https://embed.morsedecoder.com", width=800, height=170)
elif sb == ("Hacking." +lvl_10_passcode):
  hack()
elif sb in ["Q468.1234", "Q468.1111"]:
  st.markdown("name " + name + " rank " + str(rank) + " id " + str(id) + " age " + str(age))
  st.markdown("here are your missons")
  st.markdown(missons)
elif sb == ("M7007.1111"):
  st.markdown("name " + name + " rank " + str(rank) + " id " + str(id) + " age " + str(age))
  st.markdown(missons)
elif sb == ("Launch.999"):
  st.markdown("launch missile to stop search Cancel launch")
  st.text_input("were do you want to launch the missile if left blank missile will fire at testing zone")
  st.components.v1.html(
  """"  
  <html>
  <head>
    <style>
      body {
        background-color: black;
      }
      
      button {
        color: red;
        font-size: 24px;
        font-weight: bold;
      }
      
      #timer {
        color: white;
        font-size: 36px;
        font-weight: bold;
      }
    </style>
  </head>
  <body>
    <button onclick="startTimer()">Launch</button>
    <div id="timer"></div>
    
    <script>
      function startTimer() {
        // Hide the button
        document.querySelector("button").style.display = "none";
        
        // Show the timer
        document.querySelector("#timer").innerHTML = "4:00";
        
        // Start the timer
        var seconds = 240;
        var timer = setInterval(function() {
          // Update the timer display
          document.querySelector("#timer").innerHTML = Math.floor(seconds / 60) + ":" + (seconds % 60);
          
          // Decrement the timer
          seconds--;
          
          // Stop the timer when it reaches 0
          if (seconds == 0) {
            clearInterval(timer);
          }
        }, 1000);
        
        // Start flashing the background
        var isRed = false;
        setInterval(function() {
          if (isRed) {
            document.querySelector("body").style.backgroundColor = "black";
          } else {
            document.querySelector("body").style.backgroundColor = "red";
          }
          isRed = !isRed;
        }, 500);
      }
    </script>
  </body>
</html>
"""
, width=None, height=None, scrolling=False)
  
elif sb == ("Cancel launch"):
  st.components.v1.html(
  """"  
<html>
  <head>
    <style>
      body {
        background-color: black;
      }
      
      button {
        color: green;
        font-size: 24px;
        font-weight: bold;
      }
      
      #message {
        color: white;
        font-size: 24px;
        font-weight: bold;
        display: none;
      }
    </style>
  </head>
  <body>
    <button onclick="cancelLaunch()">Cancel Launch</button>
    <div id="message">Canceled Launch</div>
    
    <script>
      function cancelLaunch() {
        // Hide the button
        document.querySelector("button").style.display = "none";
        
        // Change the background color
        document.querySelector("body").style.backgroundColor = "green";
        
        // Show the message
        document.querySelector("#message").style.display = "block";
      }
    </script>
  </body>
</html>

"""
, width=None, height=None, scrolling=False)

elif sb == ("START"):
  st.markdown(" ")
elif sb == ("Misson_2231.Q468"):
  st.markdown("test")
elif sb == (""):
  st.markdown(" ")
else:
  st.markdown("type here the command that you want to do. If you dont know the commands then type Help case sensitive")
  