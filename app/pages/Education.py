import streamlit as st
from functions import load_config

config_f = load_config("config.yaml")

# Set page configuration
st.set_page_config(page_title="Juan Palmeros Portfolio", 
                   page_icon="📊", 
                   layout="wide", 
                   initial_sidebar_state="expanded")

### SET CSS STYLE
with open(config_f['css_file']) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

## Set banorte container
with st.container():
    st.write("# Juan Palmeros")
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Education")
    st.markdown("<br> <br>", unsafe_allow_html=True)

## Set itam container
with st.container():
    col1, col2 = st.columns([2.5,7.5], gap="small")
    with col1:
        st.image(config_f['itam_picture'], width=300)
    with col2:
        st.markdown(
        """
        ### M.Sc Data Science, [Instituto Tecnológico Autónomo de México, ITAM (Instituto Tecnológico Autónomo de México)](https://www.itam.mx/en)
        *August 2022 - June 2023*
        Relevant Coursework: Data Mining, Machine Learning, Deep Learning, Statical Analysis, Time Series Analysis, 
        Bayesian Statistics, Causal Inference, Optimization, Data architecture.
        """
        )
st.markdown("<br>", unsafe_allow_html=True)
## Set CIDE container
with st.container():
    col1, col2 = st.columns([2.5,7.5], gap="small")
    with col1:
        st.image(config_f['cide_picture'], width=300)
    with col2:
        st.markdown(
        """
        ### B.Sc Economics, [CIDE (Center for Research and Teaching in Economics)](https://www.cide.edu/)
        *August 2015 - June 2019*
        Relevant course work: Econometrics, Macroeconomics, Microeconomics, Game Theory, Statistics, Public Finance,
        Dissertation: "The effect of financial literacy in asset acumulation: Evidence from ENIF 2018"
        """
        )
