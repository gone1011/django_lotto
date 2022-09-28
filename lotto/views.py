from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all() # DB에 저장된 GuessNumbers 객체 모두를 가져온다.
    # 브라우저로부터 넘어온 request를 그대로 template('default.html')에게 전달
    # {} 에는 추가로 함께 전달하려는 object들을 dict로 넣어줄 수 있음
    return render(request, 'lotto/default.html', {'lottos':lottos}) # context-dict


def post(request):
    if request.method == "POST":
        # print(request.POST) # 주석을 풀면 새로운 로또 번호 생성 후 cmd에서 이 값을 확인할 수 있음
        # print(request.method) # 주석을 풀면 새로운 로또 번호 생성 후 cmd에서 이 값을 확인할 수 있음
        # 사용자로부터 넘겨져 온 POST 요청 데이터를 담아 PostForm 객체 생성
        form = PostForm(request.POST) # filled form
        # print(type(form)) # <class 'lotto.forms.PostForm'>
        # print(form)
        if form.is_valid():
	    # 사용자로부터 입력받은 form 데이터에서 추가로 수정해주려는 사항이 있을 경우 save를 보류함
            lotto = form.save(commit = False) # 최종 DB 저장은 아래 generate 함수 내부의 .save()로 처리
            print(type(lotto)) # <class 'lotto.models.GuessNumbers'>
            print(lotto)
            lotto.generate()
            return redirect('index') # urls.py의 name='index'에 해당
            # -> 상단 from django.shortcuts import render, redirect 수정
    else:
        form = PostForm() # empty form
        return render(request, "lotto/form.html", {"form": form})


def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey) # primary key
    return render(request, "lotto/detail.html", {"lotto": lotto})

    # index.html
    # <input type='text'. name='name'></input>
    # <input type='text'. name='text'></input>
    # USER가 값을 입력하고, 전송 버튼을 클릭 -> USER가 입력한 값을 가지고 HTTP POST request
    # user_input_name = request.POST['name'] # HTML에서 name이 'name'인 input tag에 대해 UESR가 입력한 값
    # user_input_name = request.POST['text'] # HTML에서 name이 'text'인 input tag에 대해 UESR가 입력한 값
    # new_row = GuessNumbers(name=uwer_input_name, text=user_input_text)
    # print(new_row.num_lotto) # 5
    # print(new_row.name) # 'win the prize!'
    # new_row.name = new_row.name.upper() # 'WiN THE PRIZE!'
    # new_row.generate() # 아니면 아래 save쓰던가
    # new_row.lottos = [ np.randint(1, 50) for i in range(6) ]
    # new_row.save()
