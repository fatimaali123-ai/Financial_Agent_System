import streamlit as st
st.write("✅ Streamlit is working properly!")  # test line

from orchestrator import Orchestrator

st.title("📊 FinAgent - Financial AI Assistant")

company_name = st.text_input("Enter Company Name (e.g., Tesla)")
ticker = st.text_input("Enter Stock Symbol (e.g., TSLA)")

if st.button("Generate Report"):
    agent = Orchestrator()
    with st.spinner("Generating report..."):
        report = agent.generate_report(company_name, ticker)
    st.success("Report Generated!")
    st.text(report)
