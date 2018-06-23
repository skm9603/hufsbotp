from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import datetime
import time
import json
import re
from . import checkBuildingNum
from . import checkWeather
from . import hakAndDiliv
from .weatherResult import Weather
from . import checkAll
# from .weatherOther import Weather

def keyboard(request):
    return JsonResponse({
        "type": "text",
        "message" : {
          'text' : '안녕하세요'
        },
    })


@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
    # start_time = time.time()
    # today = datetime.date.today()
    # today_date = today.strftime('%m월 %d일')

    checkHD = hakAndDiliv.Checking()
    haksik_dilivery = checkHD.hnd(datacontent)

    if "umon" in haksik_dilivery:
        reply = "어문관 건물 번호&위치에 대해서 알고싶으시면 '어문관 위치'를\n"
        reply = reply + "학식에 대해서 알고싶으시면 '어식'을 입력하세요!"
        return JsonResponse({
            'message': {
                'text': reply
            },
            'keyboard': {
                'type': 'text',
            }

        })
    elif haksik_dilivery is not "empty" and haksik_dilivery is not "building":
        return JsonResponse({
            'message': {
                'text': haksik_dilivery
            },
            'keyboard': {
                'type': 'text',
            }

        })

    checkDP = checkAll.checkAll()
    result = checkDP.checkPhoneNumber(datacontent)
    if result == None:
        result = checkDP.checkCalendar(datacontent)

    if result != None:
        return JsonResponse({
            'message': {
                'text': result
            }
        })

    checkB = checkBuildingNum.CheckBuilding()
    building_num = checkB.building_check(datacontent)

    if "checkBuilding" in building_num:    # 이미지 삽입하기.

        build = "어떤 건물(호실)번호 혹은 건물 위치를 알고 싶으신가요?"
        build = build + "\n\n*호실번호 입력시 호실 숫자 이외의 숫자는 입력하지 말아 주세요."
        build = build + "\n\n*호실번호 입력시 중간의 '-' 는 꼭! 입력해 주셔야 합니다!"

        return JsonResponse({
            'message': {
                'text': build
            },
            'keyboard': {
                'type': 'text',
            }

        })
    elif building_num is not "empty":
        if building_num == 'error':
            reply = "*호실번호 입력 오류입니다. 호실번호 이외의 수는 입력하지 말아주세요!"
            reply = reply + "\n\n*호실번호 입력시 중간의 '-' 는 꼭! 입력해 주셔야 합니다!"
            reply = reply + "\n\n어떤 건물(호실)번호 혹은 건물 위치를 알고 싶으신가요?"
            return JsonResponse({
                'message': {
                    'text': reply
                },
                'keyboard': {
                    'type': 'text',
                }

            })
        else:
            num = re.sub('[^0-9]', '', building_num)
            return JsonResponse({
                'message': {
                    'photo': {
                        'url': checkBuildingNum.pictureUrl[int(num[0])],
                        'width': 616,
                        'height': 382
                    },
                    'text': building_num,  # info 가 들어있음
                },
                'keyboard': {
                    'type': 'text',
                }
            })

    checkW = checkWeather.CheckW()
    weather = checkW.checkQuesiton(datacontent)
    if weather is not 'empty':
        if weather is 'tomorrow':
            tomorrow = '오늘 이외의 날씨는 지원하지 않습니다 ㅠㅠ 다음 URL을 통해 검색해주세요!\n\n'
            tomorrow = tomorrow + 'https://search.naver.com/search.naver?where=nexearch&query=%EC%9A%A9%EC%9D%B8+%EB%AA%A8%ED%98%84+%EB%82%A0%EC%94%A8&ie=utf8&sm=tab_she&qdt=0'
            return JsonResponse({
                'message': {
                    'text': tomorrow,  # 날씨 정보
                },
            })
        else:
            return JsonResponse({
                'message': {
                    'text': weather,  # 날씨 정보
                },
            })


    print = "채팅봇의 기능은 다음 아래와 같습니다."
    print = print + "\n1. 학식\n2. 배달음식\n3. 학사일정\n4. 학교기관 전화번호\n5. 건물 위치 및 번호\n6. 모현 날씨"
    print = print + "\n\n다음 기능들에 대하여 질문해 주세요 ㅠㅠ"
    return JsonResponse({
        'message': {
            'text': print,  # 날씨 정보
        },
    })
