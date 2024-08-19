import streamlit as st
import os
from dotenv import load_dotenv
from litellm import completion

class LLM:
    def __init__(self, character, max_sentences=2):
        self.character = character
        self.max_sentences = max_sentences

    def generate_response(self, prompt):
        response = completion(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You are {self.character}. Respond in character. Limit your response to {self.max_sentences} sentences."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']

def main():
    st.title("LLM Conversation App")

    # Load .env file
    load_dotenv()

    # Sidebar for user inputs
    st.sidebar.header("Settings")
    
    api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    else:
        st.sidebar.warning("Please enter your OpenAI API Key")
        return

    famous_individuals = [
        "Elon Musk", "Taylor Swift", "Barack Obama", "Oprah Winfrey",
        "Leonardo DiCaprio", "Serena Williams", "Bill Gates", "Beyoncé",
        "Donald Trump", "Emma Watson"
    ]
    character1 = st.sidebar.selectbox("Select first character", famous_individuals)
    character2 = st.sidebar.selectbox("Select second character", famous_individuals, index=1)

    num_messages = st.sidebar.number_input("Number of messages", min_value=1, value=10)
    mode = st.sidebar.radio("Interaction mode", ["debate", "date"])
    max_sentences = st.sidebar.number_input("Max sentences per response", min_value=1, value=2)
    theme = st.sidebar.text_input("Theme for the conversation")

    llm1, llm2 = None, None

    if st.sidebar.button("Start Conversation"):
        if not theme:
            st.sidebar.warning("Please enter a theme for the conversation")
            return

        llm1 = LLM(character1, max_sentences)
        llm2 = LLM(character2, max_sentences)

        is_debate = mode == "debate"
        if is_debate:
            prompt = f"Let's debate about {theme}. Present your opening argument."
        else:
            prompt = f"Let's have a romantic date and talk about {theme}. Start flirting and try to make the other person fall in love with you."

        st.write(f"{character1} and {character2} will now {mode} about {theme}!")

        for i in range(num_messages):
            if i % 2 == 0:
                response = llm1.generate_response(prompt)
                st.write(f"{character1}: {response}")
            else:
                response = llm2.generate_response(prompt)
                st.write(f"{character2}: {response}")
            prompt = response

        st.write("Conversation ended. You can start a new one by changing the settings and clicking 'Start Conversation' again.")

    # User interaction
    st.header("User Interaction")
    action = st.radio("Choose an action", ["continue", "comment", "share", "quit"])

    if action == "comment":
        user_comment = st.text_input("Enter your comment as an observer")
        if st.button("Submit Comment"):
            if llm1 is None or llm2 is None:
                st.warning("Please start a conversation first.")
            elif user_comment:
                prompt = f"An observer in the audience made this comment: '{user_comment}'. How do you respond to this?"
                st.write(f"{character1} responds: {llm1.generate_response(prompt)}")
                st.write(f"{character2} responds: {llm2.generate_response(prompt)}")
            else:
                st.warning("Please enter a comment")
    elif action == "share":
        st.write("Sharing functionality not implemented yet.")
    elif action == "quit":
        st.write("Thank you for using the LLM Conversation App!")

if __name__ == "__main__":
    main()
