from django.shortcuts import redirect


def login_required(f):
    def wrapper(*args):
        if hasattr(args[0], 'error') and args[0].error == 403:
            return redirect('login')
        return f(*args)
    return wrapper