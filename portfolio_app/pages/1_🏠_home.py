import streamlit as st

st.markdown("""
    <style>
        /* Main background with a deeper, smoother gradient */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        }

        /* Sidebar: Solid dark slate for a professional look */
        [data-testid="stSidebar"] {
            background-color: #0f172a;
        }

        /* Essential: Light color for text readability on dark background */
        [data-testid="stAppViewContainer"] p, [data-testid="stAppViewContainer"] span, label {
            color: #f1f5f9 !important;
        }

        /* Headings: Using a bright Cyan/Electric Blue to pop against the dark */
        h1, h2, h3 {
            color: #ffffff !important; 
            font-family: 'Inter', sans-serif;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        /* Styling the Info Box to match the theme */
        .stAlert {
            background-color: #1e293b;
            color: #ffffff;
            border: 1px solid #38bdf8;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🏠 Home")
st.header("Hi, I'm Lucy D. Lim! 👋")
st.write("A passionate CS Student who loves to explore the latest Technologies.")
st.info("I specialize in building systems that are not only visually modern but also functionally robust.")