# Student Query Chatbot

![User Input Screenshot](Screenshots/userinput.png)

A simple rule-based chatbot that answers common student questions
(courses, timings, fees, contact info, admissions, hostel, library,
placements, exams, scholarships) using keyword pattern matching.
Available in both **console** and **web (Flask)** interface.

## Files

- `qa_dataset.csv` — the prepared dataset of question keywords and answers
- `chatbot.py` — core logic (input handling, matching, exit option) used by both interfaces
- `app.py` — Flask web server that reuses `chatbot.py` functions
- `templates/index.html` — chat page for the web interface
- `requirements.txt` — dependency list

## How to run (Console)

```bash
python chatbot.py
```

## How to run (Web)

```bash
pip install flask
python app.py
```
Then open `http://127.0.0.1:5000` in your browser.

## How it works

1. The dataset is loaded from `qa_dataset.csv` at startup.
2. User input is lowercased and stripped of punctuation.
3. Cleaned text is matched against each row's keyword list.
4. The first matching row's answer is returned.
5. If nothing matches, a default fallback message is shown.
6. Typing an exit word (bye/exit/quit) ends the console chat.
