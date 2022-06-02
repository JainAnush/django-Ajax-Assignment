from django.http import HttpResponse
from django.core.serializers import serialize
from myapp.models import quiz
import json

def index(request):
    print("request received")
    q=quiz.objects.all()
    data=serialize('json',q,fields=('question_id','correctans'))
    return HttpResponse(data,content_type='application/json')

def processresult(request):
    print("req received")
    userans=request.GET['userans']
    corrans=request.GET['corrans']
    # print(type(corrans),type(userans))
    # print(json.loads(corrans))
    # print(type(json.loads(corrans)))
    useranslist=json.loads(userans)
    corranslist=json.loads(corrans)
    score=0
    correct=0
    wrong=0
    for i in range(len(useranslist)):
        if useranslist[i]==corranslist[i]:
            score+=4
            correct+=1
        else:
            score-=1
            wrong+=1    
    resultdict={'score':score,'right':correct,'wrong':wrong,'percentage':score/(len(corranslist)*4)*100}
    json_response=json.dumps(resultdict,indent=5)
    print("json response",json_response)
    return HttpResponse(json_response,content_type='application/json')   
    