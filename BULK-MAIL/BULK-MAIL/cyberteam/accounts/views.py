from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
import pandas as pd
import smtplib
from email.mime.text import MIMEText
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #log the user in
            login(request,user)
            return redirect('accounts:email')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def email_view(request):
        if request.method == 'POST':
            dic=[]
            us = request.POST.get('username')
            ps = request.POST.get('password')
            subject = request.POST.get('subj')
            body = request.POST.get('body')
            dic.append(us)
            dic.append(ps)
            dic.append(subject)
            dic.append(body)
            gmail_user = us
            gmail_appPassword = ps

            sent_from = us
            text = body+"  (SENT FROM BULK-MAIL-SENDER, Allinone Cyberteam, https://allinonecyberteam.com/cyberteam.co.in/) "

            msg = MIMEText(text)
            #SenderAddress = us
            #password = ps
            eemail=request.POST.get('mail')
            e = pd.read_excel(eemail)
            emails = e['Emails'].values
            #server = smtplib.SMTP("smtp.gmail.com", 587)
            #server.starttls()
            #server.login(SenderAddress, password)
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(gmail_user, gmail_appPassword)
            for email in emails:
                server.sendmail(sent_from, email, msg.as_string())
            server.quit()
            return render(request,'sent.html',{'dic':dic})
        return render(request,'email.html')

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log the user
            user=form.get_user()
            login(request,user)
            return redirect('accounts:email')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')
        
