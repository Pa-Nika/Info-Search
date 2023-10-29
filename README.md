# Info-Search
## Python

* Напишите программу, которая запрашивает у пользователя число n, а затем выводит n первых строк треугольника Паскаля. Обеспечьте отказоустойчивость при введении пользователем не валидного значения n (т.е. не целого положительного числа)
* Напишите программу, которая принимает на вход(из файла либо из консоли) скобочную последовательность, а результатом работы которой является ответ, является ли данная скобочная последовательность правильной.
Пример:
"(()())()" - Правильная последовательность
"(()))" - Неправильная последовательность
")())(" - Неправильная последовательность
* Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом, находящимся на некотором постоянном числе позиций левее или правее него в алфавите. Напишите программу, которая реализует шифрование Цезаря. Входные данные: путь до изначального файла с текстом, требуемый сдвиг и язык текста(на выбор английский либо русский). Результат работы - новый файл с зашифрованным текстом.

## Django
Разработайте приложение, которое бы работало с базой данных(например MySQL) и предоставляло полный CRUD(создание, чтение, модификация, удаления) доступ к следующим сущностям:

**Университет**
* Полное название
* Сокращенное название
* Дата создания
  
**Студент**
* ФИО
* Дата рождения
* Университет(только из списка университетов, содержащихся в базе)
* Год поступления
 
Доступ должен предоставляться как через панель администратора, так и через созданные вами страницы(по типу тех страниц, которые описаны в разделах Формы и Модели).

## Flask
Разработайте приложение аналогично заданию по Django. Вместо работы с панелью администрирования создайте ограничения на возможность выполнять операции Create и Update только зарегистрированным пользователям.
