from django.shortcuts import render


# def home(request):
#    return render(request, 'home.html')

# def lower(request):
#    user_text = request.GET['usertext'] #созд пер user_text и получаем GET запрос по ключу usertext
#    words = user_text.split() #получаем список слов в этой переменной
#    number_of_words = len(words)
#    total_characters = len(user_text)
#    lower_case_text = user_text.lower()
#    return render(request, 'lower.html', {'usertext':user_text, 'reversedtext':lower_case_text, 'number_of_words':number_of_words, 'total_characters':total_characters })


# def reverse(request):
#    user_text2 = request.GET['usertext'] #созд пер user_text и получаем GET запрос по ключу usertext
#    words2 = user_text2.split() #получаем список слов в этой переменной
#    number_of_words2 = len(words2)
#    reversed_text2 = user_text2[::-1] #делаем распечатку наоборот
#    return render(request, 'reverse.html', {'usertext2':user_text2, 'reversedtext2':reversed_text2, 'number_of_words2':number_of_words2})


# def upper(request):
#     user_text = request.GET.get('usertext', '')  # Получаем текст из GET запроса или пустую строку, если нет текста
#     words3 = user_text.split()  # Получаем список слов в этой переменной
#     number_of_words3 = len(words3)
#     total_characters3 = len(user_text)
#     upper_case_text = user_text.upper()  # Переводим текст в верхний регистр
#     return render(request, 'upper.html', {'usertext': user_text, 'uppercasetext': upper_case_text, 'number_of_words': number_of_words3, 'total_characters': total_characters3})



#добавил



def lower(request, user_text=None):
    if user_text is None:
        user_text = request.GET['usertext']
    words = user_text.split()
    number_of_words = len(words)
    total_characters = len(user_text)
    lower_case_text = user_text.lower()
    return render(request, 'lower.html', {'usertext': user_text, 'reversedtext': lower_case_text, 'number_of_words': number_of_words, 'total_characters': total_characters })


def reverse(request, user_text=None):
    if user_text is None:
        user_text = request.GET['usertext']
    words2 = user_text.split()
    number_of_words2 = len(words2)
    reversed_text2 = user_text[::-1]
    return render(request, 'reverse.html', {'usertext2': user_text, 'reversedtext2': reversed_text2, 'number_of_words2': number_of_words2})


def upper(request, user_text=None):
    if user_text is None:
        user_text = request.GET.get('usertext', '')  
    words3 = user_text.split()  
    number_of_words3 = len(words3)
    total_characters3 = len(user_text)
    upper_case_text = user_text.upper()  
    return render(request, 'upper.html', {'usertext': user_text, 'uppercasetext': upper_case_text, 'number_of_words': number_of_words3, 'total_characters': total_characters3})


# Представление для домашней страницы
def home(request):
    # Если метод запроса GET, обрабатываем запрос
    if request.method == 'GET':
        # Получаем операцию и текст из GET запроса
        operation = request.GET.get('operation', None)
        user_text = request.GET.get('usertext', '')
        # В зависимости от выбранной операции вызываем соответствующее представление
        if operation == 'lower':
            return lower(request, user_text)
        elif operation == 'reverse':
            return reverse(request, user_text)
        elif operation == 'upper':
            return upper(request, user_text)
    # Возвращаем домашнюю страницу
    return render(request, 'home.html')






