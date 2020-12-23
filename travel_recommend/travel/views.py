<<<<<<< HEAD
<<<<<<< HEAD
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse

import json


=======
=======
>>>>>>> refs/heads/main
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
<<<<<<< HEAD
>>>>>>> main

from django.urls import reverse

from travel.models import Travel, Tuser, Treview
# from travel.utils import get_db_handle, get_collection_handle
 
def IndexFunc(request):
    return render(request, 'index.html')

def LoginFunc(request):
    id = request.POST.get('id')
    pwd = request.POST.get('pwd')
    #print(id)
    #print(pwd)

    if Tuser.objects.filter(user_id = id).exists() == True:
        tusers = Tuser.objects.filter(user_id = id)
    else:
        ss = '''
            <script> 
                alert('아이디 또는 비밀번호가 일치하지 않습니다');
                history.back();
            </script>
        '''
        return render(request, 'index.html', {'error' : ss})
    
    for user in tusers:
        print(user.user_pwd)
        if user.user_pwd != pwd:
            return render(request, 'index.html')
        
        request.session['user'] = user.user_name
        return redirect('main') # urls에 name값 할당
        
def LogoutFunc(request):
    print(request.session.get('user'))
    if request.session.get('user'):
        del(request.session['user'])
    #print(request.session.get('user')) # 세션 삭제된것 확인
    return redirect('home')

=======
from django.urls import reverse
from travel.models import Travel, Tuser, Treview
# from travel.utils import get_db_handle, get_collection_handle
from travel.weather import Weather
>>>>>>> refs/heads/main

# Create your views here.
def IndexFunc(request):
    return render(request, 'index.html')

def LoginFunc(request):
    id = request.POST.get('id')
    pwd = request.POST.get('pwd')

    if Tuser.objects.filter(user_id = id).exists() == True:
        tusers = Tuser.objects.filter(user_id = id)
    else:
        ss = '''
            <script> 
                alert('아이디 또는 비밀번호가 일치하지 않습니다');
                history.back();
            </script>
        '''
        return render(request, 'index.html', {'error' : ss})
    
    for user in tusers:
        print(user.user_pwd)
        if user.user_pwd != pwd:
            return render(request, 'index.html')
        
        request.session['user'] = user.user_name
        return redirect('main') # urls에 name값 할당
        
def LogoutFunc(request):
    print(request.session.get('user'))
    if request.session.get('user'):
        del(request.session['user'])
    #print(request.session.get('user')) # 세션 삭제된것 확인
    return redirect('home')

def MainFunc(request):
    user_log = request.session.get('user')
    print(user_log) # 세션 값 = 사용자 이름
    
<<<<<<< HEAD
    
=======
>>>>>>> refs/heads/main
    return render(request, 'main.html', {'user_log' : user_log})

