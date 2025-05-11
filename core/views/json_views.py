import json
import os
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.views import View

DATA_FILE = os.path.join(os.path.dirname(__file__), '../../data/workouts.json')

def read_data():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


@csrf_exempt
def workout_list(request):
    if request.method == 'GET':
        data = read_data()
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        body = json.loads(request.body)
        data = read_data()

        new_id = max([item['id'] for item in data], default=0) + 1
        body['id'] = new_id
        data.append(body)
        write_data(data)
        return JsonResponse(body, status=201)

    return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def workout_detail(request, workout_id):
    data = read_data()
    workout = next((item for item in data if item['id'] == workout_id), None)

    if not workout:
        return HttpResponseNotFound('Workout not found')

    if request.method == 'GET':
        return JsonResponse(workout)

    elif request.method == 'PUT':
        body = json.loads(request.body)
        workout.update(body)
        write_data(data)
        return JsonResponse(workout)

    elif request.method == 'DELETE':
        data.remove(workout)
        write_data(data)
        return JsonResponse({'message': 'Workout deleted'})

    return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])
