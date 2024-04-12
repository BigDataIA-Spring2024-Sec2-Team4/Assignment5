import streamlit as st
import requests

from streamlit_option_menu import option_menu

import questionsp2, statsp3, statsp4

st.set_page_config(
    page_title="Text Extraction System",
)


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title=None,
                options=['Technical Notes', 'Questions', 'Statistics', 'Summary'],
                icons=['layout-text-sidebar-reverse', 'patch-question', 'pie-chart', 'file-bar-graph'],
                menu_icon='robot',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == "Questions":
            questionsp2.app()
        elif app == "Statistics":
            statsp3.app()
        elif app == "Summary":
            statsp4.app()
        elif app == "Technical Notes":
            self.aws_s3_viewer()

    def aws_s3_viewer(self):
        st.title("Technical Notes")

        # Define the FastAPI backend URL
        FASTAPI_URL = "http://localhost:8000"

        # Function to fetch markdown data from FastAPI backend
        def fetch_markdown_data(bucket_name):
            url = f"{FASTAPI_URL}/markdown/{bucket_name}"
            response = requests.get(url)
            if response.status_code == 200:
                markdown_files = response.text
                return response.text
            else:
                st.error(f"Error fetching markdown data: {response.text}")
                return ""

        # Dropdown menu options
        options = ["Big Data Projects", "Backtesting & Simulation", "Branded Image Link Added to Refresher Reading"]
        selected_option = st.selectbox("Select a Title", options)

        # Fetch markdown data upon selection
        markdown_data = fetch_markdown_data(selected_option)

        # Display fetched markdown data
        st.markdown(markdown_data, unsafe_allow_html=True)


if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()
