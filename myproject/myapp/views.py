from django.shortcuts import render

# ลบ HttpResponse ออก แล้วเปลี่ยนมาใช้ render ทั้งหมด

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    # ฟังก์ชัน contact จาก Assignment 7
    student_info = "6xxxxxxxxx นายสมชาย ใจดี" 
    return render(request, 'contact.html', {'info': student_info}) # หรือใช้ HttpResponse แบบเดิมถ้าอาจารย์ไม่ได้สั่งแก้

def form(request):
    return render(request, 'form.html')