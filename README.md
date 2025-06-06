1. Introduction
What is it?
A user-friendly web app built with Streamlit to help individuals manage their finances by tracking expenses, visualizing budgets, and receiving AI-driven insights.
Why is it innovative?
Combines simplicity, interactivity, and personalized financial advice in one platform.
Leverages modern tools (Streamlit, Pandas, Plotly) for a seamless experience without requiring complex coding.
Addresses a universal need: better financial management for everyone.
2. Problem Statement
Challenges in Personal Finance:
Many people struggle to track spending, set budgets, or understand their financial habits.
Existing tools can be complex, non-interactive, or lack personalized insights.
Our Solution:
A web app that simplifies expense tracking, visualizes spending patterns, and offers actionable AI-generated tips to improve financial health.
3. Key Features
Expense Tracking:
Add expenses via an intuitive sidebar form (date, category, amount, description).
View all expenses in a clean, tabular format.
Interactive Visualizations:
Pie chart showing spending distribution by category (e.g., Food, Transport, Bills).
Bar chart displaying spending trends over time.
Built with Plotly for dynamic, clickable charts.
AI-Driven Insights:
Analyzes spending patterns to provide personalized tips (e.g., “You’re spending heavily on Food; consider a budget.”).
Uses rule-based logic (scalable to advanced AI models in the future).
Data Export:
Download expense data as a CSV file for external use or record-keeping.
User-Friendly Design:
Built with Streamlit for a responsive, web-based interface.
No need for users to install software—just access via a browser.
4. Technical Highlights
Tech Stack:
Streamlit: Rapid development of interactive web apps with Python.
Pandas: Efficient data handling for expense storage and analysis.
Plotly: Interactive, visually appealing charts for data insights.
Code Structure:
Modular functions for adding expenses, generating insights, and rendering visualizations.
In-memory data storage using Streamlit’s session state (scalable to databases).
Scalability:
Can integrate real AI models (e.g., machine learning for spending predictions).
Deployable on Streamlit Community Cloud for public access.
5. Demo (Live Showcase)
Steps to Demonstrate:
Open the app (streamlit run finance_advisor.py) and show the browser interface.
Add a few sample expenses via the sidebar (e.g., $50 on Food, $30 on Transport).
Show the expense table updating in real-time.
Highlight the pie and bar charts, interacting with them (e.g., hover to see details).
Display AI insights generated based on the entered data.
Download a CSV file to show export functionality.
Tips for Demo:
Pre-populate a few expenses to save time.
Emphasize the simplicity of adding expenses and the clarity of visualizations.
Point out an AI insight (e.g., “Notice how it suggests saving more if no savings are recorded.”).
6. Benefits and Impact
For Users:
Simplifies financial tracking with an intuitive interface.
Empowers better decision-making with visual and AI-driven insights.
Accessible to non-technical users (no coding required).
For Developers:
Demonstrates Streamlit’s power for rapid app development.
Extensible codebase for adding features like cloud storage or advanced analytics.
Real-World Value:
Helps users save money, reduce overspending, and plan for financial goals.
Scalable for small businesses or financial advisors to manage client budgets.
