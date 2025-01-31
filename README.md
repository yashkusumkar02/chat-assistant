# Chat Assistant for SQLite Database

## Overview
This is a Flask-based Chat Assistant that interacts with an SQLite database to answer user queries about employees and departments. It supports natural language queries and provides structured responses.

## Features
- Accepts user queries through a chatbot interface.
- Retrieves employee and department information from an SQLite database.
- Provides a web-based interface for interaction.
- Offers quick-access suggested questions for better user experience.

## Installation & Setup

### **1. Clone the Repository**
```bash
git clone https://github.com/yashkusumkar02/chat-assistant.git
cd chat-assistant
```

### **2. Install Dependencies**
```bash
pip install flask
```

### **3. Setup the Database**
```bash
python setup_db.py
```

### **4. Run the Application**
```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser to access the chatbot.

## Supported Queries
The assistant supports the following types of queries:
- **"Show me all employees in the Sales department."**
- **"Who is the manager of the Engineering department?"**
- **"List all employees hired after 2021-01-01."**
- **"What is the total salary expense for the Marketing department?"**

## Known Limitations
- Only supports predefined query structures.
- The database is static (data does not update dynamically).
- No authentication or user management.

## Future Improvements
- Implement a more advanced NLP model for handling diverse queries.
- Add a database management interface to allow updates in real-time.
- Include authentication and user roles for restricted access.

## Deployment
This project can be deployed on platforms like **Render**, **Heroku**, or **AWS**. Follow deployment guides to set up a public URL for access.

## Contribution
If you'd like to contribute, fork the repository and submit a pull request!

## Contact
For any queries, reach out to **kusumkarsuyash1234@gmail.com**.
