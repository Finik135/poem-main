def apply_theme(user, theme_name):
    """
    Застосовує тему до користувача і зберігає її.
    Тестова зміна.
    """
    if user.is_authenticated:
        user.theme = theme_name
        user.save()

