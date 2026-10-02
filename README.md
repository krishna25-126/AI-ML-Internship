# AI/ML Internship – Task 1
### AI/ML Development Environment Setup, Python Foundations & Data Exploration

A one-week project covering environment setup, core Python, Pandas, data cleaning, and exploratory
data analysis, completed as Task 1 of an AI/ML internship.

## Project Structure
```
AI-ML-Internship/
├── data/           # raw, cleaned, and final datasets
├── notebooks/      # Jupyter notebooks (Days 2, 4, 5, 6-7)
├── src/            # reusable Python scripts
├── reports/        # EDA PDF report
├── images/         # saved charts
├── models/         # reserved for Task 2
├── requirements.txt
└── README.md
```

## Setup
1. Clone the repo
   ```bash
   git clone https://github.com/krishna25-126/AI-ML-Internship.git
   cd AI-ML-Internship
   ```
2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Launch Jupyter
   ```bash
   jupyter notebook
   ```

## Notebooks
| Notebook | Description |
|---|---|
| `02_python_fundamentals.ipynb` | Variables, data types, operators, loops, functions, lists, dicts, sets, file handling |
| `04_data_loading_exploration.ipynb` | Loading `student_data.csv` with Pandas, initial inspection |
| `05_data_cleaning.ipynb` | Handling missing values, removing duplicates, fixing inconsistent labels |
| `06_07_mini_project_eda.ipynb` | Mini project: full EDA with histograms, box plots, scatter plots, correlation heatmap, and insights |

## Mini Project: Student Performance Data Explorer
**Problem statement:** analyze student performance data to identify patterns and present findings
through visualizations.

**Key findings:**
- Study hours and attendance both show a positive relationship with average score.
- Math has the highest average score among the three subjects; English shows the widest spread.
- Attendance correlates with scores slightly more strongly than study hours.
- Gender does not show a large difference in average score.
- A small number of outliers exist in each score column.

Full findings are in [`reports/EDA_Report.pdf`](reports/EDA_Report.pdf).

## Dataset
`data/student_data.csv` — a student performance dataset (206 records) with Student ID, Name, Gender,
Study Hours, Attendance (%), Math Score, Science Score, and English Score.

## Progress
- [x] Day 1: Environment setup and repo structure
- [x] Day 2: Python fundamentals
- [x] Day 3: Practice scripts
- [x] Day 4: Pandas basics / data loading
- [x] Day 5: Data cleaning
- [x] Day 6: EDA and visualizations
- [x] Day 7: Mini project and report

## Next Task
Task 2 builds on the cleaned dataset here to introduce core machine learning concepts: preprocessing,
feature engineering, train/test splitting, baseline model training, and evaluation.
