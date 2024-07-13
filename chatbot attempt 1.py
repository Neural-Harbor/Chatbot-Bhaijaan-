import nltk
import re

# Ensure you have the necessary NLTK data
nltk.download('punkt')

# Define predefined questions and answers with context
qa_pairs = [
    (r'hi|hello|hey|aoa', 'Hello! How can I help you today?', 'greeting'),
    (r'what is your name', 'I am Bhaijaan, created by Neural Harbor.', 'introduction'),
    (r'how are you', 'I am feeling great today. What about you?', 'wellbeing'),
    (r'I am good|good|great|theek|happy', 'Great to know. Is there anything specific you would like to talk about?', 'positive_response'),
    (r'I am sad|sad|not good|not great|bad|i am depressed|im depressed', 'Sorry to hear that, how may I help you?', 'negative_response'),
    (r'can you tell me about Neural Harbor|tell me about neural harbor|what is neural harbor', 'Neural Harbor is a youth-led organization that primarily teaches and promotes Artificial Intelligence and offers skill development. Would you like to know more?', 'neural_harbor_info'),
    (r'yes|ye|yeah', 'Great! They are currently doing a five-week Python learning fellowship and have more programs in mind. For more info, follow their Instagram or check their website neuralharbor.org.', 'more_info'),
    (r'bye|goodbye', 'Goodbye! Have a great day!', 'farewell'),
    (r'what programs do they offer', 'Neural Harbor offers various programs including Python learning fellowships, AI workshops, and more. Would you like to know the details of a specific program?', 'program_details'),
    (r'what is the python learning fellowship', 'The Python learning fellowship is a five-week program that covers the basics of Python programming and introduces participants to AI concepts. Would you like to join?', 'python_fellowship'),
    (r'how can I join|how to join', 'You can join by visiting their website neuralharbor.org and filling out the registration form.', 'joining_info'),
]

# Define a function to match patterns and maintain context
def match_pattern(user_input, qa_pairs, context):
    for pattern, response, resp_context in qa_pairs:
        if re.search(pattern, user_input, re.IGNORECASE):
            return response, resp_context
    return "I'm sorry, I don't understand that.", context

# Main chatbot function with context and follow-up questions
def chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")
    context = None
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response, context = match_pattern(user_input, qa_pairs, context)
        print(f"Chatbot: {response}")

        # Follow-up questions based on the context
        if context == 'wellbeing':
            follow_up = input("Chatbot: How can I assist you further? ")
            response, context = match_pattern(follow_up, qa_pairs, context)
            print(f"Chatbot: {response}")
        elif context == 'neural_harbor_info':
            follow_up = input("Chatbot: Would you like to join their programs or know more about specific activities? ")
            response, context = match_pattern(follow_up, qa_pairs, context)
            print(f"Chatbot: {response}")
        elif context == 'program_details':
            follow_up = input("Chatbot: Which program would you like to know more about? ")
            response, context = match_pattern(follow_up, qa_pairs, context)
            print(f"Chatbot: {response}")
        elif context == 'python_fellowship':
            follow_up = input("Chatbot: Would you like to join the Python learning fellowship? ")
            response, context = match_pattern(follow_up, qa_pairs, context)
            print(f"Chatbot: {response}")
        elif context == 'joining_info':
            print("Chatbot: Please visit neuralharbor.org to register.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
