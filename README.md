# 🚀 Autonomous Data Pipeline & Analytics Agent

## 📌 Project Overview

This project aims to build an **AI-powered data analyst copilot** that automates repetitive data tasks such as querying databases, cleaning data, and generating insights.

🔍 **Core Problem:**
Data analysts spend **60–70% of their time** on data cleaning, transformation, and pipeline maintenance instead of actual analysis.

💡 **Our Solution:**
An intelligent agent that converts **natural language queries → SQL → data insights**.

---

## 🎯 Day 2 Progress: Setup & Basic Pipeline

### ✅ Achievements

* Built a **multi-table database** using DuckDB
* Loaded realistic datasets (Customers & Sales)
* Connected database with **LangChain SQLDatabase utility**
* Successfully **introspected database schema**
* Integrated **LLM to explain database structure in plain English**
* Developed a **Streamlit-based frontend skeleton**

---

## 🏗️ System Architecture

```
User Input (Streamlit UI)
        ↓
LangChain SQLDatabase
        ↓
DuckDB Database
        ↓
Schema Extraction
        ↓
LLM (Schema Explanation)
        ↓
Output to User
```

---

## 🧩 Tech Stack

* **Frontend:** Streamlit
* **Database:** DuckDB
* **Data Handling:** Pandas
* **LLM Integration:** OpenAI / NVIDIA API
* **Framework:** LangChain

---

## 📂 Project Structure

```
Autonomous-Data-Pipeline-Analytics-Agent/
│
├── app.py                # Streamlit frontend
├── setup_db.py           # Database setup script
├── csv_folder/           # Datasets (customers, sales)
├── threedatasets.db      # DuckDB database
└── README.md             # Project documentation
```

---

## ⚙️ Features Implemented (Day 2)

* 🔗 Database connection and initialization
* 📊 Multi-table dataset integration
* 🧠 Schema introspection using LangChain
* 💬 LLM-based table explanation
* 🖥️ Interactive Streamlit UI (basic)

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install streamlit duckdb langchain langchain-community
```

### 2. Run the app
## Restart the Runtime and just run this for being in the safe side and reduce errors as much as possible
```
!pkill -f streamlit
!streamlit run app1.py & npx localtunnel --port 8501
```

---

## 🧪 Sample Output

* List of available tables
* Detailed schema of each table
* AI-generated explanation of database structure

---

## 🎯 Key Learnings

* Handling **database connections & concurrency (DuckDB)**
* Integrating **LLMs with structured data**
* Building **interactive data apps using Streamlit**
* Understanding **schema introspection workflows**

---

## 🚀 Next Steps (Day 3)

* Implement **LangChain SQL Agent (ReAct pattern)**
* Enable **Natural Language → SQL query generation**
* Add **JOIN queries and aggregation support**
* Implement **automatic error correction (sql_db_query_checker)**

---

## ⭐ Conclusion

This project demonstrates how AI can **democratize data access**, allowing even non-technical users to interact with complex datasets using natural language.

---
