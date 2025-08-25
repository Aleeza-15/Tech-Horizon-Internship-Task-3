import streamlit as st
import random

st.title("📘 Simple Study Planner 📘")

# Step 1: Ask total time and subjects
total_time = st.number_input("Enter total study time available (in minutes):", min_value=1, step=1)
subjects_input = st.text_area("Enter subjects separated by commas (e.g., Math, Physics, English):")

# Use session_state to store subjects
if "subjects" not in st.session_state:
    st.session_state.subjects = []

if st.button("Next Step ➡️"):
    if total_time > 0 and subjects_input:
        st.session_state.subjects = [s.strip() for s in subjects_input.split(",")]
    else:
        st.warning("Please enter both total time and subjects.")

# Step 2: Show difficulty inputs only if subjects exist
if st.session_state.subjects:
    st.subheader("📊 Assign Difficulty Levels (1=easy, 5=hard):")
    difficulties = []
    for subject in st.session_state.subjects:
        level = st.slider(f"{subject}", min_value=1, max_value=5, value=3, key=subject)
        difficulties.append(level)

    if st.button("Generate Study Plan"):
        total_weight = sum(difficulties)

        st.subheader("📝 Your Study Plan:")
        for i in range(len(st.session_state.subjects)):
            proportion = difficulties[i] / total_weight
            allocated_time = int(proportion * total_time)
            hours = allocated_time // 60
            mins = allocated_time % 60

            if hours > 0:
                st.write(f"- {st.session_state.subjects[i]}: {hours} hr {mins} min")
            else:
                st.write(f"- {st.session_state.subjects[i]}: {mins} min")

        quotes = [
            "Keep going, you are doing great!",
            "Small progress is still progress.",
            "Stay focused, stay determined.",
            "One step at a time leads to success."
        ]
        st.success("💡 Motivation: " + random.choice(quotes))

