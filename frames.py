"""
Skinner Teaching Machine - Frame Definitions
COMP 395: AI and Learning Technologies

This file contains the instructional frames for your teaching machine.

=============================================================================
YOUR TASK:
=============================================================================
1. Choose a topic you want to teach (5-10 frames minimum)
2. Design your frame structure (see options below)
3. Write frames that follow Skinner's principles:
   - Small steps: Each frame teaches ONE small concept
   - Build sequentially: Later frames build on earlier ones
   - High success rate: Design for ~95% correct answers
   - Clear prompts: Unambiguous fill-in-the-blank or short answer

=============================================================================
FRAME STRUCTURE OPTIONS:
=============================================================================

OPTION A - Minimal:
frame = {
    "prompt": "The capital of France is _____.",
    "answer": "paris"
}

OPTION B - With feedback (RECOMMENDED):
frame = {
    "prompt": "The capital of France is _____.",
    "answer": "paris",
    "feedback_correct": "Correct! Paris is the capital of France.",
    "feedback_incorrect": "Not quite. The answer is Paris."
}

OPTION C - Rich (with hints and multiple answers):
frame = {
    "prompt": "What keyword defines a function in Python?",
    "answer": "def",
    "answers": ["def"],  # List for multiple acceptable answers
    "hint": "It's a 3-letter word.",
    "feedback_correct": "Yes! 'def' is used to define functions.",
    "feedback_incorrect": "Not quite. We use 'def' to define functions.",
    "topic": "python-functions"
}

Choose a structure and be CONSISTENT across all your frames!
=============================================================================
"""

# =============================================================================
# EXAMPLE FRAMES: Introduction to Python Variables
# Replace these with your own topic!
# =============================================================================

FRAMES = [
    # Frame 1: Introduction
    {
        "prompt": "In Alladin, the main character is _____.",
        "answer": "Alladin",
        "feedback_correct": "Correct! The movie called Alladin is about Alladin.",
        "feedback_incorrect": "Not quite. Hint - The movie is named after him!"
    },
    
    # Frame 2: Assignment operator
    {
        "prompt": "Alladin's sings this song when he tries to become a prince: ____.",
        "answer": "Prince Ali",
        "feedback_correct": "Yes! Prince Ali fabulous he...",
        "feedback_incorrect": "Not quite. The song is called 'Prince __' (google it)."
    },
    
    # Frame 3: Simple assignment
    {
        "prompt": "To store the number 5 in a variable called x, we write: x _____ 5",
        "answer": "=",
        "feedback_correct": "Correct! x = 5 assigns the value 5 to x.",
        "feedback_incorrect": "Remember, we use = for assignment. So: x = 5"
    },
    
    # Frame 4: String variables
    {
        "prompt": "Text data in Python is called a _____.",
        "answer": "string",
        "feedback_correct": "Yes! Strings are sequences of characters (text).",
        "feedback_incorrect": "Text data is called a string."
    },
    
    # Frame 5: Princess Jasmine
    {
        "prompt": "The princess in Aladdin is named _____.",
        "answer": "jasmine",
        "feedback_correct": "Correct! The princess in Aladdin is named Jasmine!",
        "feedback_incorrect": "No. But I'll give you a hint: it is a type of flower."
    },
    
    # Frame 6: Princess Jasmine song
    {
        "prompt": "What is Princess Jasmine's most famous song?",
        "answer": "a whole new world",
        "feedback_correct": "Yessss that's right! It truly is one of the best Disney songs of all time.",
        "feedback_incorrect": "Noooo. Try again, it's a duet."
    },
    
    # Frame 7: Drag-and-drop - who sings this song?
    {
        "type": "drag",
        "prompt": "Drag the character(s) who sing the song 'A Whole New World'.",
        # the correct answers (normalized to lowercase)
        "answer": "aladdin,jasmine",
        # options presented as draggable choices (display text)
        "options": ["Aladdin", "Jasmine", "Genie", "Jafar", "Iago", "Sultan"],
        "feedback_correct": "Correct! 'A Whole New World' is sung by Aladdin and Jasmine.",
        "feedback_incorrect": "Not quite. That song is a duet sung by Aladdin and Jasmine."
    },
    
    # Frame 8: Drag-and-drop - who sings this song?
    {
        "type": "drag",
        "prompt": "Drag the character(s) who sing the song 'Prince Ali'.",
        "answer": "genie",
        "options": ["Aladdin", "Jasmine", "Genie", "Jafar", "Iago", "Sultan"],
        "feedback_correct": "Correct! 'Prince Ali' is performed by the Genie.",
        "feedback_incorrect": "Not quite. 'Prince Ali' is performed by the Genie."
    },
]


# =============================================================================
# TIPS FOR WRITING GOOD FRAMES:
# =============================================================================
# 
# 1. START EASY: First frames should be very simple
# 
# 2. ONE CONCEPT PER FRAME: Don't combine multiple ideas
# 
# 3. USE BLANKS STRATEGICALLY: 
#    "In Python, we use _____ to define a function."
#    Not: "What do we use to define a function in Python?"
# 
# 4. BUILD ON PREVIOUS FRAMES: Frame 5 can reference concepts from Frame 3
# 
# 5. ANTICIPATE ERRORS: Your feedback_incorrect should address common mistakes
# 
# 6. NORMALIZE ANSWERS: The app converts to lowercase and strips whitespace,
#    but consider if "=" and "equals" should both be accepted
#
# =============================================================================
