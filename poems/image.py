from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
import json
import base64
from .models import Poem

@csrf_exempt
def receive_poem(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title', 'Без назви')
            text = data.get('text', '')
            image_data = data.get('image', None)

            poem = Poem.objects.create(title=title, text=text)

            if image_data:
                format, imgstr = image_data.split(';base64,')
                ext = format.split('/')[-1]
                image_content = ContentFile(base64.b64decode(imgstr), name=f"poem_{poem.id}.{ext}")
                poem.image.save(image_content.name, image_content, save=True)

            return JsonResponse({'status': 'success'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=405)
