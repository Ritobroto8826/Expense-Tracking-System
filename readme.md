
# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.
With this you can track your expenses for a particular day, for a range of date grouped on category or for different months grouped on category.
This has been used with Mysql database

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```

## Expense Tracker Management System Demo 
### App_demo
![app_demo](https://github.com/user-attachments/assets/2b456024-ac15-43e9-a3a7-b98dccc5ca0b)

### Analytics_by_category with bar chart
![analytics_by_category_demo](https://github.com/user-attachments/assets/5f55479f-1b2a-484a-89e0-1ebb44939550)

### Analytics_by_month with bar chart
![analytics_by_month_demo](https://github.com/user-attachments/assets/014d5d1a-7a2f-4930-9f37-6eb7aa21b600)

### Analytics_by_day with pie chart
![analytics_by_day_demo](https://github.com/user-attachments/assets/c10df243-30a0-4d48-9a20-dce2186dd7b2)




   
