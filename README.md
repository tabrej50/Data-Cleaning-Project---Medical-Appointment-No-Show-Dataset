# 📊 Data Cleaning Project - Medical Appointment No Show Dataset

## 📁 Project Overview

This project is part of my Data Analyst Internship assignment where the objective was to clean and preprocess a real-world dataset. I selected the **Medical Appointment No Show Dataset** from Kaggle, which contains information about over 110,000 medical appointments in Brazil. The goal of this dataset is to analyze whether a patient showed up for their appointment or not, based on various factors like age, gender, health conditions, and appointment scheduling.

The raw data had several issues such as duplicates, inconsistent formatting, unnecessary columns, and incorrect data types. This project focuses on cleaning and transforming the dataset to make it ready for further analysis or machine learning modeling.

---

## 🎯 Objective

The primary objective of this task was to:
- Identify and handle missing values
- Remove duplicate entries
- Correct inconsistent data formats
- Fix data types (like date columns and age values)
- Rename columns for better readability
- Standardize categorical variables

---

## 📌 Dataset Information

- **Rows**: 110,527
- **Columns**: 14
- **Source**: [Kaggle - Medical Appointment No Shows](https://www.kaggle.com/datasets/joniarroba/noshowappointments)
- **Context**: This dataset collects appointment records from Brazil and records whether the patient showed up or not, along with demographic and health-related features.

---

## 🛠️ Tools Used

- Python 3
- Pandas
- Jupyter Notebook

---

## 🧹 Data Cleaning Steps Performed

### ✅ 1. Loaded the dataset
The CSV file was read into a Pandas DataFrame to inspect its structure, column names, and types.

### ✅ 2. Renamed column headers
Converted all column names to lowercase and replaced spaces with underscores for better consistency and easier coding.

Example:
- `ScheduledDay` ➝ `scheduled_day`
- `AppointmentDay` ➝ `appointment_day`

### ✅ 3. Removed duplicate records
Dropped 100+ duplicate rows to ensure each appointment record is unique.

### ✅ 4. Fixed date formats
Converted `scheduled_day` and `appointment_day` columns from object type to proper `datetime` format using `pd.to_datetime()`.

### ✅ 5. Handled incorrect age values
Removed entries where age was negative (e.g., -1) which are clearly invalid.

### ✅ 6. Dropped irrelevant columns
Columns like `patientid` and `appointmentid` were removed as they are unique identifiers and not useful for analysis.

### ✅ 7. Checked and cleaned categorical values
- Ensured that `gender` had only two valid categories: `Male`, `Female`
- Standardized other categorical columns where necessary

---

## ✅ Final Result

After cleaning, the dataset is:
- Free of duplicates
- Free of invalid values (like negative ages)
- Properly formatted with correct data types
- Ready for analysis and visualization

---

## 💾 Files in This Repository

- `cleaned_medical_appointments.csv` – The final cleaned dataset
- `data_cleaning_notebook.ipynb` – Jupyter notebook with all cleaning steps and code
- `README.md` – Project overview and summary of work

---

## 🙋‍♂️ About Me

I’m **Tabrej Patel**, a BSc Data Science student at Symbiosis Skills and Professional University. This project was completed as part of my internship assignment to strengthen my skills in data preprocessing — one of the most important steps in any data analytics pipeline.

---

## 🔗 Submission

This project has been submitted to the internship task portal via GitHub. Thank you for reviewing my work!

