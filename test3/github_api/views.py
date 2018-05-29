# coding: utf-8


from django.http import JsonResponse

from github_api.helpers import (
        call_github_api, refine_data, make_response
)


def github_events(request):
    
    call_type = request.GET.get('sort')

    data = call_github_api()
    refined_data = refine_data(data)

    response = make_response(refined_data, sort=sort)
    return JsonResponse(response, safe=False)    

