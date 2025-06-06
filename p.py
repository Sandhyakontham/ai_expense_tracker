import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import io

# Initialize session state for storing expenses
if 'expenses' not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])

# Function to add a new expense
def add_expense(date, category, amount, description):
    new_expense = pd.DataFrame({
        'Date': [date],
        'Category': [category],
        'Amount': [amount],
        'Description': [description]
    })
    st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)

# Function to generate AI-driven insights (simple rule-based for demo)
def generate_insights(df):
    insights = []
    if not df.empty:
        total_spent = df['Amount'].sum()
        category_spending = df.groupby('Category')['Amount'].sum()
        
        # Insight 1: High spending in a category
        max_category = category_spending.idxmax()
        max_amount = category_spending.max()
        if max_amount / total_spent > 0.4:
            insights.append(f"You’re spending {max_amount:.2f} in {max_category}, which is over 40% of your total expenses. Consider diversifying your spending or setting a budget for this category.")
        
        # Insight 2: Overspending alert
        if total_spent > 1000:  # Arbitrary threshold for demo
            insights.append("Your total spending is high. Try reviewing non-essential expenses to save more.")
        
        # Insight 3: Category suggestion
        if 'Savings' not in df['Category'].values:
            insights.append("No savings recorded. Consider allocating a portion of your income to savings for future security.")
    
    return insights if insights else ["No specific insights yet. Add more expenses to get personalized tips!"]

# Streamlit app layout
st.title("💰 AI-Powered Personal Finance Advisor")
st.markdown("Track your expenses, visualize your budget, and get AI-driven financial insights!")

# Sidebar for expense input
with st.sidebar:
    st.header("Add New Expense")
    with st.form(key='expense_form'):
        date = st.date_input("Date", value=datetime.today())
        category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Bills", "Savings", "Other"])
        amount = st.number_input("Amount ($)", min_value=0.0, step=0.01)
        description = st.text_input("Description")
        submit_button = st.form_submit_button("Add Expense")
        
        if submit_button:
            if amount > 0:
                add_expense(date, category, amount, description)
                st.success("Expense added successfully!")
            else:
                st.error("Amount must be greater than 0.")

# Main content
if not st.session_state.expenses.empty:
    # Display expense table
    st.subheader("Your Expenses")
    st.dataframe(st.session_state.expenses)

    # Visualizations
    st.subheader("Spending Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        # Pie chart for category distribution
        fig_pie = px.pie(st.session_state.expenses, names='Category', values='Amount', title="Spending by Category")
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        # Bar chart for spending over time
        expenses_by_date = st.session_state.expenses.groupby('Date')['Amount'].sum().reset_index()
        fig_bar = px.bar(expenses_by_date, x='Date', y='Amount', title="Spending Over Time")
        st.plotly_chart(fig_bar, use_container_width=True)

    # AI Insights
    st.subheader("AI Financial Insights")
    insights = generate_insights(st.session_state.expenses)
    for insight in insights:
        st.info(insight)

    # Download expenses as CSV
    st.subheader("Export Data")
    csv = st.session_state.expenses.to_csv(index=False)
    st.download_button(
        label="Download Expenses as CSV",
        data=csv,
        file_name="expenses.csv",
        mime="text/csv"
    )
else:
    st.info("No expenses recorded yet. Use the sidebar to add your first expense!")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit | © 2025 Personal Finance Advisor")