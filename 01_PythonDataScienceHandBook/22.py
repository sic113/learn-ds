# coding: utf-8
help(len)
get_ipython().run_line_magic('pinfo', 'len')
L = [1,2,3]
get_ipython().run_line_magic('pinfo', 'L.insert')
get_ipython().run_line_magic('pinfo', 'L')
def square(a):
    """Возвращает значение a^2"""
    return a ** 2
get_ipython().run_line_magic('pinfo', 'square')
get_ipython().run_line_magic('pinfo2', 'square')
get_ipython().run_line_magic('pinfo2', 'len')
get_ipython().run_line_magic('psearch', '*Warning')
get_ipython().run_line_magic('psearch', 'str.*find*')
import pandas as pd
pd.DataFrame({
     'Комбинация клавиш': ['Ctrl+A', 'Ctrl+E', 'Ctrl+B (или стрелка влево)', 'Ctrl+F (или стрелка вправо)'],
     'Действие': ['Перемещает курсор в начало строки', 'Перемещает курсор в конец строки', 'Перемещает курсор назад на 1 символ', 'Перемещает курсор вперед на 1 символ']
})
pd.DataFrame({
     'Комбинация клавиш': ['BackSpace', 'Ctrl+D', 'Ctrl+K', 'Ctrl+U', 'Ctrl+Y', 'Ctrl+T'],
     'Действие': ['Удаляет предыдущий символ в строке', 'Удаляет следующий символ в строке', 'Вырезает текст от курсора и до конца строки',
                  'Вырезает текст с начала строки до курсора','Вставляет предварительно вырезанный текст','Меняет местами предыдущие два символа']
})
pd.DataFrame({
     'Комбинация клавиш': ['Ctrl+P', 'Ctrl+N (или стрелка вверх)', 'Ctrl+R (или стрелка вниз)'],
     'Действие': ['Доступ к предыдущей команде в истории', 'Доступ к следующей команде в истории', 'Поиск в обратном направлении по истории команд']
})
pd.DataFrame({
     'Комбинация клавиш': ['Ctrl+L', 'Ctrl+N (или стрелка вниз)', 'Ctrl+D'],
     'Действие': ['Очистить экран терминала', 'Прервать выполнение текущей команды Python', 'Выйти из сеанса IPython']
})
get_ipython().run_line_magic('run', 'myscript.py')
get_ipython().run_line_magic('timeit', 'L = [n ** 2 for n in range(1000)]')
get_ipython().run_cell_magic('timeit', '', 'L = []\nfor n in range(1000):\n    L.append(n ** 2)\n')
get_ipython().run_line_magic('pinfo', '%timeit')
get_ipython().run_line_magic('lsmagic', '')
get_ipython().run_line_magic('rerun', '21')
