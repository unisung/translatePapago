import json

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse
import os
import sys
import urllib.request

def index(request):
    response = HttpResponse()
    response.write("<h1>Welcome</h1>")
    response.write("<p>This is my first Django. </p>")
    return response


def index_redirect(request):
    return HttpResponseRedirect('http://google.com')


def index_json(request):
    return JsonResponse({'key': 'value'})


def index_file(request):
    img = open('./images/IU_MelOn_Music_Awards_2017_06.jpg', 'rb')
    response = FileResponse(img)
    return response

def index_trans_result(request):
    paramText=request.GET.get('text', None)
    print('paramText:',paramText)
    # 네이버 Papago NMT API 예제
    client_id = 'lHIsFThpxgc9n9VxVeXt'
    client_secret = 'qua9SSHWRO'
    encText = urllib.parse.quote(paramText)
    data = "source=ko&target=en&text=" + encText
    print(data)
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    print('response:', response)
    rescode = response.getcode()
    result=''
    if (rescode == 200):
        response_body = response.read()
        decode = json.loads(response_body.decode('utf-8'))
        # print('decode:',decode)
        # result = decode['message']['result']['translatedText']
        # print('result:',result)
        return JsonResponse(decode)
    else:
        print("Error Code:" + rescode)

    return result

def index_trans(request):
    response = HttpResponse()
    response.write('<!DOCTYPE html>')
    response.write('<html lang="en">')
    response.write('<head>')
    response.write('<meta charset="UTF-8">')
    response.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    response.write('<meta name="referrer" content="no-referrer">')
    response.write('<title>Document</title>')
    response.write('</head>')
    response.write('<body>')
    response.write('<input type="text" id="msg" placeholder="원본 텍스트를 입력하기"> ')
    response.write('<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>')
    response.write('<button id="translateText">번역하기</button>')
    response.write('<div id="translated-text-container"></div>')
    response.write('<script>')
    response.write('const   button2 = document.getElementById("translateText");')
    response.write('const  translateUrl = "http://127.0.0.1:8000/translate0/trans_result"; ')
    response.write('const  gettranslateText = function(){    ')
    response.write(' var  originalText = document.getElementById("msg").value; ')
    response.write('axios.get(translateUrl, { ')
    response.write(' params: { ')
    response.write('source: "ko",target: "en", text: originalText  } ')
    response.write('}).then((response) => {  ')
    response.write('    var  translation = JSON.stringify(response);  console.log("translation:",translation);')
    response.write('    var  translationTT = JSON.parse(translation); console.log("translationTT:",translationTT.data.message.result.translatedText);')
    response.write('    var translatedTextContainer = document.getElementById("translated-text-container"); ')
    response.write('translatedTextContainer.textContent = translationTT.data.message.result.translatedText; ')
    response.write('}).catch(function(error) ')
    response.write('{ ')
    response.write('    console.log("Error:", error); ')
    response.write('}); ')
    response.write('} \n')
    response.write('const   translateButton = document.getElementById("translateText"); ')
    response.write('translateButton.addEventListener("click", gettranslateText); ' )
    response.write('</script>')
    return response
