"""
This python module implements the main function of my data science portfolio.
"""
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Juan Palmeros Portfolio", 
                   page_icon="📊", 
                   layout="wide", 
                   initial_sidebar_state="expanded")

st.write("# Juan Palmeros :computer: :bar_chart: :computer:")
st.subheader("About me")

st.sidebar.success("Juan Palmeros :computer: ")

st.markdown(
    """
## Data Scientist
👋🏻 Hi, I'm Juan Francisco Palmeros Barradas! I'm a Data Scientist based in Mexico City with proven experiences in the finance and public policy sectors.  
   I am continuously seeking unique projects that allow me to broaden my horizons.  

💼 Now more than ever, I see huge potential for the application of Data Science across various industries, in particular in the banking and fintech sectors.  
:bank: :chart_with_upwards_trend:  Since I was an economics student, I have been passionate about financial inclusion and the use of data to improve the lives of people.

🏋🏻 When I'm not working, I enjoy indulging in various hobbies.  
I love learning new techniques and tools in the field of Data Science  
:fork_and_knife: :dog: :tv: I also enjoy having a walk with my dog, wathcing anime and cooking 

👨🏼‍💻 Academic Interests:  
Cloud computing, financial technology, machine learning, deep learning, natural language processing, computer vision, and data visualization. 

💭 Ideal Career Prospects:  
Data Scientist, Data Analyst, Data Engineer, Business Intelligence Analyst and Machine Learning Engineer. 

"""
)