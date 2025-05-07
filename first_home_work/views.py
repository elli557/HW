from django.shortcuts import render

def first_page_view(request):
    if request.method == 'GET':
        
        context = {
            'emoji': '🎞️',
            'text': 'Здесь собраны лучшие фильмы, которые я рекомендую всем.',
            'run_string': 'Каждый фильм - это отдельная история, готовая покорить твое сердце.'
        }
    return render(request, template_name='index.html', context=context)