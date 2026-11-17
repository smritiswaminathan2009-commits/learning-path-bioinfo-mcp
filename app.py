import streamlit as st
from core import generate_path

st.title("Learning Path Generator")
topic = st.text_input("Topic", "bioinformatics")
level = st.selectbox("Level", ["beginner", "intermediate", "advanced"])
weeks = st.slider("Weeks", 2, 12, 4)

if st.button("Generate"):
    for step in generate_path(topic, level, weeks)["plan"]:
        st.subheader(f"Week {step['week']}: {step['focus']}")
        st.write(f"📚 {step['resource']}")
        st.caption(step["goal"])
