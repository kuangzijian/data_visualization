from django.http import HttpResponse
from  .models import Ranking
import json
from django.db.models import Q

def get_all_data(request):
    if request.method == 'GET':
        data = {"data": []}
        qs = Ranking.objects.all()
        for one_rank in qs:
            data['data'].append({
                "id": one_rank.id,
                "year": one_rank.yearRange,
                "location": one_rank.location,
                "type": one_rank.studentType,
                "tuition": one_rank.tuitionFee
                })
        return HttpResponse(status=200, content=json.dumps(data), content_type='application/json')
    else:
        return HttpResponse(status=405)

def getDistinctValue(request):
    if request.method=='GET':
        data = {"yearRange": [], 'location':[],'studentType':[]}
        yearRange = Ranking.objects.distinct().order_by().values('yearRange')
        location = Ranking.objects.distinct().order_by().values('location')
        studentType = Ranking.objects.distinct().order_by().values('studentType')
        for i in yearRange:
            data['yearRange'].append(i['yearRange'])
        for j in location:
            data['location'].append(j['location'])
        for j in studentType:
            data['studentType'].append(j['studentType'])
        return HttpResponse(status=200, content=json.dumps(data), content_type='application/json')
    else:
        return HttpResponse(status=405)


def getTuitionForTwoLocation(request):
    import json
    if request.method=='POST':
        data = {'location1':[],'location2':[]}
        body = json.loads(request.body)
        qs = Ranking.objects.filter(location = body.get('location1'), yearRange=body.get("year"))
        qs2 =Ranking.objects.filter(location = body.get('location2'), yearRange=body.get("year"))

        for one_rank in qs:
            data['location1'].append({
                "studentType": one_rank.studentType,
                "tuition": one_rank.tuitionFee
                })
        for one_rank in qs2:
            data['location2'].append({
                "studentType": one_rank.studentType,
                "tuition": one_rank.tuitionFee
                })

        return HttpResponse(status=200, content=json.dumps(data), content_type='application/json')
    else:
        return HttpResponse(status=405)
