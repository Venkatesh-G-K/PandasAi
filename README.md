🤖 PandasAI Streamlit App – Ask Questions to Your CSV

This is a Streamlit web application that allows users to upload a CSV file and ask natural-language questions about the data using PandasAI + OpenAI.

The app converts plain English questions into Pandas operations and returns clear, readable answers—no coding required.

🚀 Live Demo

👉 Live App:
https://venkat-pandasai.streamlit.app/

✨ Features

📂 Upload any CSV file

🤖 Ask questions in plain English

📊 Automatic data understanding using PandasAI

⚡ Fast, interactive Streamlit UI

🔐 Secure API key handling via Streamlit Secrets

☁️ Cloud-deployed (Streamlit Community Cloud)

🧱 Tech Stack

Python 3.11

Streamlit – Web UI

Pandas – Data handling

PandasAI – Natural language to Pandas

OpenAI API – LLM backend

📁 Project Structure
pandas_ai/
│── app.py                 # Streamlit application
│── requirements.txt       # Python dependencies
│── runtime.txt            # Python version (3.11)
│── README.md              # Project documentation
│
└── .streamlit/
    └── secrets.toml       # Local secrets (not committed)

🛠 Installation (Local Setup)
1️⃣ Clone the repository
git clone https://github.com/venkatesh-g-k/pandasai.git
cd pandasai

2️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

🔐 Configure OpenAI API Key (Local)

Create a file at:

.streamlit/secrets.toml


Add:

OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxx"


⚠️ Never commit this file to GitHub

▶️ Run the App Locally
streamlit run app.py


The app will open in your browser.

☁️ Deployment (Streamlit Cloud)

Push code to GitHub

Go to https://share.streamlit.io

Click New App

Select:

Repository

Branch: main

File: app.py

Add Secrets in Streamlit Cloud:

OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxx"


Deploy 🚀

💡 Example Questions

“How many rows are in this dataset?”

“Show me the top 5 values by sales”

“What is the average revenue per category?”

“Which column has missing values?”

“Summarize this dataset”

⚠️ Notes & Limitations

Large datasets may take longer to process

OpenAI API usage is billable

Best suited for analysis, not transactional workloads

🧭 Future Enhancements

💬 Chat history

🔒 User authentication

📥 Download answers

📊 Visual outputs (charts)

📁 Multi-file analysis

👤 Author

Venkat
Data & Analytics | Power BI | Python | AI
