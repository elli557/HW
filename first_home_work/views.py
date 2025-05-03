from django.shortcuts import render

def first_page_view(request):
    if request.method == 'GET':
        
        context = {
            'emoji': '🪶',
            'text': 'Моё первое домашнее задание на Django',
            'run_string': 'HomeWork'
        }
    return render(request, template_name='index.html', context=context)