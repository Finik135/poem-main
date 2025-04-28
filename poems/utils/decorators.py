from django.shortcuts import redirect
from functools import wraps

def require_account_type(*allowed_types):
    """
    Декоратор, який дозволяє доступ лише користувачам з певним типом акаунта.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')  # або твоя сторінка входу
            if request.user.account_type not in allowed_types:
                return redirect('upgrade')  # або твоя сторінка апгрейду
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

# коротші версії
require_free = require_account_type('free')
require_pro = require_account_type('pro')
require_premium = require_account_type('premium')
