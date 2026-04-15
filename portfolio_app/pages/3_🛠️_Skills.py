import streamlit as st

# Set page configuration
st.set_page_config(page_title="Skills", page_icon="🛠️")

# Custom CSS
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

        /* Essential: Light color for standard text */
        [data-testid="stAppViewContainer"] p, [data-testid="stAppViewContainer"] span, label {
            color: #ffffff !important;
        }

        /* Targets the custom skill labels to be white */
        .skill-label {
            color: #ffffff !important;
            font-weight: 500;
            margin-bottom: 5px;
        }

        /* Headings: Cyan/Electric Blue */
        h1, h2, h3 {
            color: #38bdf8 !important; 
            font-family: 'Inter', sans-serif;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
    </style>
""", unsafe_allow_html=True)

st.title("🛠️ Skills")
st.subheader("💻 Programming")

def display_skill(name, value):
    with st.container():
        # Using the skill-label class we defined in CSS above
        st.markdown(f'<div class="skill-label">{name}</div>', unsafe_allow_html=True)
        st.progress(value)

# Display skills
display_skill("PHP/ XAMMP", 80)
display_skill("Python", 90)
display_skill("HTML / CSS / JAVASCRIPT", 85)

st.write("") 

st.subheader("🎨 Design")
st.markdown("""
    <div class="skill-container">
        <li style="color: #ffffff;">UI/UX Design with a focus on clean, aesthetic layouts</li>
    </div>
""", unsafe_allow_html=True)
