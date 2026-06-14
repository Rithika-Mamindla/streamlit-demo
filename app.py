import streamlit as st
import pandas as pd
from datetime import date, timedelta

st.set_page_config(page_title="Smart Campus Resource Sharing System", layout="wide")

# -----------------------------
# Sample Data
# -----------------------------
resources = pd.DataFrame({
    "Item": ["Scientific Calculator", "Umbrella", "Lab Coat", "Power Bank", "USB Drive"],
    "Available": [15, 10, 8, 12, 20]
})

borrowings = pd.DataFrame({
    "Item": ["Calculator", "Umbrella"],
    "Due Date": ["Jun 18", "Jun 15"],
    "Status": ["Active", "Due Soon"]
})

notifications = [
    "Reminder: Return Calculator in 1 day",
    "Penalty Alert: Umbrella overdue",
    "New Resource Available: Power Bank"
]

penalties = pd.DataFrame({
    "Student Name": ["Rithika", "Karthik", "Prerna"],
    "Item": ["Calculator", "Umbrella", "Lab Coat"],
    "Days Late": [2, 1, 3],
    "Fine (₹)": [40, 20, 60]
})

# -----------------------------
# Welcome Screen
# -----------------------------
st.title("Smart Campus Resource Sharing System")

role = st.radio(
    "Select Your Role",
    ["👨‍🎓 Student", "👨‍💼 Admin"]
)

# ==================================================
# STUDENT SECTION
# ==================================================
if role == "👨‍🎓 Student":

    st.header("1. Login Page")

    student_id = st.text_input("Student ID / Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.success("Login Successful")

    menu = st.sidebar.selectbox(
        "Student Navigation",
        [
            "Home Dashboard",
            "Resource Catalog",
            "Item Details",
            "Borrow Confirmation",
            "My Borrowings",
            "Notifications",
            "Return Item"
        ]
    )

    # -----------------------------
    # Home Dashboard
    # -----------------------------
    if menu == "Home Dashboard":
        st.header("2. Home Dashboard")

        st.subheader("Welcome, Student Name")

        st.text_input("Search Resources")

        st.subheader("Categories")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.info("Academic Items")

        with col2:
            st.info("Lab Equipment")

        with col3:
            st.info("Electronics")

        with col4:
            st.info("Emergency Resources")

        with col5:
            st.info("Miscellaneous")

        st.subheader("Resource Summary")

        c1, c2, c3 = st.columns(3)

        c1.metric("Available Items", "65")
        c2.metric("Borrowed Items", "12")
        c3.metric("Due Soon", "3")

    # -----------------------------
    # Resource Catalog
    # -----------------------------
    elif menu == "Resource Catalog":
        st.header("3. Resource Catalog")
        st.dataframe(resources, use_container_width=True)

    # -----------------------------
    # Item Details
    # -----------------------------
    elif menu == "Item Details":
        st.header("4. Item Details")

        st.subheader("Scientific Calculator")

        st.write("**Availability:** 15")
        st.write("**Borrow Duration:** 3 Days")
        st.write("**Penalty:** ₹20/day after due date")
        st.write("**Condition:** Good")

        st.button("Borrow Now")

    # -----------------------------
    # Borrow Confirmation
    # -----------------------------
    elif menu == "Borrow Confirmation":
        st.header("5. Borrow Confirmation")

        st.write("**Item Name:** Scientific Calculator")
        st.write(f"**Borrow Date:** {date.today()}")

        return_date = date.today() + timedelta(days=3)

        st.write(f"**Return Date:** {return_date}")
        st.write("**Penalty Policy:** ₹20/day after due date")

        agree = st.checkbox(
            "I agree to return the item on time"
        )

        if st.button("Confirm Borrow"):
            if agree:
                st.success("Borrow Request Confirmed")
            else:
                st.warning("Please agree to the policy first.")

    # -----------------------------
    # My Borrowings
    # -----------------------------
    elif menu == "My Borrowings":
        st.header("6. My Borrowings")

        st.subheader("Active Borrowings")

        st.dataframe(borrowings, use_container_width=True)

    # -----------------------------
    # Notifications
    # -----------------------------
    elif menu == "Notifications":
        st.header("7. Notifications")

        for note in notifications:
            st.info(note)

    # -----------------------------
    # Return Item
    # -----------------------------
    elif menu == "Return Item":
        st.header("8. Return Item")

        st.write("Student scans QR code")

        st.write("**Item Name:** Scientific Calculator")
        st.write("**Return Status:** Ready for Return")

        if st.button("Complete Return"):
            st.success("Item Returned Successfully")

# ==================================================
# ADMIN SECTION
# ==================================================
else:

    menu = st.sidebar.selectbox(
        "Admin Navigation",
        [
            "Admin Dashboard",
            "Inventory Management",
            "Penalty Management"
        ]
    )

    # -----------------------------
    # Admin Dashboard
    # -----------------------------
    if menu == "Admin Dashboard":
        st.header("1. Admin Dashboard")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Total Resources", "100")
        c2.metric("Borrowed Resources", "25")
        c3.metric("Overdue Resources", "5")
        c4.metric("Available Resources", "75")

    # -----------------------------
    # Inventory Management
    # -----------------------------
    elif menu == "Inventory Management":
        st.header("2. Inventory Management")

        st.subheader("Add Item")
        st.text_input("Item Name")
        st.number_input("Quantity", min_value=1, value=1)

        st.button("Add Item")

        st.divider()

        st.subheader("Other Actions")

        st.button("Remove Item")
        st.button("Update Quantity")
        st.button("Mark Item Damaged")

    # -----------------------------
    # Penalty Management
    # -----------------------------
    elif menu == "Penalty Management":
        st.header("3. Penalty Management")

        st.dataframe(penalties, use_container_width=True)
