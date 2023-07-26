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
    st.subheader("Professional Experience")
    st.markdown("<br> <br>", unsafe_allow_html=True)

## Set banorte container
with st.container():
    col1, col2 = st.columns([2.5,7.5], gap="small")
    with col1:
        st.image(config_f['banorte_picture'], width=300)
    with col2:
        st.markdown(
        """
        ### Data Scientist, [Grupo Financiero Banorte (Financial Group Banorte)](https://investors.banorte.com/en)
        *June 2023 - Present*
        - Implement experiments to boolster the digital onboarding process. 
        - Perfom AB testing to evaluate the impact of new features in the mobile app.
        - Develop an statistical analysis to identify the efficency of bank branches and atms.
        """
        )
st.markdown("<br>", unsafe_allow_html=True)
## Set banxico container
with st.container():
    col1, col2 = st.columns([2.5,7.5], gap="small")
    with col1:
        st.image(config_f['banxico_picture'], width=300)
    with col2:
        st.markdown(
        """
        ### Financial Researcher, [Banco de México (Central Bank of Mexico)](https://www.banxico.org.mx/indexen.html)
        *August 2019 - June 2023*
        - Led the first representative survey in Latin America on the financial health of individuals. [Link to survey results (spanish)](https://www.banxico.org.mx/publicaciones-y-prensa/encuesta-de-competencias-financieras-de-la-poblaci/competencias-financieras-en.html)
        - Contributed to the modification of the [National Survey of Financial Inclusion 2021](http://en.www.inegi.org.mx/programas/enif/2021/), one of the largest financial inclusion surveys in the world.
        - Conducted a statistical analysis of financial infrastructure locations for a public investment of over 120 million Mexican pesos.
        - Provided continuous information on the state of the financial system in Mexico to guide decision-making for stakeholders.
        """
        )
## Set cide container
with st.container():
    col1, col2 = st.columns([2.5,7.5], gap="small")
    with col1:
        st.image(config_f['cide_picture'], width=300)
    with col2:
        st.markdown(
        """
        ### Research assitant, [CIDE (Center for Research and Teaching in Economics)](https://www.cide.edu/)
        *August 2016 - June 2019*
        - Analyzed relevant literature on the Central American migratory phenomenon.
        - Compiled information for the elaboration of a paper on the consequences of migration in the labor market of the receiving country.
        - Assisted with the implementation of the "Mexico Las Americas y el mundo (Mexico, The Americas, and the World)" survey.
        """
        )
