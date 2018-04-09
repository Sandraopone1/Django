from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, "survey_form/index.html")

def process(request):
	if request.method == 'POST':
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
		
	
	return redirect('/result')
def result(request):
		
	 	request.session['name'] 
		request.session['location'] 
		request.session['language'] 
		request.session['comment'] 
		
	
		return render(request, "survey_form/result.html")

def reset(request):
		return redirect("/")
	# def create(request):
	# if request.method == "POST":
	# 	print "*"*50
	# 	print request.POST
 #        print request.POST['name']
 #        print request.POST['desc']
 #        request.session['name'] = "test"  # more on session below
	# 	print "*"*50
	# 	return redirect("/")
	# else:
	# 	return redirect("/")
