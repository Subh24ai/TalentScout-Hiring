import streamlit as st
from transformers import pipeline

# Load the Hugging Face model (GPT-2)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

# Initialize the app
st.title("TalentScout Hiring Assistant")
st.sidebar.title("Chat Settings")

# Sidebar configuration
conversation_ending_keywords = ["exit", "quit", "bye"]
name = st.sidebar.text_input("Full Name", "")
email = st.sidebar.text_input("Email Address", "")
phone = st.sidebar.text_input("Phone Number", "")
years_experience = st.sidebar.number_input("Years of Experience", 0, 50, step=1)
desired_position = st.sidebar.text_input("Desired Position(s)", "")
current_location = st.sidebar.text_input("Current Location", "")
tech_stack = st.sidebar.text_area("Tech Stack", "e.g., Python, TensorFlow, PyTorch")

# Introduction
def greet_user():
    st.write("Hello! Welcome to TalentScout's Hiring Assistant. I am here to help gather information about you and test your technical expertise.")
    st.write("You can exit the conversation at any time by typing 'exit', 'quit', or 'bye'.")

# Technical Question Generator using GPT-2
def generate_questions(tech_stack):
    model = load_model()
    prompt = f"Generate 3-5 technical interview questions for the following tech stack: {tech_stack}"
    
    try:
        # Use GPT-2 to generate the questions
        response = model(prompt, max_length=150, num_return_sequences=1)
        
        # Extract the generated text
        generated_text = response[0]['generated_text']
        return generated_text.strip()
    
    except Exception as e:
        st.error(f"An error occurred while generating questions: {e}")
        return ""

# Conversation Flow
def main():
    if name and email and phone:
        greet_user()
        st.write(f"Nice to meet you, {name}!")

        if st.button("Submit My Information"):
            st.write("Thanks for sharing your details. Here's a quick summary:")
            st.write(f"- **Name:** {name}")
            st.write(f"- **Email:** {email}")
            st.write(f"- **Phone Number:** {phone}")
            st.write(f"- **Experience:** {years_experience} years")
            st.write(f"- **Desired Position(s):** {desired_position}")
            st.write(f"- **Current Location:** {current_location}")
            st.write(f"- **Tech Stack:** {tech_stack}")

        if st.button("Generate Technical Questions"):
            if tech_stack:
                questions = generate_questions(tech_stack)
                st.write("Here are your technical questions:")
                st.write(questions)
            else:
                st.write("Please specify your tech stack in the sidebar.")

        user_input = st.text_input("Chat with the Assistant")

        if user_input.lower() in conversation_ending_keywords:
            st.write("Thank you for using TalentScout's Hiring Assistant. We'll get back to you soon. Goodbye!")
        elif user_input:
            st.write("Assistant: I'm sorry, I didn't quite catch that. Can you rephrase?")

    else:
        st.write("Please fill in your details in the sidebar to begin.")

if __name__ == "__main__":
    main()
