from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')     # reunder 은 세개의 인자, 첫번째는 request 고장 인자, 두번째는 템플릿 이름, 세번째는 선택으로 사전형 인자

def about(request):
    return render(request, 'about.html')



def result(request):
    text=request.GET['fulltext']    # 입력받은 글 전체
    words=text.split()  # 공백 기준 나눠서 리스트로 만들어주는 함수
    word_dictionary={}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
                #add to dictionary
                word_dictionary[word]=1
    return render(request, 'result.html',{'full':text, 'total':len(words), 'dictionary':word_dictionary.items()}) # items는 쌍으로 표현
