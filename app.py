import streamlit as st
import pandas as pd
import os

DATA_FILE = "baby_vicky_data.csv"

st.set_page_config(page_title="Baby VICKY – Vocal Mentorship")
st.title("🍼 Baby VICKY – Find Your Voice Mentor!")

st.markdown("Fill out this form to find or become a vocal mentor. Baby VICKY is here to help you grow!")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
level = st.selectbox("Skill Level", ["Beginner", "Intermediate", "Advanced"])
role = st.radio("I'm interested in:", ["Finding a Mentor", "Becoming a Mentor", "Both"])
goals = st.text_area("Your Vocal Goals")
availability = st.text_input("When are you usually available? (e.g. weekends, evenings)")

if st.button("Submit"):
    new_entry = pd.DataFrame([[name, email, level, role, goals, availability]],
                             columns=["Name", "Email", "Level", "Role", "Goals", "Availability"])
    
    if os.path.exists(DATA_FILE):
        existing = pd.read_csv(DATA_FILE)
        updated = pd.concat([existing, new_entry], ignore_index=True)
    else:
        updated = new_entry

    updated.to_csv(DATA_FILE, index=False)
    st.success("Thanks! Baby VICKY added you to the mentorship list 👶🎤")

# Admin view
if st.checkbox("👀 Show List of Interested Singers"):
    if os.path.exists(DATA_FILE):
        data = pd.read_csv(DATA_FILE)
        st.dataframe(data)
    else:
        st.info("No entries yet.")
