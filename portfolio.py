import streamlit as st
from PIL import Image

st.set_page_config(page_title="Annu Priya | Portfolio", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Me", "Projects", "Skills", "Resume", "Achievements", "Contact"])

# About
if page == "About Me":
    st.title("👩 Hi, I'm Annu Priya")
    image = Image.open("assets/Annu.png")
    st.image(image, width=150)
    st.write("""
    I’m a B.Tech graduate in Information Technology from Bengal Institute of Technology.  
    I enjoy solving problems with Python, analyzing data with SQL, and visualizing it using Power BI.  
    I have hands-on experience in Python, SQL, PySpark, Deep Learning (CNN), and Databricks.
    """)

# Projects
elif page == "Projects":
    st.title("📈 Projects")

    st.subheader("1. Sales Analysis Dashboard")
    st.write("🔧 Tech: Power BI, SQL, Python")
    st.write("A dashboard to visualize sales trends and key metrics.")
    
    st.subheader("2. Coffee Shop Sales Dashboard")
    st.write("🔧 Tech: Power BI, SQL")
    st.write("Built a sales dashboard to visualize product trends, peak sales time, and branch performance using real-world coffee shop data.")

    st.subheader("3. Facial Emotion Recognition")
    st.write("🔧 Tech: Python, Keras, OpenCV, CNN")
    st.write("Built a CNN model to detect emotions from facial images with 80% accuracy.")
    
    st.subheader("4. Retail Sales Analysis")
    st.write("🔧 Tech: Python, PySpark, Colab")
    st.write("Analyzed product trends and cleaned retail data using PySpark.")

# Skills
elif page == "Skills":
    st.title("🛠 Skills")
    st.write("""
    **Languages**: Python, Java, SQL  
    **Tools**: Power BI, MySQL, Databricks, Linux  
    **Tech**: PySpark, CNN (Keras), ETL Process, Database Design  
    **Other**: Problem Solving, Teamwork, Azure Fundamentals
    """)

# Resume
elif page == "Resume":
    st.title("📄 Resume")
    st.markdown("[📥 Download My Resume (PDF)](https://drive.google.com/file/d/1-xfCVYraIiPsNHi_qX5AMg4Qh7ENwem1/view?usp=drivesdk)")

# Achievements
elif page == "Achievements":
    st.title("🏆 Achievements")
    st.markdown("- Solved **50+ DSA problems** on [Leetcode](https://leetcode.com/u/annupriyasahu2000/)")
    st.markdown("- Solved **25+ SQL problems** from [Top SQL 50](https://leetcode.com/studyplan/top-sql-50/)")
    st.markdown("- Completed: Coursera – *Programming for Everybody (Python)*")
    st.markdown("- Completed: Udemy – *DSA using Python*")

# Contact
elif page == "Contact":
    st.title("📬 Contact")
    st.write("📧 Email: annupriyasahu2000@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/annu-priya-42a181219/)")
    st.write("🗃 [GitHub](https://github.com/Annupriya28)")


