import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai_litellm.litellm import LiteLLM

# --- UI ---
st.title("🤖 Pandas_AI– Ask Questions to Your File")
st.write("Upload your CSV, then ask questions about the data.")

uploaded_file = st.file_uploader("📂 Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### 📊 Preview of your dataset")
    st.dataframe(df.head())

    # LLM Setup
    llm = LiteLLM(
        model="gpt-4.1-mini",
        api_key=st.secrets["OPENAI_API_KEY"]
    )

    sdf = SmartDataframe(df, config={"llm": llm})

    question = st.text_input("💬 Ask a question about your data")

    if st.button("Ask"):
        with st.spinner("⏳ Thinking..."):
            response = sdf.chat(question)
            st.write("### 🧾 Answer:")
            st.write(response)

