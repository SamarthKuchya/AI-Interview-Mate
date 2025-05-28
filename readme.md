# 🧐 AI Interview Questions Generator

This is a Streamlit-based web application that leverages **Google's Gemini API** to generate **15 personalized interview questions** based on a candidate's resume. These questions cover technical, behavioral, and situational topics, helping candidates prepare smarter for interviews.

---

## 🚀 Features

* 📄 Upload resume in **PDF** or **DOCX** format
* 🧠 Get **15 AI-generated** interview questions
* ⚙️ Uses **Gemini 2.0 Flash Model** for quick response
* 💻 Clean and responsive UI with **Streamlit**

---

## 🛠️ Tech Stack

* **Frontend/UI**: [Streamlit](https://streamlit.io/)
* **AI Model**: [Google Generative AI (Gemini)](https://ai.google.dev/)
* **Environment Management**: [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📦 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/interview-questions-generator.git
cd interview-questions-generator
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

### 4. Add your Google API key

Create a `.env` file in the root directory and add the following:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📄 Example Usage

Upload this resume summary:

```
Role: Software Developer
Skills: Java, Spring Boot, REST APIs, MySQL, Git
Experience: 2 years backend development
Projects: E-commerce API, Task Management System
```

You may get questions like:

* How have you used Spring Boot in your recent projects?
* Can you explain the architecture of the e-commerce API?
* Describe a time when you optimized a database query.
* How do you manage version control using Git in a team setting?

---

## 📁 File Structure

```
├── app.py               # Main Streamlit application
├── .env                 # Environment file for API keys
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---