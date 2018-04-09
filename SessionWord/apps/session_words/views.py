from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
	return render(request, "session_words/index.html")
# Create your views here.
def process(request):
	if 'listofWord' not in request.session:
		request.session['listofWord'] = []
	if request.method == 'POST':
		comment = request.POST['comment']
		color = ''
		if 'color' in request.POST:
			color = request.POST['color']
		setFontTo = ''
		if 'bigFont' in request.POST: 
			setFontTo = 'bold'
		time = strftime("%Y-%m-%d %H:%M %p", gmtime())
		allWords = {
				'color': color,
				'comment': comment,
				'font': setFontTo,
				'time': time

		}

		request.session['listofWord'].append(allWords)
		request.session.modified= True
		return redirect('/add_word')
def add_word(request):
	print request.session['listofWord']		
	return render(request, 'session_words/index.html')

def clear(request):
	request.session.clear()		
	return redirect('/')


		# request.session['name'] = request.POST['name']
		# if request.POST['red'] :
		# 	request.session['color'] = request.POST['red']

		# if request.POST['green'] :
		# 	request.session['color'] = request.POST['green']

		# if request.POST['blue'] :
		# 	request.session['blue'] = request.POST['blue']

		# request.session['checkbox'] = request.POST['checkbox']

		# request.session['submit'] = request.POST['submit']

		

	