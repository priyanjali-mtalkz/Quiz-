import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['Quiz']        
coll = db['Question']

quiz_questions = [{
    "Level" : "Easy",
    "questions" :
    [{
    "question" : "How many legs does a spider have?",
    "option1" : "A: Six",
    "option2" : "B: Ten",
    "option3" : "C: Eight",
    "option4" : "D: Four",
    "answer" : "C",

    },
    {
    "question" : "What is the name of the toy cowboy in Toy Story?",
    "option1" : "A: Stella",
    "option2" : "B: Woody",
    "option3" : "C: Clara",
    "option4" : "D: Stanley",
    "answer" : "B",
    
    },
    {
    "question" : "What is the color of an emerald?",
    "option1" : "A: Red",
    "option2" : "B: Green",
    "option3" : "C: Blue",
    "option4" : "D: Black",
    "answer" : "B",
    
    },
    {
    "question" : "Where does the President of the United States live while in office?",
    "option1" : "A: The White House",
    "option2" : "B: President's House",
    "option3" : "C: PM Office",
    "option4" : "D: Capital house",
    "answer" : "A",
    },
    {
    "question" : "Where does Santa Claus live?",
    "option1" : "A: The South Pole",
    "option2" : "B: The North Pole",
    "option3" : "C: The East Pole",
    "option4" : "D: The West Pole",
    "answer" : "B",
    
    }]},


    {
    "Level" : "Medium",
    "questions" : [{
    "question" : "What year did the Titanic sink in the Atlantic Ocean on 15 April, on its maiden voyage from Southampton?",
    "option1" : "A: 1932",
    "option2" : "B: 1902",
    "option3" : "C: 1912",
    "option4" : "D: 1905",
    "answer" : "C",
    
    },
    {
    "question" : " What is the capital of Portugal?",
    "option1" : "A: Lisbon",
    "option2" : "B: Coimbra",
    "option3" : "C: Viana do Castelo",
    "option4" : "D: Castelo Branco",
    "answer" : "A",
    
    },
    {
    "question" : "What is the world’s smallest bird?",
    "option1" : "A: Songbirds",
    "option2" : "B: American Goldfinch",
    "option3" : "C: Bee Hummingbird",
    "option4" : "D: Common Starling",
    "answer" : "C",

    },
    {
    "question" : "What is the lifespan of a dragonfly?",
    "option1" : "A: 48 hours",
    "option2" : "B: 24 hours",
    "option3" : "C: 12 hours",
    "option4" : "D: 6 hours",
    "answer" : "B",
    },
    {
    "question" : "Who invented the tin can for preserving food in 1810?",
    "option1" : "A: Albert Einstein",
    "option2" : "B: Georg Simon Ohm",
    "option3" : "C: Peter Durand",
    "option4" : "D: John Dalton",
    "answer" : "C",
    
    }]},
    {
    "Level" : "Hard",
    "questions" : [{
        "question" : "What's the capital of Norway",
        "option1" : "A.Stockholm",
        "option2" :  "B.Copenhagen", 
        "option3" : "C.Helsinki",
        "option4" :  "D. Oslo",        
        "answer" : "D",

    },
    {
    "question" : "What's the state capital of Texas, USA",
    "option1" : "A.Harrisburg",
    "option2": "B. Houston",
    "option3" :  "C. Columbia", 
    "option4" :  "D. Austin",
    "answer" : "D",    
    },
    {   
    "question" : "When was the first public version of Python released?",
    "option1" : "A.January 1991",
    "option2" :  "B.October 2000",
    "option3" :  "C.December 2008",
    "option4" : "D.January 1994",
    "answer" : "A",
    
    },
    {
    "question" : "What's the name of Python's sorting algorithm",
    "option1" : "A.Bubble sort",
    "option2" :  "B. Insertion sort",
    "option3" : "C. Time Sort",
    "option4" : "D. Quick sort",
    "answer" : "A",

    },
    {
    "question" : "Who created Python?",
    "option1" : "A. Guido van Rossum",
    "option2" : "B. Elon Musk ",
    "option3" : "C. Bill Gates",
    "option4" : "D. Mark Zuckerburg",
    "answer" : "A",

}]}]

#coll.insert_many(quiz_questions)