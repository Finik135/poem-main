from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Poem

@csrf_exempt  # Вимикаємо CSRF-захист (або налаштовуємо токени)
def receive_poem(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title', 'Без назви')
            text = data.get('text', '')

            if text:
                Poem.objects.create(title=title, text=text)
                return JsonResponse({'status': 'success'}, status=201)
            else:
                return JsonResponse({'error': 'Empty text'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=405)
