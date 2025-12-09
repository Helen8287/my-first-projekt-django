from django.http import HttpResponse

def home_view(request):
    # Здесь добавим ссылки на другие страницы:
    return HttpResponse("""
        <h1>Главная страница</h1>
        <p>
            <a href="/data/">Перейти на страницу Data</a><br>
            <a href="/test/">Перейти на страницу Test</a>
        </p>
    """)

def data_view(request):
    return HttpResponse("""
        <h1>Страница Data</h1>
        <a href="/">Вернуться на главную</a>
    """)

def test_view(request):
    return HttpResponse("""
        <h1>Страница Test</h1>
        <a href="/">Вернуться на главную</a>
    """)
