from django.shortcuts import redirect


def is_user(function):
	def wrap(request, *args, **kwargs):
		if 'userauth' not in request.session:
			return redirect('login')
		else:
			return function(request, *args, **kwargs)
		
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap