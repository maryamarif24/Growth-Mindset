import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from database import add_transaction, get_transactions, remove_transaction

# Title
st.title("💰 AI-Powered Personal Finance Tracker")

# 📌 **Add Transaction Form**
st.subheader("➕ Add a Transaction")
date = st.date_input("📅 Date")
category = st.selectbox(
    "📂 Category",
    [
        "Food", "Transport", "Shopping", "Bills", "Other"
    ]
    )
amount = st.number_input("💰 Amount", min_value=0.0, step=0.1)
trans_type = st.radio("🔄 Type", ["Income", "Expense"])

if st.button("✅ Add Transaction"):
    add_transaction(str(date), category, amount, trans_type)
    st.success("🎉 Transaction Added!")
    st.rerun()  # ✅ Fixed (Updated from experimental_rerun to rerun)

# 📌 **Show Transactions with Remove Buttons**
st.subheader("📋 Transaction History")
transactions = get_transactions()

# Ensure df is always defined
if transactions:
    df = pd.DataFrame(
        transactions,
        columns=[
            "ID",
            "Date",
            "Category",
            "Amount",
            "Type"
        ]
    )
else:
    df = pd.DataFrame(
        columns=[
            "ID",
            "Date",
            "Category",
            "Amount",
            "Type"
        ]
    )  # Empty DataFrame

if not df.empty:
    # **Show Transactions with Delete Button**
    for index, row in df.iterrows():
        col1, col2, col3, col4, col5, col6 = st.columns([1, 2, 2, 2, 2, 1])
        col1.text(row["ID"])
        col2.text(row["Date"])
        col3.text(row["Category"])
        col4.text(f"${row['Amount']:.2f}")
        col5.text(row["Type"])

        # **Delete Button (❌)**
        if col6.button("❌", key=f"delete_{row['ID']}"):
            remove_transaction(row["ID"])
            st.rerun()  # ✅ Fixed (Updated from experimental_rerun to rerun)

else:
    st.info("No transactions found. Start adding some!")

# 📌 **Visualization - Spending Analysis**
st.subheader("📊 Spending Analysis")

# Ensure df has data before filtering
if not df.empty:
    expense_df = df[df["Type"] == "Expense"]

    if not expense_df.empty:
        fig, ax = plt.subplots()
        expense_df.groupby("Category")["Amount"].sum().plot(kind="bar", ax=ax)
        st.pyplot(fig)
    else:
        st.info("No expenses recorded yet.")
else:
    st.info("No transactions recorded yet.")
