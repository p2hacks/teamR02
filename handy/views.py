from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import HelloForm
from .models import Form
from django.shortcuts import redirect
from .forms import HelloForm

#class クラス名(forms.Form):
#変数＝フィールド
#変数=フィールド
#.....略....

class HelloView(TemplateView): #ホーム画面
    def get(self, request):
        #GETアクセスの際に実行される処理
        return render (request, 'handy/index.html')
        
    def post(self, request):#入力後の画面表示
        #チェックの時はここでif文にして検索がかかんないようにする？？？
        if('check' in request.POST):
            self.params['result']=' Checked...'#登録ありがとうございました。
        else:
            self.params['result'] = 'not checked...'#ご利用規約に同意お願いします
          #  self.params['from'] = HelloForm(request.POST)
        return render(request, 'handy/index.html', self.params)

#create model
def user_form(request):
    if(request.method == 'POST'):
        ins=Form()
        info=HelloForm(request.POST, instance=ins)
        info.save()
        return redirect(to='/handy')
    params = {
        'title': 'ユーザー登録',
        'form':HelloForm(),
     }
    return render(request, 'handy/form.html', params)

def cristmas(request):
    return render(request, 'handy/kurisumasu.html')

class Dbg(TemplateView):
    def get(self,request):
        all=Form.objects.all()
        params={
            'dish':all
        }
        
            
        return render(request,'handy/database.html',params)

def syuto(request):
    return render(request, 'handy/syuto-renn.html')
def mito(request):
    return render(request, 'handy/mi-toro-fu.html')
def bihu(request):
    return render(request, 'handy/bi-fusityu-.html')

def freezer(request):
    return render(request,'handy/doraggu.html')

def refree(request):
    return render(request,'handy/reizouko.html')
def refrze(request):
    return render(request,'handy/reitouko.html')
#params変数を用意した後、if分でPOSTを送信されたかチェック
#POST送信の場合は、レコードの保存の処理を行っている
#上の値をもとにFormインスタンスを生成
