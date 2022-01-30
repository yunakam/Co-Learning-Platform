## About the app
This is an online forum where users can search for a course (and eventually, a book) they are studying and look for questions to answer.
Users can submit an answer to a chosen question (also uploaded by other users), and see others' responses to the same question.

## Structure
- folder "co-learning_platform" is the project folder
- folder "forum" is the app folder

## Technical notes
- For now, all you can register from front-end is questions
    - Answers can be submitted, but become invalid


## To fix
### Functionality
- forum\views.py
    - Posted answers get invalid in the next page (forum\templates\forum\question.html)

- Others
    - When trying to add a question from admin, it returns AttributeError: 'str' object has no attribute 'utcoffset'

 (last update: Jan. 28, 2022)


## Further development to do
- **Models should be organized using Subclass???**
- User registration
- Courses, chapters, questions can be posted (Currently hard-coded)
- Questions and answers can be rated
- Users can choose by which order to display questions & answers - either by date, by rating or at random

## Future development dreamed
- Auto-rate an input answer using other answers' rating by users
- Validate the input question whether it is not similar to any existing question
- Make suggestions for creating a question ("Define...", "What's wrong with...")

