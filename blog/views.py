from django.shortcuts import render

# Create your views here.
posts = [

	{
		'author': 'Dr. Swapnil Jain',
		'title': 'post 1',
		'content': 'about pandemic',
		'date': 'first July'	
	
	},

	{
		'author': 'Dr. Swap Jain',
		'title': 'post 2',
		'content': 'about covid',
		'date': 'second July'
		
	}
]



def home(request):
	context = {
			'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})







