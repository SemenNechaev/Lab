# Алгоритм  Бойера-Мура
def boyer_moore_search(text, pattern):
    shift_table = {} # таблица сдвига
    for i in range(len(pattern)): # заполнение таблицы сдвига
        shift_table[pattern[i]] = len(pattern) - i - 1
    result_list = [] # список для хранения найденных вложений
    i = len(pattern) - 1
    while i < len(text): # проходимся по тексту и ищем совпадение символов, если символы не совпали, делаем сдвиг согласно таблице сдвигов
        j = len(pattern) - 1
        while text[i] == pattern[j]:
            if j == 0:
                result_list.append(i)
                break
            i -= 1
            j -= 1
        i += max(shift_table.get(text[i], len(pattern)), len(pattern) - j)
    return result_list
# Алгоритм  Рабина-Карпа
def rabin_karp_search(text, pattern):
    n = len(text) # длина текста
    m = len(pattern) # длина искомого слова
    pattern_hash = hash(pattern) # вычисляем хеш для искомого слова
    result_list = []
    for i in range(n - m + 1):
        if hash(text[i:i+m]) == pattern_hash: # вычисляем хеш выделенной подстроки
            if text[i:i+m] == pattern: # сравниваем вычисленный хеш с искомым
                result_list.append(i) # если текущий хеш и искомый совпали, записываем в result
    return result_list
# Алгоритм  Кнута-Морриса-Пратта
def kmp_search(text, pattern):
    lps = [0] * len(pattern) # переменная для хранения префикса\суффикса
    i = 1
    j = 0
    result_list = []
    while i < len(pattern): # проходимся по искомому слову
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j # записываем символ
            i += 1
        else:
            if j != 0: # если есть более короткое совпадение, записываем его
                j = lps[j-1]
            else: # иначе записываем найденное совпадение
                lps[i] = 0
                i += 1
    # после поиска префикса\суффикса используем lps для поиска подстроки
    i = 0
    j = 0
    while i < len(text): # пока строка не закончилась
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern): # если найдена подстрока, записываем индекс вхождения
            result_list.append(i-j)
            j = lps[j-1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0: # проверяем, можно ли взять более короткий префикс\суффикс
                j = lps[j-1] # если можно, делаем это
            else: # если нельзя, переходим к следующей букве
                i += 1
    return result_list
if __name__ == "__main__":
    print("Алгоритм  Бойера-Мура")
    text = "Молодой человек взял их и до того рассердился, что хотел было уже уйти; но тотчас одумался, вспомнив, что идти больше некуда и что он еще и за другим пришел."
    pattern = "что"
    result = boyer_moore_search(text.lower(), pattern)
    print("Исходный текст: " + text + "\nИскомое слово: " + pattern + "\nВхождения: ")
    print(result)

    print("\nАлгоритм  Рабина-Карпа")
    text = "Он охотно давал их читать, никогда не требуя их назад; зато никогда не возвращал хозяину книги, им занятой."
    pattern = "не"
    result = rabin_karp_search(text.lower(), pattern)
    print("Исходный текст: " + text + "\nИскомое слово: " + pattern + "\nВхождения: ")
    print(result)

    print("\nАлгоритм  Кнута-Морриса-Пратта")
    text = "До этой поры он не жил, а лишь существовал, правда очень недурно, но все же возлагая все надежды на будущее."
    pattern = "недурно"
    result = kmp_search(text.lower(), pattern)
    print("Исходный текст: " + text + "\nИскомое слово: " + pattern + "\nВхождения: ")
    print(result)