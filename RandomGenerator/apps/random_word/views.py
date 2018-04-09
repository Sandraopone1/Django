from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):
	count = request.session.get('count', 0)
	unique_word = get_random_string(length=14)
	request.session['count'] = count + 1
	context ={
			"generator": unique_word,
			"counter": count
		}
	return render(request, "random_word/index.html", context)
def create(request):

	if request.method == "POST":
		return redirect("/")
def reset(request):
		del request.session['count']
		return redirect("/")
# 		count = request.session.get('count', 0)
# 		unique_word = get_random_string(length=14)
		
#     	return render(request, "random_word/index.html", context)
#     	return redirect("/")
	# else:
	# 	return redirect("/")
# Create your views here.
