import streamlit as st
from src import about, journey, certificates, projects, dashboard
import os

st.set_page_config(
    page_title="Data Science Portfolio",
    layout="wide",
)

# Load external CSS
def load_css(css_file):
    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the external CSS file
css_path = os.path.join(os.path.dirname(__file__), 'style.css')
load_css(css_path)

# Create tabs
tabs = ["About Me", "PROFESSIONAL JOURNEY", "Projects", "Certificates", "Dashboard"]
current_tab = st.tabs(tabs)

# Initialize tab_id in session state if not present
if 'tab_id' not in st.session_state:
    st.session_state.tab_id = 0

# Render content based on selected tab
with current_tab[0]:
    about.show()
with current_tab[1]:
    journey.show()
with current_tab[2]:
    projects.show()
with current_tab[3]:
    certificates.show()
with current_tab[4]:
    dashboard.show()
