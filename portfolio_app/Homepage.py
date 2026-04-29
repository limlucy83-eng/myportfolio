import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="💻")

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

        /* Main Welcome Title - Forced to Bright White */
        h1 {
            color: #ffffff !important;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            font-size: 30px;
            font-family: 'Inter', sans-serif;
        }

        /* Subtitles and Body Text */
        h2, h3, p, li, [data-testid="stMarkdownContainer"] {
            color: #f1f5f9 !important;
        }

        /* Section List Box */
        .stCodeBlock, div[data-testid="stVerticalBlock"] > div:nth-child(3) {
            background-color: #1e293b !important;
            border: 1px solid #38bdf8;
            border-radius: 10px;
        }
        
        /* Select a page instruction text */
        .stAlert {
            background-color: #1e293b;
            color: #38bdf8;
            border: 1px solid #38bdf8;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Welcome to My Professional Portfolio")

st.write("Navigate through the sidebar to learn more about my work and skills.")

st.info("Select a page above to get started about me!")
