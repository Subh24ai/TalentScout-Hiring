# TalentScout-Hiring

TalentScout Hiring Assistant is a simple web application made with Streamlit and Hugging Face's GPT-2 model for easy recruitment processing between the recruiters and candidates. It acts as an intelligent assistant in helping extract essential candidate information, providing technical interview questions, and helping them get through easier communication with candidates.
Let us see what constitutes the main body of this project:

### 1. Core Functionality:
Personal Information Collection: The app collects the candidate's basic details through a sidebar form, such as:

Full Name: 

Email Address:

Phone Number:

Years of Experience:

Desired Position(s):

Current Location:

Tech Stack (technologies a candidate is proficient in)
Welcome and Introduction: Upon arrival, the app welcomes the user with a personalized message describing its purpose. It also offers the ability to end the conversation by typing in keywords like "exit," "quit," or "bye."

### 2. Technical Question Generation (Using GPT-2):
One of the greatest features of this app is its ability to generate technical interview questions based on a candidate's tech stack, such as Python, TensorFlow, PyTorch, and so on.
This is powered by the GPT-2 model from Hugging Face. The model is trained to understand technical language and can generate meaningful, context-specific questions.
How it works:
When the user inputs the list of technologies, the application generates 3-5 questions related to them.
Example : If the technology stack includes "Python, TensorFlow, PyTorch," relevant coding and conceptual questions related to those technologies would be generated for the user by the application.

### 3. Interactive Features:
User Interaction: The assistant interacts with the user by giving answers to input in a conversational manner.

If the user clicks the submit button with their details, the assistant shows a summary of the input.
If the user clicks the button to create technical questions, the app generates questions.
The assistant is created to answer user inputs and ask follow-up questions.
Exit Options:

If the user wants to quit, typing keywords such as "exit", "quit", or "bye" ends the conversation elegantly.
This way, users are in control of the interaction.
