import streamlit as st

st.markdown("""
    <style>
        /* Main background */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #0f172a;
        }

        /* --- THE HEADER BOX FIX: Turning Project Headers Black --- */
        /* This targets the clickable part of the expander */
        div[data-testid="stExpander"] summary {
            background-color: #000000 !important;
            color: #ffffff !important;
            border-radius: 10px 10px 0px 0px; /* Rounds the top corners */
        }

        /* This ensures the title text (FitCalc, etc.) stays white */
        div[data-testid="stExpander"] summary p {
            color: #ffffff !important;
            font-weight: bold;
        }

        /* The content area below the header when opened */
        div[data-testid="stExpanderDetails"] {
            background-color: #111827 !important; /* Slightly lighter than black for contrast */
            border-radius: 0px 0px 10px 10px;
        }

        /* General Text Color */
        [data-testid="stAppViewContainer"] p, 
        [data-testid="stMarkdownContainer"] p,
        label {
            color: #ffffff !important;
        }

        /* Headings: Cyan/Electric Blue */
        h1, h2, h3 {
            color: #38bdf8 !important; 
            font-family: 'Inter', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📂 My Projects")

projects = {
    "FitCalc": "A digital platform designed to provide users with an instant assessment of their body composition.",
    "Hotel Reservation System": "A digital platform designed to manage and automate the lifecycle of a guest's stay—from the initial booking to the final checkout.",
}

for name, desc in projects.items():
    with st.expander(name):
        # Using st.markdown inside the expander ensures the CSS targets it correctly
        st.markdown(desc)