import streamlit as st
import pandas as pd
import sqlite3

DB_PATH = r"C:\Users\abinsanal\Videos\local food waste\db\food.db"

# ---------------------------
# DB Helpers
# ---------------------------
def run_query(query, params=()):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df

def run_execute(query, params=()):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

# ---------------------------
# CRUD Operations
# ---------------------------
def add_provider(name, city):
    run_execute("INSERT INTO providers (name, city) VALUES (?, ?)", (name, city))

def add_receiver(name, city):
    run_execute("INSERT INTO receivers (name, city) VALUES (?, ?)", (name, city))

def add_food_listing(provider_id, food_type, quantity):
    run_execute("INSERT INTO food_listings (provider_id, type, quantity) VALUES (?, ?, ?)", 
                (provider_id, food_type, quantity))

def add_claim(receiver_id, food_listing_id, status):
    run_execute("INSERT INTO claims (receiver_id, food_listing_id, status) VALUES (?, ?, ?)", 
                (receiver_id, food_listing_id, status))

# ---------------------------
# Pages
# ---------------------------
def page_home():
    st.title("📊 Dashboard")
    st.info("Welcome to the Food Waste Management Dashboard")
    st.write("Key stats will appear here.")

def page_providers():
    st.title("🏢 Providers")
    city_filter = st.text_input("Filter by City (optional)")

    if city_filter:
        df = run_query("SELECT * FROM providers WHERE city LIKE ?", (f"%{city_filter}%",))
    else:
        df = run_query("SELECT * FROM providers")
    st.dataframe(df)

    with st.form("add_provider"):
        st.subheader("➕ Add Provider")
        name = st.text_input("Name")
        city = st.text_input("City")
        if st.form_submit_button("Add Provider"):
            add_provider(name, city)
            st.success("✅ Provider added!")
            st.experimental_rerun()

def page_receivers():
    st.title("🙋 Receivers")
    city_filter = st.text_input("Filter by City (optional)")

    if city_filter:
        df = run_query("SELECT * FROM receivers WHERE city LIKE ?", (f"%{city_filter}%",))
    else:
        df = run_query("SELECT * FROM receivers")
    st.dataframe(df)

    with st.form("add_receiver"):
        st.subheader("➕ Add Receiver")
        name = st.text_input("Name")
        city = st.text_input("City")
        if st.form_submit_button("Add Receiver"):
            add_receiver(name, city)
            st.success("✅ Receiver added!")
            st.experimental_rerun()

def page_food_listings():
    st.title("🥗 Food Listings")
    df = run_query("SELECT * FROM food_listings")
    st.dataframe(df)

    with st.form("add_food_listing"):
        st.subheader("➕ Add Food Listing")
        provider_id = st.number_input("Provider ID", min_value=1)
        food_type = st.text_input("Food Type")
        quantity = st.number_input("Quantity", min_value=1)
        if st.form_submit_button("Add Food Listing"):
            add_food_listing(provider_id, food_type, quantity)
            st.success("✅ Food listing added!")
            st.experimental_rerun()

def page_claims():
    st.title("📦 Claims")
    df = run_query("SELECT * FROM claims")
    st.dataframe(df)

    with st.form("add_claim"):
        st.subheader("➕ Add Claim")
        receiver_id = st.number_input("Receiver ID", min_value=1)
        food_listing_id = st.number_input("Food Listing ID", min_value=1)
        status = st.selectbox("Status", ["Pending", "Approved", "Rejected"])
        if st.form_submit_button("Add Claim"):
            add_claim(receiver_id, food_listing_id, status)
            st.success("✅ Claim added!")
            st.experimental_rerun()

def page_insights():
    st.title("📈 Insights")
    st.write("Charts and analytics will be shown here.")

def page_admin():
    st.title("🛠 Admin")
    st.file_uploader("Upload CSV")
    st.write("DB rebuild and maintenance tools.")

# ---------------------------
# Sidebar Navigation
# ---------------------------
PAGES = {
    "Home / Dashboard": page_home,
    "Providers": page_providers,
    "Receivers": page_receivers,
    "Food Listings": page_food_listings,
    "Claims": page_claims,
    "Insights": page_insights,
    "Admin": page_admin
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
PAGES[selection]()
