# Student Query Chatbot

A simple rule-based chatbot that answers common student questions
(courses, timings, fees, contact info, admissions, hostel, library,
placements, exams, scholarships, hello) using keyword pattern matching.

## Files

- `qa_dataset.csv` — the prepared dataset of question keywords and answers
- `chatbot.py` — main program (input handling, matching logic, exit option)
- `requirements.txt` — dependency list (none required by default)

## How to run

1. Make sure Python 3 is installed:
   ```
   python --version
   ```

2. Open a terminal in this folder and run:
   ```
   python chatbot.py
   ```

3. Type a question, e.g.:
   ```
   You: what are the fees for this course
   Bot: The course fee is Rs. 50,000 per semester, payable in two installments.
   ```

4. Type `bye` or `exit` to end the chat.

## How it works

1. The chatbot loads `qa_dataset.csv` into memory at startup.
2. Each user message is lowercased and stripped of punctuation.
3. The cleaned text is checked against each row's keyword list.
4. The first matching row's answer is shown to the user.
5. If no keyword matches, a default fallback message is shown.
6. Typing an exit word (bye/exit/quit/goodbye) ends the loop.
