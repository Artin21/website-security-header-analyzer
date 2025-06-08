import streamlit as st
import pandas as pd
from scanner.headers_check import analyze_headers

st.set_page_config(page_title="Website Security Header Analyzer")

st.title("Website Security Header Analyzer")
st.write("Analyserar vanliga säkerhetsheadrar i HTTP-responsen.")

url =st.text_input("Skriv in en URL (inkl. https://)", "https://example.com")

if st.button("Analysera"):
    with st.spinner("Hämtar och analyserar headers..."):
        result = analyze_headers(url)

    if "error" in result:
        st.error(f"Något gick fel: {result['error']}")
    else:
        st.subheader("Resultat")
        st.write(f"**HTTP-status:** {result['status_code']}")
        st.write(f"**Säkerhetsbedömning:** `{result['rating']}`")

        total_headers = len(result["present_headers"]) + len(result["missing_headers"])
        st.write(f"**Säkerhetspoäng:** {result['score_percent']}% ({len(result['present_headers'])} av {total_headers} headers hittades)")

        st.markdown("### Hittade headrar:")
        if result["present_headers"]:
            df = pd.DataFrame(list(result["present_headers"].items()), columns=["Header", "Värde"])
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Inga säkerhetsheadrar hittades.")

        st.markdown("### Saknade headrar:")
        if result["missing_headers"]:
            df_missing = pd.DataFrame(result["missing_headers"], columns=["Header"])
            df_missing.index += 1
            st.dataframe(df_missing, use_container_width=True)
        else:
            st.success("Alla viktiga säkerhetsheadrar är närvarande!")