def SearchFunction(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
<<<<<<< HEAD
        weather = 'rainy'
=======
        user_log = request.session.get('user')
        print(user_log) # 세션 값 = 사용자 이름
        #print(search)
>>>>>>> refs/heads/main

        if start_date == '':
            start_date = None
            weather = ''
        if end_date == '':
            end_date = None
<<<<<<< HEAD
            weather = ''    
=======
            weather = ''
            
        wlist = []
        # 날씨 출력    
        try:
            weather = Weather(search)
            
            query = (weather['date'] >= start_date) & (weather['date'] <= end_date)
            
            for i in range(len(weather.loc[query]['weather'].values)):
                
                w = weather.loc[query]['weather'].values[i]
                if (w >= 1 and w <= 3) or (w >= 33 and w <= 35):
                    w = '맑음'
                elif (w >= 4 and w <= 5) or (w >= 36 and w <= 37):
                    w = '구름 조금'
                elif (w >= 6 and w <= 8) or (w == 38):
                    w = '흐림'
                elif (w == 11):
                    w = '안개'
                elif (w == 12 or w == 13):
                    w = '소나기'
                elif (w >= 14 and w <= 17) or (w == 39):
                    if (w == 15 or w == 16) or (w == 41 or w == 42):
                        w = '천둥번개와 비'
                    w = '한때 비'
                elif w == 18 and w <= 40:
                    if (w >= 19 and w <= 21) or (w == 32):
                        w = '강풍'
                    elif(w == 23 or w == 24) or (w == 29) or (w == 43 or w == 44):
                        w = '눈'
                    elif(w == 25):
                        w = '진눈깨비'
                    elif(w == 26):
                        w = '얼어붙은 비'
                    w = '비'
                elif w == 30:
                    w = '뜨거움 - 주의'
                elif w == 31:
                    w = '추움 - 주의'
                wlist.append(w)
            print(wlist)   
        except: 
            print('===날짜가 없을경우===')
            print(start_date)
            print(end_date)

        ###
        ### 데이터 분석 받아오는곳
        ###
>>>>>>> refs/heads/main
        
<<<<<<< HEAD
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
            
        
        
        
        

        ###
        ### 데이터 분석 받아오는곳
        ###
        
        travel = Travel.objects.all()
        tuser = Tuser.objects.all()
        treview = Treview.objects.all()  
=======
        travel = Travel.objects.all()
        tuser = Tuser.objects.all()
        treview = Treview.objects.all()
>>>>>>> refs/heads/main
        
<<<<<<< HEAD
        weather = 'rainy'
=======
>>>>>>> refs/heads/main

        root = ['루트1', '루트2', '루트3', '루트4', '루트5']
<<<<<<< HEAD
        # tour = ['여행지1', '여행지2', '여행지3', '여행지4', '여행지5']
        tour = data['장소'][:5]
        
        restaurant = ['음식점1', '음식점2', '음식점3', '음식점4', '음식점5']
=======
        tour = ['여행지1', '여행지2', '여행지3', '여행지4', '여행지5']
>>>>>>> refs/heads/main
        
<<<<<<< HEAD
        
        context={'travel':search, 'start':start_date, 'end':end_date, 'weather':weather, 'root':root, 'tour':tour, 'restaurant':restaurant}
        #return render(request, 'main.html', context)
=======
        context={'travel':search, 'start':start_date, 'end':end_date, 'weather': wlist, 'root':root, 'tour':tour, \
                  'user_log' : user_log}
>>>>>>> refs/heads/main
        return render(request, 'main.html', context)
<<<<<<< HEAD
        #return HttpResponse()
=======
        return HttpResponseRedirect(reverse(''))
    
>>>>>>> main
    
<<<<<<< HEAD
def DetailFunction(request):
    return render(request, 'detail2.html')

def SignupFunction(request):
=======
>>>>>>> refs/heads/main
    
<<<<<<< HEAD
<<<<<<< HEAD
    return render(request, 'detail.html')
=======
    return render(request, 'signup.html')

def SignupFunction2(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ID = request.POST.get('ID')
        password = request.POST.get('password')
        travel1 = request.POST.get('travel1')
        rating1 = request.POST.get('rating1')
        travel2 = request.POST.get('travel2')
        rating2 = request.POST.get('rating2')
        travel3 = request.POST.get('travel3')
        rating3 = request.POST.get('rating3')
        
        print(name, ID, password)
        print(travel1, travel2, travel3)
        print(rating1, rating2, rating3)
        
        return redirect('home')
    return render(request, 'datail.html')

>>>>>>> main
=======
def DetailFunction(request):
    return render(request, 'detail2.html')

def SignupFunction(request):
    return render(request, 'signup.html')

def SignupFunction2(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ID = request.POST.get('ID')
        password = request.POST.get('password')
        travel1 = request.POST.get('travel1')
        rating1 = request.POST.get('rating1')
        travel2 = request.POST.get('travel2')
        rating2 = request.POST.get('rating2')
        travel3 = request.POST.get('travel3')
        rating3 = request.POST.get('rating3')
        
        print(name, ID, password)
        print(travel1, travel2, travel3)
        print(rating1, rating2, rating3)
        
        return redirect('home')
    return render(request, 'datail.html')

>>>>>>> refs/heads/main
