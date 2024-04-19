import google.generativeai as genai

API_KEY = "AIzaSyCZg8rEBIZYKchotxqWEkgo5-fcGqVIrv4"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="gemini-1.0-pro")

chat = model.start_chat(history=[])

instruction = "respond to the questions in short but crisp and with full information"

while True:
    question = input("You: ")

    if question.strip().lower() == 'quit':
        print("Chanakya: Goodbye!")
        break

    # Check if the question contains stock-related keywords
    stock_keywords = ['hello', 'stock', 'market', 'company', 'investment', 'portfolio', 'finance', 'NASDAQ', 'NYSE', 'S&P', 'Dow Jones', 'index', 'help', 'saving', 'advice']
    if any(keyword in question.lower() for keyword in stock_keywords):
        response = chat.send_message(instruction + ' ' + question)
        print(f"Bot: {response.text}")
        instruction = ''
    else:
        print("Chanakya: Please ask a question related to the stock market.")