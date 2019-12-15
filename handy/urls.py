# -*- coding: utf-8 -*-

#フォーラムの処理１form.py→2view.py→3templateのhandyのhome.html→4handyのurl.py

from django.urls import path
#from django.conf.urls import path
from . import views
from .views import HelloView,Dbg
#,HelloForm


urlpatterns = [
        
       path('HelloView',HelloView.as_view(), name = 'HelloView'),
       path('',HelloView.as_view(),name='home'),
       path('form',views.user_form,name='user_forms'),
       path('cristmas',views.cristmas,name='Crist'),
       path('db',Dbg.as_view(),name='Dbg'),
       path('bi-fusityu-.html',views.bihu,name='bi'),
       path('syuto-renn.html',views.syuto,name='syuto'),
       path('mi-toro-fu.html',views.mito,name='mi'),
       path('ドラッグ.html',views.freezer,name='drug'),
       path('reizouko.html',views.refree,name='rei'),
       path('reitouko.html',views.refrze,name='res'),


 ]