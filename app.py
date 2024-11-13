import streamlit as st 
from assistants import (
    analyst_with_uploaded_csv,
    generator,
)
from knowledgebase import interaction_knowledge_base

st.set_page_config(
    page_title="BrainStorm Assistants",
    page_icon=":storm:",
)

st.title("Brainstorm Assistants Team")
st.markdown("##### 🤖 Your AI Assistants Team for Brainstorming!")

def generate_hypothesis_report(csv_file):
    st.write("Starting analysis...")

    with st.status("Analyzing data", expanded=True) as status:
        with st.container():
            analytical_report_container = st.empty()
            analytical_report = analyst_with_uploaded_csv(csv_file)
            #st.write(f"Analytical report length: {len(analytical_report)}")
            if analytical_report:
                analytical_report_container.markdown(analytical_report)
                st.session_state["analysis_report"] = analytical_report
        status.update(label="Analyzing data... Done!", state="complete")

    st.write("Starting hypothesis generation...")

    with st.status("Generating hypotheses", expanded=True) as status:
        with st.container():
            hypotheses_report_container = st.empty()
            hypotheses_report = generator.run(analytical_report, markdown=True, stream=False)
            #st.write(f"Number of hypotheses generated: {len(hypotheses_report)}")
            if hypotheses_report:
                hypotheses_report_container.markdown(hypotheses_report)
                st.session_state["hypotheses_report"] = hypotheses_report
    status.update(label="Generating hypotheses... Done!", state="complete")


def main() -> None:

    # upload data and knowledge base
    uploaded_data = st.sidebar.file_uploader("Upload your data", type=["csv", "txt"])
    if uploaded_data is not None:
        with open("temp_uploaded_data.csv","wb") as f:
            f.write(uploaded_data.getbuffer())
        st.session_state["uploaded_data"] = "temp_uploaded_data.csv"

    st.sidebar.file_uploader("Upload knowledge base", type=["pdf", "txt"])
    
    # button to generate hypothesis
    generate_hypothesis = st.sidebar.button("Generate Hypothesis")
    if generate_hypothesis:
        csv_file = st.session_state.get("uploaded_data")
        generate_hypothesis_report(csv_file)
    

    # check boxes for search, to be implementedin the future for advanced hypothesis generation
    st.sidebar.markdown("##### Assistants")
    search_knowledgebase=st.sidebar.checkbox("Knowledgebase search", value=True)
    search_exa = st.sidebar.checkbox("Exa search", value=False, disabled=True)
    search_arxiv = st.sidebar.checkbox("ArXiv search", value=False, disabled=True)
    search_pubmed = st.sidebar.checkbox("PubMed search", value=False, disabled=True)
        
    st.sidebar.markdown("---")
    if st.sidebar.button("Download Report"):
        # Retrieve both reports from session state
        hypotheses_report = st.session_state.get("hypotheses_report", "")
        analysis_report = st.session_state.get("analysis_report", "")

        # Combine the reports with a separator
        combined_report = f"""
    # Analysis Report

    {analysis_report}    

    ---
    # Hypotheses Report

    {hypotheses_report}

    """

        # Offer the combined report for download
        st.download_button(
            label="Download Report",
            data=combined_report,
            file_name="combined_report.md",
            mime="text/markdown"
        )
    if st.sidebar.button("Regenerate"):
        st.rerun()


        

if __name__ == "__main__":
    main()