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

        /* FORCE WHITE TEXT: Targets all standard text and list items */
        [data-testid="stAppViewContainer"] p, 
        [data-testid="stAppViewContainer"] li, 
        [data-testid="stAppViewContainer"] span, 
        label {
            color: #ffffff !important;
        }

        /* Headings: Bright White/Off-White */
        h1, h2, h3 {
            color: #f1f5f9 !important; 
            font-family: 'Inter', sans-serif;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        /* Info Box Styling */
        .stAlert {
            background-color: #1e293b;
            color: #ffffff !important;
            border: 1px solid #38bdf8;
        }
        
        /* Ensures text inside info boxes is also white */
        .stAlert p {
            color: #ffffff !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("👤 About Me")
st.info("I am a Junior Full-Stack Developer focused on bridging the gap between robust system architecture and high-fidelity user experiences.")

st.subheader("🎓 Education")
st.info("- BS in Computer Science, DEBESMSCAT - PRESENT 2023")

st.subheader("🚀 Goals")
st.info("- Full Stack web Developer ")
st.info("- Eagerly refining my technical toolkit to evolve from a passionate student into a professional-grade systems developer.")