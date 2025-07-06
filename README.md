# 🎬 Movie Recommendation System

This is a simple Netflix-style Movie Recommendation System using **User-Based Collaborative Filtering**. It recommends movies to users based on the ratings given by other similar users.

---

## 📁 Project Structure

```
Project 3/
├── data/
│ ├── ratings.csv # Movie ratings dataset
│ └── movies.csv # Movie metadata
│
├── recommender/
│ ├── build_similarity.py # Builds cosine similarity matrix
│ └── recommend.py # User-based collaborative filtering logic
│
├── app/
│ └── streamlit_app.py # Optional UI using Streamlit
│
├── main.py # CLI test script to get recommendations
├── requirements.txt # Python library dependencies
├── README.md # Project documentation
└── venv/ # Virtual environment folder
```

---

## ⚙️ Setup Instructions

### 1. ✅ Clone or Download the Repository

```bash
cd "your path/Project 3"
```
### 2. 📦 Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
# source venv/bin/activate  # For Linux/Mac
```
### 3. 📥 Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. 🧪 Run From Command Line (for testing)
Edit main.py to change user_id = ... and then:
    
```bash
python main.py
```
### 5. 🌐 Launch Streamlit Web App

```bash
streamlit run app/streamlit_app.py
```