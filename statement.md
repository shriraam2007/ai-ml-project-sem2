# Project Statement

## Project Title
**UPSC Preparation Chatbot**

## Course
Fundamentals of AI and ML

---

## 1. Purpose of the Project

The goal of this project was to develop a simple chatbot using Python that runs in the command line. The chatbot is designed to help users by providing basic information related to UPSC preparation, such as exam pattern, subjects, recommended books, and current affairs.

It interacts with users in a conversational way and responds to queries using predefined keywords.

---

## 2. Requirements

The chatbot was built using basic programming concepts, including:

- Handling user input  
- Using dictionaries to store responses  
- Implementing loops and conditional logic  
- Performing keyword matching  
- Structuring code using functions  

---

## 3. System Design

### Data Structure
A dictionary is used to store predefined responses.  
- **Key** → keyword (e.g., "upsc", "prelims", "books")  
- **Value** → corresponding response  

### User Interaction
The chatbot continuously takes user input and checks for matching keywords to generate appropriate responses.

---

## 4. Top-Down Design / Modularization

The program is structured into functions for better clarity and maintainability:

### `chatbot()`

This is the main function and entry point of the program. It handles:

- Displaying the welcome message  
- Managing the conversation loop  
- Processing user input  
- Matching keywords with responses  
- Handling special commands like `help` and `exit`  

---

## 5. Algorithm Development

### Program Flow

1. Display a welcome message  
2. Prompt the user to enter a query  
3. Convert input to lowercase for consistency  
4. Check user input:
   - `exit` → terminate the program  
   - `help` → display available topics  
   - greetings like `hi`, `hello` → respond accordingly  
5. Search for keywords in the input  
6. If a match is found → display response  
7. If no match is found → show error message  
8. Repeat until user exits  

---

## 6. Implementation

- **Language:** Python 3  
- **Input Handling:** Case-insensitive using lowercase conversion  
- **Logic Used:** Dictionary lookup, loops, and conditional statements  

---

## 7. Testing and Refinement

The chatbot was tested manually for different scenarios:

- Different user inputs (keywords, greetings, random text)  
- Keyword matching accuracy  
- Help command functionality  
- Exit condition  

**Refinement:**  
Responses were improved and made more user-friendly for better interaction.

---

## 8. Conclusion

This project demonstrates how basic Python concepts can be used to build a simple interactive chatbot. The chatbot is easy to use and provides useful UPSC-related information.

---

## 9. Future Enhancements

- Expand the knowledge base  
- Implement Natural Language Processing (NLP)  
- Add voice interaction  
- Develop a GUI  
- Integrate real-time current affairs APIs  
