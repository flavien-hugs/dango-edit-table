# table/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from table.models import TableModel


def tableDataAPI(request):
    data = TableModel.objects.all()
    dataList = []

    for item in data:
        dataList.append(
            {
                'name': item.name,
                'result': item.result,
                'id': item.id,
            }
        )

    return JsonResponse(dataList, safe=False)


@csrf_exempt
def addItemTable(request):
    name = request.POST.get('name')
    result = request.POST.get('result')

    TableModel.objects.create(
        name=name, result=result,
    )

    return JsonResponse('Add success !', safe=False)


@csrf_exempt
def updateItemTable(request):
    objId = request.POST.get('id')
    result = request.POST.get('result')
    table = TableModel.objects.get(id=objId)
    table.result = result
    table.save()

    return JsonResponse('Update success !', safe=False)


@csrf_exempt
def deleteItemTable(request):
    objId = request.POST.get('id')
    table = TableModel.objects.get(id=objId)
    table.delete()

    return JsonResponse('Delete success !', safe=False)
