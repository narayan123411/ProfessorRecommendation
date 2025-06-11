# Professor Recommendation System 🎓

A personalized modular recommendation system built for students at the University of North Texas (UNT) to help them make informed decisions about course selection and professor preferences each semester. The system uses historical feedback, course load analysis, and student priorities to suggest optimal subject-professor combinations.

### 💡 Modular Design Philosophy
Separation of Concerns: Business logic is separated from routing and data access.

Reusable Components: Recommendation and ranking engines are self-contained.

Ease of Testing: Each module can be tested independently.

Scalable Structure: Easily extensible for more campuses or recommendation types.


### 🚀 Features

👨‍🏫 Professor ranking module using ratings, difficulty level, and grading patterns

🔍 Filter and search module for schedule preferences, credits, and department

🧠 Personalization engine that adapts based on user profile/preferences

📊 Modular data visualizations for trends and statistics


### 📦 Tech Stack

Backend: Python (Modularized using packages and layers)

Framework: Flask (or FastAPI for async)

Frontend: HTML/CSS 

Database: SQLite and Pandas (abstracted via a data access layer)

ML: Scikit-learn, Pandas, NumPy

Visualization: Seaborn / Plotly


### 💡 How It Works

Input: Student inputs preferences such as:

Major/Department

Desired credit hours

Interest level / Difficulty tolerance

Preferred professor style (strict, lenient, engaging, etc.)


### Processing:

Uses a recommendation algorithm (content-based or collaborative filtering).

Considers historical data: student ratings, past grades, course load difficulty.

### Output:

List of recommended subject-professor combinations.

Additional insights like average GPA, professor reviews, and workload.

### 📈 Data Sources

Historical student feedback (anonymized)

UNT course catalog

Public professor rating platforms/ GoogleScholar/ LinkedIn
