import os
import argparse
import random
from dotenv import load_dotenv
from litellm import completion

class LLM:
    def __init__(self, character, max_sentences=2):
        self.character = character
        self.max_sentences = max_sentences

    def generate_response(self, prompt):
        response = completion(
            model="gpt-4o-mini",  # Updated model name
            messages=[
                {"role": "system", "content": f"You are {self.character}. Respond in character. Limit your response to {self.max_sentences} sentences."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']

def choose_characters():
    famous_individuals = [
        "Elon Musk", "Taylor Swift", "Barack Obama", "Oprah Winfrey",
        "Leonardo DiCaprio", "Serena Williams", "Bill Gates", "Beyoncé",
        "Donald Trump", "Emma Watson"
    ]
    print("Choose two characters (enter the numbers separated by a comma):")
    for i, character in enumerate(famous_individuals, 1):
        print(f"{i}. {character}")
    choices = input("Enter your choices (e.g., 1,5): ").split(',')
    return [famous_individuals[int(choice.strip()) - 1] for choice in choices]

def get_theme():
    return input("Enter a theme for the conversation: ")

def have_conversation(llm1, llm2, theme, num_messages, is_debate):
    if is_debate:
        prompt = f"Let's debate about {theme}. Present your opening argument."
    else:
        prompt = f"Let's have a romantic date and talk about {theme}. Start flirting and try to make the other person fall in love with you."
    output = {'messages': []} 
    for i in range(num_messages):
        if i % 2 == 0:
            response = llm1.generate_response(prompt)
            output['messages'].append({'character': llm1.character, 'content': response})
            # print(f"{llm1.character}: {response}")
            # print()
            prompt = response
        else:
            response = llm2.generate_response(prompt)
            output['messages'].append({'character': llm2.character, 'content': response})
            # print(f"{llm2.character}: {response}")
            # print()
            prompt = response
    import json
    print(json.dumps(output, indent=4))
def main(api_key=None, characters=None, num_messages=10, is_debate=True, max_sentences=2, theme="Artificial Intelligence"):
    # Load .env file
    load_dotenv()

    # Set OpenAI API key
    api_key = api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OpenAI API key must be provided either in .env file or via --api_key argument.")
        return

    os.environ["OPENAI_API_KEY"] = api_key

    # print("Welcome to the LLM Conversation App!")
    
    if characters:
        character1, character2 = characters.split(',')
    else:
        character1, character2 = choose_characters()
    
    llm1 = LLM(character1, max_sentences)
    llm2 = LLM(character2, max_sentences)
    
    theme = theme or get_theme()

    
    interaction_type = "debate" if is_debate else "date"
    # print(f"\n{character1} and {character2} will now {interaction_type} about {theme}!\n")
    
    while True:
        have_conversation(llm1, llm2, theme, num_messages, is_debate)
        break
        
        # action = input("Choose an action (continue/comment/share/quit): ").lower()
        
        # while action not in ['continue', 'comment', 'share', 'quit']:
        #     print("Invalid action. Please try again.")
        #     action = input("Choose an action (continue/comment/share/quit): ").lower()
        
        
        # if action == 'continue':
        #     print("Continuing the conversation...")
        #     continue
        # elif action == 'comment':
        #     user_comment = input("Enter your comment as an observer: ")
        #     prompt = f"An observer in the audience made this comment: '{user_comment}'. How do you respond to this?"
        #     print(f"{character1} responds: {llm1.generate_response(prompt)}")
        #     print(f"{character2} responds: {llm2.generate_response(prompt)}")
        # elif action == 'share':
        #     print("Sharing functionality not implemented yet.")
        # elif action == 'quit':
        #     print("Thank you for using the LLM Conversation App!")
        #     break
        # else:
        #     print("Invalid action. Please try again.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LLM Conversation App")
    parser.add_argument("--api_key", help="OpenAI API Key")
    parser.add_argument("--characters", help="Two character names separated by a comma")
    parser.add_argument("--num_messages", type=int, default=10, help="Number of messages in the conversation")
    parser.add_argument("--mode", choices=['debate', 'date'], default='debate', help="Interaction mode: debate or date")
    parser.add_argument("--max_sentences", type=int, default=2, help="Maximum number of sentences per response")
    parser.add_argument("--theme", default=None, help="Theme for the conversation")
    
    args = parser.parse_args()
    main(args.api_key, args.characters, args.num_messages, args.mode == 'debate', args.max_sentences, args.theme)
