from responses import *
import random
opened = 0

def chatbot(name):
    agent_name = random.choice(agent_names)
    with open('user_logs.txt' , 'w') as file:
        file.write(f'Users name: {name}'
                   f'Agent name: {agent_name}')
    print(f'Hello {name}, my name is {agent_name}')
    running = True
    while running:
        x = random.choice(questions)
        response = input(f'\n{x} {name}? ')
        annotate(f'\n{x}?: {response}')
        if response.lower() == agent_name.lower():
            response = input(f"How may i help you {name}? ")
        elif response.lower() in quit_words:
            print(f'Goodbye {name}, i hope to speak to you soon')
            running = False
        else:
            for word in emotions:
                if word.lower() in response:
                    response = input(f'{emotion_responses[emotions.index(word)]} ')
                    annotate(f'What makes {name} {word} is {response}')
                    break
                else:
                    pass
            for word in opinions:
                if word.lower() in response:
                    response = input(f'{opinion_responses[opinions.index(word)]} ')
                    annotate(f"""{name}'s favourite {word} is {response}""")
                else:
                    pass



def annotate(data):
    with open('user_logs.txt' , 'a') as file:
        file.write(f'\n{data}')

