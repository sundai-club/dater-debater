
# Celebrity Debate or Date

Celebrity Debate or Date is a Python application that allows users to simulate either a debate or a romantic date between two famous personalities. The app lets the audience participate in the conversation.

## Features

- Select two celebrities 
- Choose between two modes: Debate or Date.
- Set a theme for the conversation.
- Audience participation: Continue the conversation, add comments, or share (sharing not yet implemented).

## Prerequisites

- Python 3.6 or later
- OpenAI API key

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/celebrity-debate-date.git
   cd celebrity-debate-date
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a copy of the `.env.example` file and name it `.env`.
   - Open the `.env` file and replace `your_api_key_here` with your actual OpenAI API key.

## How to Run

1. Navigate to the project directory:
   ```bash
   cd celebrity-debate-date
   ```

2. Run the main script:
   ```bash
   python main.py
   ```
   Alternatively, you can provide the API key as a command-line argument:
   ```bash
   python main.py --api_key your_api_key_here
   ```

3. Follow the prompts to:
   - Choose two celebrities.
   - Select the interaction mode (Debate or Date).
   - Set a theme for the conversation.

4. Enjoy the simulated interaction! You can choose to continue the conversation, add comments as an audience member, or end the session.

## Examples

### Example 1: Celebrity Debate
```bash
python main.py --characters "Elon Musk,Taylor Swift" --mode debate --theme "The Future of AI"
```
In this scenario, Elon Musk and Taylor Swift will debate the future of AI.

### Example 2: Celebrity Date
```bash
python main.py --characters "Leonardo DiCaprio,Emma Watson" --mode date --theme "abortion"
```
Here, Leonardo DiCaprio and Emma Watson will engage in a flirtatious conversation during a romantic evening in Paris.
