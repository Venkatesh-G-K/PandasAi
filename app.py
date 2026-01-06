import streamlit as st
import pandas as pd
from openai import OpenAI

# ---------- OpenAI Client ----------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ---------- UI ----------
st.set_page_config(page_title="Ask CSV with AI", layout="wide")
st.title("🤖 Ask Questions to Your CSV")
st.write("Upload a CSV file and ask questions in any language.")

uploaded_file = st.file_uploader("📂 Upload CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.subheader("📊 Data Preview")
        st.dataframe(df.head(10), use_container_width=True)

        question = st.text_input("💬 Ask a question about the data")

        if st.button("Ask") and question.strip():
            with st.spinner("Thinking..."):
                prompt = f"""
You are a professional data analyst.

Dataset columns:
{list(df.columns)}

Sample data:
{df.head(10).to_string(index=False)}

User question:
{question}

Answer clearly and concisely.
"""

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful data analyst."},
                        {"role": "user", "content": prompt}
                    ],
                )

                st.subheader("🧾 Answer")
                st.write(response.choices[0].message.content)

    except Exception as e:
        st.error("❌ Error reading file or processing question")
        st.exception(e)
else:
    st.info("⬆️ Upload a CSV file to get started.")

st.title("Venkat")
