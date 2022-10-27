# Format date from column excel
# Before
![2022-10-27_22-53-31](https://user-images.githubusercontent.com/66513936/198386033-efc04002-8a2e-4919-adde-666b08a3f0b8.png)
# After
![2022-10-27_22-51-38](https://user-images.githubusercontent.com/66513936/198386039-08178064-4797-4812-bd56-13311bf693dc.png)
# Russian
Существует конструктор Bothelp, в нем можно выгружать пользователей
ваших ботов и смотреть данные, которые оставили пользователи
Данные загружаются в формате csv, в колонке, где должна быть дата первого контакта first_contact подгружаются данные,
но они не отформатированы в дату
С помощью программы на python и пакета xlwings, я загрузил колонку first_contact в массив отформатировал его в формат русской даты
Далее было необходимо загрузить данный массив в каждую ячейку колонки "Первый контакт", для этого я воспользовался пакетом xlsxwriter
Итог: Мы видим удобочитаемые даты в колонке "Первый контакт"
Ваш маркетолог скажет вам спасибо

# English

There is a Bothelp constructor, in which you can upload users
of your bots and view the data that users have left
The data is loaded in csv format, in the column where the date of the first contact should be first_contact, the data is loaded,
but they are not formatted to a date
Using a python program and the xlwings package, I loaded the first_contact column into an array and formatted it in the Russian date format
Next, it was necessary to load this array into each cell of the "First Contact" column, for this I used the xlsxwriter package
Bottom line: We see readable dates in the "First contact" column
Your marketer will thank you
