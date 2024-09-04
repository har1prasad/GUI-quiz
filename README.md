# Trivia Quiz GUI Application

## Overview

This project is a graphical user interface (GUI) application that allows users to participate in trivia quizzes. The application is built using Python's Tkinter library for the GUI and utilizes the Open Trivia Database API to fetch trivia questions. 

## Features

- **Question Types**: The quiz supports  true/false questions.
- **Scoring System**: A scoring system to track the user's performance.
- **Dynamic Questions**: Fetches new questions from the Open Trivia Database API for each quiz session, ensuring a fresh experience every time.
- **Responsive UI**: A simple, clean, and user-friendly interface designed using Tkinter.


## API Information

- **Open Trivia Database API**: The application uses the Open Trivia Database API to fetch trivia questions in real-time.
- **API Endpoint:** `https://opentdb.com/api.php`
- **Parameters Used:**
  - `amount`: Number of questions.
  - `category`: Category ID selected by the user.
  - `difficulty`: Difficulty level selected by the user.
  - `type`: Type of questions (multiple or boolean).

## Dependencies

- **Python 3.x**
- **Tkinter**: Built-in with Python.
- **Requests**: For making HTTP requests to the API.
- **JSON**: For parsing the API responses.

### File Tree Structure

```plaintext
TriviaQuizApp/
│
├── images/                       # Folder containing image assets used in the GUI
├── data.py                       # Script possibly handling data fetching or storage
├── main.py                       # Main entry point of the application
├── question_model.py             # Defines the Question class or handles question-related data
├── quiz_brain.py                 # Manages the logic of the quiz, such as question handling and scoring
└── ui.py                         # Contains the GUI logic using Tkinter
```
