DATA BASE - POSTGRES 
---
MAIN - Основной файл запуска
---
JSONER - Файл для работы с JSON
---
Data_base - Файл с функциями БД
---

Запускается через файл main.py

1)Cоздаётся файл со строкой внутри _**def file_with_json**_

2)Строка из файла преобразуется в JSON def **_json_file_reader_**

3)Создается база данных с таблицами **_data_base_creating()_**

4)JSON из файла проходит валидацию **_def validator_**

5)Запрос разбивается на элементы 

6)Элементы вставляются в БД
