import streamlit as st
from scanner.headers_check import analyze_headers

st.set_page_config(page_title="Website Security Header Analyzer")

st.title("Website Security Header Analyzer")
st.write("Analyserar vanliga säkerhetsheadrar i HTTP-responsen.")

url = st.text_input("Skriv in en URL (inkl. https://)", "https://example.com")

if st.button("Analysera"):
    with st.spinner("Hämtar och analyserar headers..."):
        result = analyze_headers(url)

    if "error" in result:
        st.error(f"Något gick fel: {result['error']}")
    else:
        st.subheader("Resultat")
        st.write(f"**HTTP-status:** {result['status_code']}")
        st.write(f"**Säkerhetsbedömning:** `{result['rating']}`")

        st.markdown("### Hittade headrar:")
        if result["present_headers"]:
            st.table(result["present_headers"].items())
        else:
            st.info("Inga säkerhetsheadrar hittades.")

        st.markdown("### Saknade headrar:")
        if result["missing_headers"]:
            st.write(result["missing_headers"])
        else:
            st.success("Alla viktiga säkerhetsheadrar är närvarande!")
