"""
This python module implements the main function of my data science portfolio.
"""
import streamlit as st
from functions import get_binary_file_downloader_html, load_config

config_f = load_config("config.yaml")

# Set page configuration
st.set_page_config(page_title="Juan Palmeros Portfolio", 
                   page_icon="📊", 
                   layout="wide", 
                   initial_sidebar_state="expanded")
### SET CSS STYLE
with open(config_f['css_file']) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with st.container():
    st.write("# Juan Palmeros")
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Data Scientist :computer: :bar_chart: :computer:")

with st.container():
    col1, col2 = st.columns([2.5,7.5], gap="small")
    with col1:
        st.image(config_f['profile_picture'], width=300)
        st.markdown("<br> <br> <br>", unsafe_allow_html=True)
        st.write(":mailbox:",config_f["email"])
    with col2:
        st.markdown(
        """
        ## About me
        👋🏻 Hi, I'm Juan Francisco Palmeros Barradas! I'm a Data Scientist based in Mexico City with proven experiences in the banking and public policy sectors.  
        :mortar_board: I hold a Master's degree in Data Science from the Autonomous Technological Institute of Mexico (ITAM) and a Bachelor's degree in Economics  
        from the Center for Research and Teaching in Economics (CIDE).

        💼 Now more than ever, I see huge potential for the application of Data Science across various industries, in particular in the banking and fintech sectors.  
        :bank: :chart_with_upwards_trend:  Since I was an economics student, I have been passionate about financial inclusion and the use of data to improve the lives of people.

        🏋🏻 When I'm not working, I enjoy indulging in various hobbies. I love learning new techniques and tools in the field of Data Science (I'm a long-life online learner) 
        :fork_and_knife: :dog: :tv: I also enjoy having a walk with my dog, wathcing anime and cooking 

        👨🏼‍💻 Academic Interests:  
        Cloud computing, financial technology, machine learning, deep learning, natural language processing, computer vision, and data visualization. 

        💭 Ideal Career Prospects:  
        Data Scientist, Data Analyst, Data Engineer, Business Intelligence Analyst and Machine Learning Engineer. 

        """
        )
        

with st.container():
    # Add download link for your resume
    st.markdown(get_binary_file_downloader_html(config_f['resume_version'], ':page_facing_up: Download my resume'), unsafe_allow_html=True)
