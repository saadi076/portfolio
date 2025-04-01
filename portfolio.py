import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        font-family: Arial, sans-serif;
    }
    .header {
        text-align: center;
        color: #4CAF50;
        font-size: 50px;
        font-weight: bold;
    }
    .subheader {
        text-align: center;
        color: #333333;
        font-size: 20px;
        margin-bottom: 30px;
    }
    .section-title {
        color: #4CAF50;
        font-size: 30px;
        margin-top: 30px;
        margin-bottom: 10px;
    }
    .project-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .contact-form input, .contact-form textarea {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    .contact-form button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .contact-form button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Services", "Projects", "Contact Me"])

# Home Page
if page == "Home":
    st.markdown('<div class="header">Welcome to My Portfolio</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Hi, I am Myhammad Saad, a passionate Flutter,SQL,Web develepor with basics and machine learning enthusiast.</div>', unsafe_allow_html=True)
    st.write("""
    I specialize in building ML models and solving real-world problems using technology. 
    I love learning new tools and frameworks to stay updated in this fast-paced tech world.
    """)

# Services Page
elif page == "Services":
    st.markdown('<div class="section-title">Services</div>', unsafe_allow_html=True)
    st.write("""
    - **Web Development**: Building responsive and scalable web applications.
    - **Machine Learning**: Developing predictive models and AI solutions.
    - **Data Analysis**: Extracting insights from data to drive business decisions.
    - **Flutter Developer**: Currently learning and working on some projects
    """)

# Projects Page
elif page == "Projects":
    st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)

    # Project 1
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.subheader("Project 1: ML(Machine Learning)")
    st.write("""
    I have done some projects base on single,multi regression,Classification. Now learning DL.
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Project 2
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.subheader("Project 2: Sentiment Analysis using ML")
    st.write("""
    A simple project that analyzes the sentiment of user-provided text using natural language processing (NLP). 
    It provides insights into whether the sentiment is positive, negative, or neutral.
    """)
  
    st.markdown('</div>', unsafe_allow_html=True)

# Contact Me Page
elif page == "Contact Me":
    st.markdown('<div class="section-title">Contact Me</div>', unsafe_allow_html=True)
    st.write("Feel free to reach out to me for collaboration or any inquiries!")

    # Contact Form
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success(f"Thank you, {name}! Your message has been sent.")

# Footer
st.sidebar.markdown('<div class="subheader">© 2025 Muhammad Saad. All rights reserved.</div>', unsafe_allow_html=True)