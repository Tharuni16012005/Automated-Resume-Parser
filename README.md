# Automated Resume Parser

## Overview

Automated Resume Parser is a Flask-based web application that extracts candidate information from PDF resumes. The application automatically identifies and displays key details such as name, email, phone number, skills, and educational qualifications.

## Features

* Upload PDF resumes
* Extract candidate name
* Extract email address
* Extract phone number
* Extract technical skills
* Extract educational qualifications
* Store extracted data in SQLite database
* User-friendly web interface

## Technologies Used

* Python
* Flask
* PDFPlumber
* SQLite
* HTML
* CSS

## Project Structure

```text
Resume_Parser/
│
├── app.py
├── parser.py
├── database.py
├── resumes.db
├── requirements.txt
│
├── resumes/
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
python app.py
```

4. Open in browser

```text
http://127.0.0.1:5000
```

## Output

The application extracts:

* Name
* Email
* Phone Number
* Skills
* Educational Qualifications

and stores the information in a SQLite database.

## Future Enhancements

* NLP-based skill extraction
* Resume ranking system
* Candidate search dashboard
* Multiple resume upload support

## Author

Dyapa Tharuni
