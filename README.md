<div align="center">
  <h1>🍿 Movie Recommendation System</h1>
  <p>A smart, web-based application that suggests movies based on user preferences, tracks search history, and visualizes trends using Machine Learning and Data Analytics.</p>

  ![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
  ![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey.svg)
  ![MySQL](https://img.shields.io/badge/MySQL-Database-orange.svg)
  ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Recommendation%20Engine-green.svg)
  ![License](https://img.shields.io/badge/License-MIT-purple.svg)
</div>

<br />

## 📖 Overview

The **Movie Recommendation System** provides tailored movie suggestions by analyzing the attributes of a user's chosen film. Beyond simple recommendations, the application serves as an analytics platform by persisting user search queries into a local **MySQL** database and dynamically generating a bar chart of the most searched movies using **Matplotlib**.

## ✨ Key Features

- **Personalized Recommendations:** Get accurate movie suggestions based on complex similarity metrics.
- **Search Analytics:** Tracks every movie searched and stores the search frequency in a database.
- **Trend Visualization:** Automatically generates and displays a bar chart of the top 10 most-searched movies.
- **Responsive UI:** Clean, intuitive, and interactive web interface built with HTML, CSS, and Flask.

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Data Analytics & ML:** Pandas, NumPy, Scikit-learn, Matplotlib
- **Database:** MySQL Connector
- **Frontend:** HTML5, CSS3, JavaScript

## 📂 Project Structure

```text
MovieRecommendationSystem/
│
├── dataset/                  # Contains the CSV datasets (movies and credits)
├── models/                   # Pickled ML models (e.g., similarity matrices)
├── src/                      # Source code (training and recommendation logic)
│   ├── train.py
│   └── recommend.py
├── static/                   # Static assets (CSS, JS, generated graphs)
│   ├── css/style.css
│   └── graphs/search_trend.png
├── templates/                # HTML templates for the UI
│   └── index.html
├── app.py                    # Main Flask application
└── README.md                 # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- MySQL Server

### 1. Database Setup

Create a database named `movie_db` and a table to store search history:

```sql
CREATE DATABASE movie_db;
USE movie_db;

CREATE TABLE movie_search_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_name VARCHAR(255) NOT NULL,
    search_count INT DEFAULT 1
);
```

### 2. Installation

Clone the repository and install the required Python packages:

```bash
git clone https://github.com/Dhararp/Movie-recommendation-system.git
cd Movie-recommendation-system

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install flask mysql-connector-python pandas numpy matplotlib scikit-learn
```

### 3. Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and navigate to `http://127.0.0.1:5000/`.

## 📈 Visualizing Trends

When users search for movies, the application updates the database and instantly regenerates a Matplotlib graph representing the global search trends. This ensures that the platform is always up-to-date with the latest user analytical data.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
