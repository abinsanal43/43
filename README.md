# 🍽️ Local Food Waste Management

A simple **Streamlit-based web application** to connect **food providers** with **food receivers**, reducing food waste in the local community.

---

## 🚀 Features
- 📂 **Load Data from CSV** – View providers and receivers from preloaded CSV files.
- 🔍 **Search by Location & Food** – Quickly find food available near you.
- ➕ **Add Providers & Receivers** – Update the database directly from the UI.
- 💡 **User-Friendly Interface** – Powered by [Streamlit](https://streamlit.io/).

---

## 📂 Project Structure
.
├── data/ # CSV files for providers & receivers
├── db/ # Database/CSV storage
├── notebooks/ # Optional Jupyter notebooks
├── src/ # Source code
├── main.py # Streamlit app entry point
├── create_db.py # Script to initialize database
├── requirements.txt # Python dependencies
└── .gitignore # Ignored files (e.g., venv/)

yaml
Copy
Edit

---

## 🛠️ Installation & Running the App

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/abinsanal43/food-waste-magangement.git
cd food-waste-magangement
2️⃣ (Optional) Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the App
bash
Copy
Edit
streamlit run main.py
