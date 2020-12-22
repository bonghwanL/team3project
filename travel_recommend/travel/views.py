from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse

import json



# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def SearchFunction(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        if start_date == '':
            start_date = None
        if end_date == '':
            end_date = None
        
        print(search)
        print(start_date)
        print(end_date)
        print('a')
        #collection_handle = get_collection_handle(db_handle, 'testdb')
        #data = collection_handle.find({'도시' : '충주'}) # 도시가 충주인것 찾음
        
        data = collection_handle.find_one({'도시' : search}) # 한개만 찾을때
        print(data['도시']) # 부산광역시
        list1 = [] # 루트1
        list2 = [] # 루트2
        list3 = [] # 루트3
        list4 = [] # 루트4
        list5 = [] # 루트5
        print()
        count = 0
        
        while True: # 루트 5개만 하고 멈춤
            for i in range(0, len(data['장소']), 5):
                print(data['장소'][i : i + 5])
                print(data['주소'][i : i + 5])
                count += 1
                if count == 5:
                    break
            
        
        
        
        
        weather = 'rainy'
        root = ['루트1', '루트2', '루트3', '루트4', '루트5']
        # tour = ['여행지1', '여행지2', '여행지3', '여행지4', '여행지5']
        tour = data['장소'][:5]
        
        restaurant = ['음식점1', '음식점2', '음식점3', '음식점4', '음식점5']
        
        
        context={'travel':search, 'start':start_date, 'end':end_date, 'root':root, 'tour':tour, 'restaurant':restaurant}
        return render(request, 'main.html', context)
        #return HttpResponse()
    
def DetailFunction(request):
    
    return render(request, 'detail.html')
