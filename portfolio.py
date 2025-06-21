import streamlit as st
from PIL import Image
import smtplib
from email.message import EmailMessage

st.set_page_config(page_title="Muhammad Saad | Professional Portfolio", layout="wide", initial_sidebar_state="expanded")

option = st.sidebar.radio("Reach Out:", ["Home", "About", "Projects", "Contact Me"])

if option == "Home":
    st.title("👋 Welcome to My Professional Portfolio")
    st.subheader("Muhammad Saad")
    st.markdown("### 🚀 Machine Learning Specialist | Flutter & Python Developer")

    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            image = Image.open(r"C:\Users\DELL\Desktop\Vs code program\saadi.jpeg")
            st.image(image, width=200, caption="Muhammad Saad")
        except FileNotFoundError:
            st.error("Profile image not found.")

    with col2:
        st.markdown("""
        I am a results-driven software engineer with expertise in:
        - 🔍 **Machine Learning & AI**: Building predictive models using Python, scikit-learn, TensorFlow, and pandas.
        - 📱 **Mobile Development**: Creating cross-platform applications with Flutter for seamless user experiences.
        - 🖥️ **Full-Stack Web Development**: Designing responsive interfaces with HTML, CSS, and JavaScript.
        - 🧠 **Data Analysis & Visualization**: Transforming data into actionable insights with advanced visualization tools.

        My mission is to develop intelligent, scalable, and user-centric solutions that drive innovation.
        """)

    st.divider()

    st.markdown("## 🧰 Technical Expertise")
    skills = {
        "Programming Languages": "Python, Dart, JavaScript, C++",
        "Frameworks & Libraries": "Flutter, Django, Streamlit, scikit-learn, TensorFlow, Keras, pandas, numpy, matplotlib",
        "Tools & Platforms": "Git, Visual Studio Code, Google Colab, Firebase, Jupyter Notebook"
    }

    for category, skill_list in skills.items():
        st.markdown(f"**{category}:** {skill_list}")

    st.divider()
    st.success("Thank you for exploring my portfolio! Use the sidebar to learn more.")

elif option == "About":
    st.title("🧑 About Me")
    st.markdown("""
    I am Muhammad Saad, a dedicated software engineer with a passion for leveraging machine learning and mobile development to solve complex challenges.

    - 🎓 **Education**: Bachelor of Science in Computer Science
    - 💡 **Interests**: Artificial Intelligence, Automation, Mobile App Development, and Cloud Integration
    - 🌐 **GitHub**: [github.com/saadi076](https://github.com/saadi076)
    - 📚 **Current Learning**: Deep Learning, API Engineering, and Cloud-Native Development
    - 🎯 **Professional Goal**: To lead transformative projects as a Machine Learning Engineer and App Developer
    """)

elif option == "Projects":
    st.title("💼 Selected Projects")
    st.markdown("### A Showcase of My Work")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🏠 House Price Prediction")
        st.caption("Developed a regression model using scikit-learn to accurately predict house prices based on feature engineering and data preprocessing.")

    with col2:
        st.markdown("### 🍷 Wine Quality Classifier")
        st.caption("Implemented multiple classification algorithms (KNN, Decision Trees, Random Forest, SVM) to evaluate wine quality with high accuracy.")

    with col3:
        st.markdown("### 📊 Data Visualization Suite")
        st.caption("""
        - **Matplotlib**: Designed trend-focused visualizations for data analysis.
        - **Seaborn**: Created statistical graphics for deeper insights.
        - **Plotly**: Built interactive dashboards for dynamic data exploration.
        """)

    st.markdown("Discover more projects on my [GitHub](https://github.com/saadi076).")

elif option == "Contact Me":
    st.title("📬 Contact Me")
    st.markdown("Connect with me through the following platforms or send a direct message below:")

    st.markdown("""
    - 📧 **Email**: [saad176pak@gmail.com](mailto:saad176pak@gmail.com)
    - 💬 **WhatsApp**: [+92 303 3805775](https://wa.me/923033805775)
    - 💼 **Facebook**: [Muhammad Saad](https://web.facebook.com/?_rdc=1&_rdr)
    """)

    st.divider()
    st.markdown("### 📩 Send a Message")

    with st.form("contact_form"):
        name = st.text_input("Full Name", placeholder="Enter your full name")
        email = st.text_input("Email Address", placeholder="Enter your email address")
        subject = st.text_input("Subject", placeholder="Enter the subject of your message")
        message = st.text_area("Message", placeholder="Type your message here")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            if name and email and subject and message:
                try:
                    msg = EmailMessage()
                    msg['Subject'] = f"Portfolio Contact: {subject}"
                    msg['From'] = "your_email@gmail.com"  # Replace with your sender email
                    msg['To'] = "saad176pak@gmail.com"
                    msg.set_content(f"""
                    New message from portfolio website:

                    Name: {name}
                    Email: {email}
                    Subject: {subject}
                    
                    Message:
                    {message}
                    """)

                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login("saad176pak@gmail.com", "ieyt fcim wycr cinf")  # Replace with your email and app-specific password
                    server.send_message(msg)
                    server.quit()

                    st.success(f"Thank you, {name}! Your message has been sent successfully.")
                except Exception as e:
                    st.error(f"Failed to send message. Please try again or contact me directly.")
            else:
                st.error("Please fill out all fields before submitting.")