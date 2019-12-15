from django.contrib import admin
from .models import Form

admin.site.register(Form)
"""
↑登録するメソッドで、ここにモデルクラスを指定すれば、そのクラスが管理ツールで編集できるようになる
"""
