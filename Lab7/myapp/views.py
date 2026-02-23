from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>หน้าแรกของเว็บไซต์วิชา ICT12367</h1>")

def about(request):
    return HttpResponse("<h1>เกี่ยวกับเรา</h1>")

# ข้อ 1: หน้าติดต่อ
def contact(request):
    # ใส่รหัสนักศึกษาและชื่อของคุณตรงนี้
    return HttpResponse("<h1>ติดต่อ: 68103144 นายชินภัทร บุญยศ</h1>")

# ข้อ 2: หน้าแบบฟอร์ม (ใช้ render)
def form(request):
    return render(request, 'form.html')