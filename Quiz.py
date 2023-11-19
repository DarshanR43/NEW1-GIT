import random

questions= [
    {"question": "What is the capital of Australia?",
     "options": ["Sydney", "Melbourne", "Canberra", "Perth"],
     "answer": "Canberra"},
    
    {"question": "Who wrote 'To Kill a Mockingbird'?",
     "options": ["J.K. Rowling", "Harper Lee", "George Orwell", "Ernest Hemingway"],
     "answer": "Harper Lee"},
    
    {"question": "Which planet is known as the 'Red Planet'?",
     "options": ["Mars", "Venus", "Jupiter", "Saturn"],
     "answer": "Mars"},
    
    {"question": "In what year did World War II end?",
     "options": ["1943", "1945", "1950", "1939"],
     "answer": "1945"},
    
    {"question": "Which programming language was created by Guido van Rossum?",
     "options": ["Java", "Python", "C++", "JavaScript"],
     "answer": "Python"},
    
    {"question": "Who is known as the 'Father of Physics'?",
     "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Niels Bohr"],
     "answer": "Isaac Newton"},
    
    {"question": "What is the chemical symbol for gold?",
     "options": ["Au", "Ag", "Fe", "Hg"],
     "answer": "Au"},
    
    {"question": "Which continent is the largest by land area?",
     "options": ["Asia", "Africa", "North America", "South America"],
     "answer": "Asia"},
    
    {"question": "Who directed the movie 'Inception'?",
     "options": ["Christopher Nolan", "Steven Spielberg", "Quentin Tarantino", "Martin Scorsese"],
     "answer": "Christopher Nolan"},
    
    {"question": "What is the speed of light in a vacuum?",
     "options": ["300,000 km/s", "150,000 km/s", "500,000 km/s", "1,000,000 km/s"],
     "answer": "300,000 km/s"}
]
f1= open('Quiz','w')
f1.write(str(questions))
f1.close()
f2= open('Quiz','r')
print(f2.read())

for i in questions:
    questions.split(',')
    print(questions)
f2.close()