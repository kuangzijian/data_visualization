from django.http import HttpResponse
from .models import Ranking
import json

def get_all_data(request):
    if request.method == 'GET':
        data = {"data": []}
        qs = Ranking.objects.all()
        for one_rank in qs:
            data['data'].append({
                "id": one_rank.id,
                "year": one_rank.yearRange,
                "location": one_rank.location,
                "total number of 1 does": one_rank.numtotal_1dose,
                "total number of 2 does": one_rank.numtotal_2dose
                })
        return HttpResponse(status=200, content=json.dumps(data), content_type='application/json')
    else:
        return HttpResponse(status=405)

def getDistinctValue(request):
    if request.method=='GET':
        data = {"yearRange": [], 'location': []}
        yearRange = Ranking.objects.distinct().order_by().values('yearRange')
        location = Ranking.objects.distinct().order_by().values('location')
        numtotal_1dose = Ranking.objects.distinct().order_by().values('numtotal_1dose')
        numtotal_2dose = Ranking.objects.distinct().order_by().values('numtotal_2dose')
        for i in yearRange:
            data['yearRange'].append(i['yearRange'])
        for j in location:
            data['location'].append(j['location'])
        return HttpResponse(status=200, content=json.dumps(data), content_type='application/json')
    else:
        return HttpResponse(status=405)

def getVaccinationForTwoLocation(request):
    if request.method=='POST':
        data = {'location1': [], 'location2': []}
        body = json.loads(request.body)
        qs = Ranking.objects.filter(location=body.get('location1'), yearRange=body.get("year"))
        qs2 = Ranking.objects.filter(location=body.get('location2'), yearRange=body.get("year"))

        for one_rank in qs:
            data['location1'].append({
                "numtotal_1dose": one_rank.numtotal_1dose,
                "numtotal_2dose": one_rank.numtotal_2dose
                })
        for one_rank in qs2:
            data['location2'].append({
                "numtotal_1dose": one_rank.numtotal_1dose,
                "numtotal_2dose": one_rank.numtotal_2dose
                })

        return HttpResponse(status=200, content=json.dumps(data), content_type='application/json')
    else:
        return HttpResponse(status=405)
