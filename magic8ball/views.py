import random
from django.shortcuts import render

RESPONSES = [
    "It is certain.",
    "Ask again later.",
    "Outlook not so good.",
    "Yes, definitely!",
    "Cannot predict now.",
    "Don't count on it.",
    "Signs point to yes.",
    "My reply is no.",
    
]

def ask_question(request):
    return render(request, 'magic8ball/ask.html')
    
def show_answer(request):
    question = request.GET.get('question', '')
    answer = random.choice(RESPONSES)
    return render(request, 'magic8ball/answer.html', {'question': question, 'answer': answer})
