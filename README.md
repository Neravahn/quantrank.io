# quantrank.io
quantrank.io is an interactive web platform desgined to help students practice quatitative aptitute efficiently. It tracks user performance, provides analytics, and offers a gamified experience to motivate consistent practics


[DEMO](https://drive.google.com/file/d/1HGhjwuwTLpOd3-BUfxsw4ekn1H5x31i5/view?usp=sharing)

## TEST ACCOUNT
username: prashant
password: prashant01


## Project Overview
quantrank.io is built to provide:
- Chapter-wise accuracy tracking – Understand which topics need more practice.
- Daily heatmap points system – Earn points based on daily activity.
- Difficulty-based scoring – Track performance across question difficulty     levels.
- Leaderboard – Compare performance with peers and encourage healthy competition.
- Attempted vs Correct graph – Visualize performance trends over time.
- Gamified experience – Points, streaks, and progress tracking make learning engaging.

The platform is desgined with scalability in min, using Python backend, SQLite databse, and a responsive JavaScript/Chart.js frontend.


## Features
### User Authentication
- Manual login with username/password
- Future support for Google and GitHub login

### Question Bank
- Chapter-wise and difficulty-level categorized questions
- Tracks attempted and correct answers

### Analytics & Dashboard
- Accuracy chart per chapter
- Last 10 days attempted vs correct line graph
- Heatmap of daily points earned
- Pie chart for points by difficulty level

### Leaderboard
- Ranks users by points
- Shows top performers

### Gamification
- Daily streak points
- Difficulty-level multipliers

### Admin Features
- Add/edit/delete questions
- View user performance


## Technologies Used
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=flat&logo=chartdotjs&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)


## Installation 
### Prerequisites
- Python 3.10+
- Pip package manager
- Git

### Steps
1. Clone the repository:
```bash
git clone https://github.com/Neravahn/QuantRank.io.git
cd QuantRank.io
```

2. Create a venv:
```bash
python3 -m venv venv
source venv/bin/activate
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the applicationL:
```bash
python app.py
```


## Usage
- Sign up with username and password
- Attemp questions from any chapter
- Track your progress on the dashboard
- Check leaderboards to compare score
- Analyze performance using line graphs, heatmaps, and pie charts


## License
This project is licensed under the MIT License 


