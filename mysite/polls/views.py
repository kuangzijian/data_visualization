from django.http import HttpResponse
from .models import Ranking
import json

def get_all_data(request):
    # a function to retrieve all data from database
    if request.method == 'GET':
        data = {"data": []}
        qs = Ranking.objects.all()
        for one_rank in qs:
            data['data'].append({
                "id": one_rank.id,
                "year": one_rank.yearRange,
                "location": one_rank.location,
                "type": one_rank.type,
                "total_number": one_rank.total_number
                })
        return HttpResponse(status=200, content=json.dumps(data), content_type='application/json')
    else:
        return HttpResponse(status=405)

def getDistinctValue(request):
    # a function to retrieve the data that can be dumped into the filters
    if request.method=='GET':
        data = {"yearRange": [], 'location':[],'type':[]}
        yearRange = Ranking.objects.distinct().order_by().values('yearRange')
        location = Ranking.objects.distinct().order_by().values('location')
        type = Ranking.objects.distinct().order_by().values('type')
        for i in yearRange:
            data['yearRange'].append(i['yearRange'])
        for j in location:
            data['location'].append(j['location'])
        for j in type:
            data['type'].append(j['type'])
        return HttpResponse(status=200, content=json.dumps(data), content_type='application/json')
    else:
        return HttpResponse(status=405)


def getVaccinationForTwoLocation(request):
    # a function to retrieve the vaccination information based on the location and year filters.
    import json
    if request.method=='POST':
        data = {'location1':[],'location2':[]}
        body = json.loads(request.body)
        qs = Ranking.objects.filter(location = body.get('location1'), yearRange=body.get("year"))
        qs2 =Ranking.objects.filter(location = body.get('location2'), yearRange=body.get("year"))

        for one_rank in qs:
            data['location1'].append({
                "type": one_rank.type,
                "total_number": one_rank.total_number
                })
        for one_rank in qs2:
            data['location2'].append({
                "type": one_rank.type,
                "total_number": one_rank.total_number
                })

        return HttpResponse(status=200, content=json.dumps(data), content_type='application/json')
    else:
        return HttpResponse(status=405)
