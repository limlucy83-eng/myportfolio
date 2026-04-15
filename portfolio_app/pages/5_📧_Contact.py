import streamlit.components.v1 as components
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Contact Me", page_icon="📧")

# Custom CSS
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    </style>
""", unsafe_allow_html=True)

st.title("📧 Contact Me")
st.write("Have a question or want to work together? Fill out the form below to send me an email directly.")

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Send a Message")

    # ✅ HTML FORM (CLIENT-SIDE) — WORKS WITH FREE Web3Forms
    st.markdown("""
    <style>
    /* Darker Deep Navy/Charcoal Gradient */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #020617 0%, #0f172a 100%);
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #020617;
    }

    /* Force headers and standard text to be bright white for readability */
    h1, h2, h3, p, span, label {
        color: #ffffff !important;
    }

    /* Styling the link buttons to match the purple theme */
    .stLinkButton > a {
        background-color: #1e293b !important;
        color: white !important;
        border: 1px solid #38bdf8 !important;
    }
    
    .stInfo {
        background-color: #0f172a;
        color: #38bdf8;
        border: 1px solid #38bdf8;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📧 Contact Me")
st.write("Have a question or want to work together? Fill out the form below to send me an email directly.")

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Send a Message")

    # ✅ HTML FORM (CLIENT-SIDE)
    components.html("""
        <style>
            body {
                font-family: 'Inter', Arial, sans-serif;
                background-color: transparent; /* Makes the iframe blend in */
            }

            .form-container {
                background: #f8fafc; /* Slightly off-white for better eye comfort */
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0px 10px 25px rgba(0,0,0,0.3);
                max-width: 100%;
            }

            input, textarea {
                width: 95%;
                padding: 12px;
                margin-top: 8px;
                margin-bottom: 20px;
                border-radius: 8px;
                border: 1px solid #cbd5e1;
                font-size: 15px;
            }

            textarea {
                min-height: 120px;
                resize: vertical;
            }

            button {
                width: 100%;
                background-color: #7c3aed; /* Vibrant Purple */
                color: white;
                border-radius: 10px;
                border: none;
                padding: 12px;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                transition: 0.3s;
            }

            button:hover {
                background-color: #6d28d9;
                transform: translateY(-2px);
            }

            label {
                font-weight: 600;
                color: #1e293b; /* Dark labels for inside the white card */
            }
        </style>

        <div class="form-container">
            <form action="https://api.web3forms.com/submit" method="POST">
                <input type="hidden" name="access_key" value="372abaf0-d753-4c5f-aa36-a3c3d303a8f6">

                <label>Name</label>
                <input type="text" name="name" placeholder="Enter your full name" required>

                <label>Email Address</label>
                <input type="email" name="email" placeholder="Enter your email address" required>

                <label>Message</label>
                <textarea name="message" placeholder="Write your message here..." required></textarea>

                <input type="hidden" name="subject" value="New Contact Form Message">
                <button type="submit">Send Message</button>
            </form>
        </div>
    """, height=520)

with col2:
    st.subheader("Connect with Me")
    st.write("You can also find me here:")

    st.link_button("🌐 GitHub", "https://github.com/RICAY458")
    st.link_button("📱 Facebook", "https://www.facebook.com/carimae.sinogbujan")

    st.markdown("---")
    st.info("📍 **Location:** Masbate, Philippines")