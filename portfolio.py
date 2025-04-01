import streamlit as st
import smtplib
from email.message import EmailMessage
from PIL import Image

st.markdown("""
    <style>
    .main { background-color: #f5f5f5; font-family: Arial, sans-serif; }
    .header { text-align: center; color: #4CAF50; font-size: 50px; font-weight: bold; }
    .subheader { text-align: center; color: #333333; font-size: 20px; margin-bottom: 30px; }
    .section-title { color: #4CAF50; font-size: 30px; margin-top: 30px; margin-bottom: 10px; }
    .project-card { background-color: #ffffff; padding: 15px; border-radius: 10px; 
                    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); margin-bottom: 20px; }
    .contact-form input, .contact-form textarea { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; }
    .contact-form button { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
    .contact-form button:hover { background-color: #45a049; }
    .social-icons { text-align: center; margin-top: 30px; }
    .social-icons a { margin: 0 10px; text-decoration: none; }
    </style>
""", unsafe_allow_html=True)


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Services", "Projects", "Contact Me"])


if page == "Home":
    st.markdown('<div class="header">Welcome to My Portfolio</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Hi, I am Muhammad Saad, a passionate Flutter, SQL, Web Developer with ML enthusiasm.</div>', unsafe_allow_html=True)
    st.write("I specialize in building ML models, web apps, and solving real-world problems using technology.")


elif page == "Services":
    st.markdown('<div class="section-title">Services</div>', unsafe_allow_html=True)
    st.write("""
    - **Web Development**: Building responsive and scalable web applications.
    - **Machine Learning**: Developing predictive models and AI solutions.
    - **Data Analysis**: Extracting insights from data to drive business decisions.
    - **Flutter Development**: Creating cross-platform mobile applications.
    """)


elif page == "Projects":
    st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)
    
 
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.subheader("Project 1: Machine Learning Models")
    st.write("Worked on Regression, Classification, and currently learning Deep Learning.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.subheader("Project 2: Sentiment Analysis")
    st.write("NLP-based project analyzing user sentiment as Positive, Negative, or Neutral.")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Contact Me":
    st.markdown('<div class="section-title">Contact Me</div>', unsafe_allow_html=True)
    st.write("Feel free to reach out for collaboration or inquiries!")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")
        
        if submitted:
            try:
                msg = EmailMessage()
                msg.set_content(f"Name: {name}\nEmail: {email}\nMessage: {message}")
                msg["Subject"] = "New Contact Form Submission"
                msg["From"] = "your_email@gmail.com"  
                msg["To"] = "your_email@gmail.com" 
                
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login("saad176pak@gmail.com", "Pvtbmsaadi1549")  
                    server.send_message(msg)
                
                st.success(f"Thank you, {name}! Your message has been sent.")
            except Exception as e:
                st.error("Error sending email. Please try again later.")

st.markdown("""
<div class="social-icons">
    <a href="https://github.com/saadi076/portfolio" target="_blank"><img src="https://img.icons8.com/ios-glyphs/30/github.png"/></a>
    <a href="mailto:saad176pak@gmail.com"><img src="https://img.icons8.com/ios-glyphs/30/gmail.png"/></a>
    <a href="https://web.facebook.com/profile.php?id=100078128845085" target="_blank"><img src="https://img.icons8.com/ios-glyphs/30/facebook.png"/></a>

</div>
""", unsafe_allow_html=True)

st.sidebar.markdown('<div class="subheader">© 2025 Muhammad Saad. All rights reserved.</div>', unsafe_allow_html=True)
