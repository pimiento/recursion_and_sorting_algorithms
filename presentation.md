- [Что такое рекурсия?](#orgc7dd575)
- [Правильная рекурсия](#org97381e0)
- [Что такое стек вызовов?](#org11aae50)
- [Что такое стек вызовов?](#orgb0ee022)
- [Почему рекурсия это плохо](#org5992215)
- [Recursion depth](#org46d2569)
- [Глубина рекурсии](#org584f271)
- [Почему рекурсия это хорошо](#org03f701c)
- [Вариант задачи для рекурсии](#org5471811)
- [Хвостовая рекурсия](#org1cc4984)
- [Оптимизация хвостовой рекурсии и почему её нет в Python](#orgf56bdef)
- [Пример когда рекурсия помогает](#org7bfc9a0)
- [Дополнительная литература](#org204501c)
- [Зачем нужна сортировка данных](#orga6cd202)
- [Глупая сортировка / сортировка дурака](#org937011b)
- [Пузырьковая сортировка](#orgcfcec38)
- [Сортировка вставками](#org58cd2bc)
- [Сортировка вставками](#org85fed23)
- [Сортировка Шелла](#org5417cf4)
- [Быстрая сортировка](#orgeb9c04d)
- [Быстрая сортировка без рекурсии](#orgafa4332)
- [Сортировка слиянием (Merge Sort)](#orgf75ab38)
- [Параллельный MergeSort](#org6aaf1d7)
- [Сравнение алгоритмов сортировки](#orgfbece3f)
- [Устойчивость сортировки](#org0d83af1)
- [Экзотические сортировки](#org6f32bc6)
- [Дополнительная литература](#org7171f49)
- [Вопросы-ответы](#orgf717ae3)



<a id="orgc7dd575"></a>

# Что такое рекурсия?

Приём в программировании, когда задача может быть разделена на несколько таких же, но проще, задач.  

```python
def pow(x, n):
    # возведение числа в степень это
    # умножение числа на число
    # в степени n-1
    if n == 0:
        return 1
    return x * pow(x, n-1)
```


<a id="org97381e0"></a>

# Правильная рекурсия

```python
def pow(x, n):
    # хорошо бы проверить,
    # что база достижима
    assert n >= 0
    # base case / база рекурсии
    if n == 0:
        return 1
    # recursive case / шаг рекурсии
    return x * pow(x, n-1)
```


<a id="org11aae50"></a>

# Что такое стек вызовов?

```python
def foo(msg):
    print '{} foo'.format(msg)

def main():
    msg = 'hello'
    foo(msg)

if __name__ == '__main__':
    main()
```


<a id="orgb0ee022"></a>

# Что такое стек вызовов?

![img](callstack.png)  


<a id="org5992215"></a>

# Почему рекурсия это плохо

-   стек вызовов растёт вместе с ростом глубины рекурсии
-   можно попасть в бесконечную рекурсию и истратить всю память на стек вызовов


<a id="org46d2569"></a>

# Recursion depth

```python
def inf_counter(x):
    print(x)
    return inf_counter(x+1)
inf_counter(0)
```


<a id="org584f271"></a>

# Глубина рекурсии

```python
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(
    sys.getrecursionlimit() + 234
)
print(sys.getrecursionlimit())
```

    1000
    1234


<a id="org03f701c"></a>

# Почему рекурсия это хорошо

Помогает описать решение задачи понятным языком  

```python
# n! = n * (n-1)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
```

    120


<a id="org5471811"></a>

# Вариант задачи для рекурсии

Попробуйте реализовать решение <span class="underline"><span class="underline">[этой задачи](https://gist.github.com/pimiento/201225ad1a70432060531676dd3e6239)</span></span> без использования рекурсии \Winkey[][green!60!white]  


<a id="org1cc4984"></a>

# Хвостовая рекурсия

Рекурсия, не требующая действий с возвращённым результатом из шага рекурсии.  

```python
def factorial(n, collected=1):
    if n == 0:
        return collected
    return factorial(n-1, collected*n)

print(factorial(5))
```

    120


<a id="orgf56bdef"></a>

# Оптимизация хвостовой рекурсии и почему её нет в Python

-   Интерпретаторы/компиляторы могут оптимизировать хвостовую рекурсию (Tail Call Optimization) и не делать записей в стек вызовов, а подменять переменные в стеке вызовов, таким образом код получится равнозначным обычному циклу
-   <span class="underline"><span class="underline">[Почему TCO нет и не будет в Python](https://neopythonic.blogspot.com/2009/04/final-words-on-tail-calls.html)</span></span>


<a id="org7bfc9a0"></a>

# Пример когда рекурсия помогает

-   **Задача:** У вас есть вложенная структура данных и вы хотите просуммировать значения поля X во всех объектах этой структуры.
-   **Решение задачи:** <https://gist.github.com/pimiento/bc4d5800f66541cb59ea388c1c3c263c>


<a id="org204501c"></a>

# Дополнительная литература

-   <span class="underline"><span class="underline">[SICP](https://web.mit.edu/6.001/6.037/sicp.pdf)</span></span>
-   <span class="underline"><span class="underline">[СИКП](https://raw.githubusercontent.com/alexbakharew/SP/master/%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%20%D0%B8%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BF%D1%80%D0%B5%D1%82%D0%B0%D1%86%D0%B8%D1%8F%20%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D1%85%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC.pdf)</span></span>


<a id="orga6cd202"></a>

# Зачем нужна сортировка данных

-   Можем получить медианное значение  
    
    ![img](median.jpeg)
-   Можем использовать бинарный поиск
-   Проще найти минимум/максимум
-   Множество других применений


<a id="org937011b"></a>

# Глупая сортировка / сортировка дурака

```python
def sort_alg(l):
  while True:
    c = 0
    for i in range(len(l)-1):
      if l[i] > l[i+1]:
        l[i+1],l[i] = l[i],l[i+1]
      else:
        c += 1
    if c == (len(l) - 1): return l

print(sort_alg([1, 3, 2, 0]))
```

    [0, 1, 2, 3]

-   Эффективность **глупой сортировки**: $\mathcal{O}(n^{3})$


<a id="orgcfcec38"></a>

# Пузырьковая сортировка

```python
def sort_alg(l):
    for i in range(len(l)):
        for j in range(len(l[i+1:])):
            if l[j] > l[j+1]:
                l[j], l[j+1] = (
                    l[j+1], l[j]
                )
    return l


print(sort_alg([1, 3, 2, 0]))
```

    [0, 1, 2, 3]

-   Эффективность **пузырьковой сортировки**: $\mathcal{O}(n^{2})$


<a id="org58cd2bc"></a>

# Сортировка вставками

```python
def sort_alg(l):
    for i in range(1, len(l)):
        k = l[i]
        j = i-1
        print(f"i: {i}; k: {k}")
        while j >= 0 and k < l[j]:
            l[j+1] = l[j]
            print(f"l: {l}")
            j -= 1
        l[j+1] = k
        print(f"j: {j}; l: {l}")

d = [12, 11, 13, 5, 6]
```


<a id="org85fed23"></a>

# Сортировка вставками

-   Эффективность **сортировки вставками**: $\mathcal{O}(n^{2})$

**Но!** Эта сортировка эффективна если у вас уже частично отсортированные данные, так как пропускается этап перестановки данных.  

-   <span class="underline"><span class="underline">[Дополнительно почитать](https://habr.com/ru/post/415935/)</span></span>


<a id="org5417cf4"></a>

# Сортировка Шелла

-   <span class="underline"><span class="underline">[Код](https://ru.wikibooks.org/wiki/%25D0%259F%25D1%2580%25D0%25B8%25D0%25BC%25D0%25B5%25D1%2580%25D1%258B_%25D1%2580%25D0%25B5%25D0%25B0%25D0%25BB%25D0%25B8%25D0%25B7%25D0%25B0%25D1%2586%25D0%25B8%25D0%25B8_%25D1%2581%25D0%25BE%25D1%2580%25D1%2582%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25BA%25D0%25B8_%25D0%25A8%25D0%25B5%25D0%25BB%25D0%25BB%25D0%25B0#Python)</span></span>
-   на практике получается скорость работы быстрее $\mathcal{O}(n^{2})$ но нет математических описаний как выбор последовательности дистанций влияет на алгоритмическую сложность.


<a id="orgeb9c04d"></a>

# Быстрая сортировка

```python


def sort_alg(L):
    if L:
        return (
            sort_alg(
        [e for e in L[1:] if e < L[0]]
            ) +
            L[0:1] +
            sort_alg(
        [e for e in L[1:] if e >= L[0]]
            )
        )
    return []


```


<a id="orgafa4332"></a>

# Быстрая сортировка без рекурсии

    % ./quicksort.py 16K
      2 вызовов для 16K данных: лучший результат равен 20.75
    % ./quicksort.py 32K
      2 вызовов для 32K данных: лучший результат равен 78.98


<a id="orgf75ab38"></a>

# Сортировка слиянием (Merge Sort)

-   <span class="underline"><span class="underline">[Код](https://gist.github.com/pimiento/72ea7cc917e1e732f834e307f6998d89)</span></span>
-   <span class="underline"><span class="underline">[мультик](https://www.youtube.com/watch?v=JSceec-wEyw)</span></span>

Сортировка слиянием позволяет нам распараллелить процесс сортировки. Это очень эффективно на больших данных и широко используется в алгоритмах map/reduce.  


<a id="org6aaf1d7"></a>

# Параллельный MergeSort


<a id="orgfbece3f"></a>

# Сравнение алгоритмов сортировки

![img](sorting_algorithms.png)  


<a id="org0d83af1"></a>

# Устойчивость сортировки

```python
records = [
   (("A", "X"), ("B", 1)),
   (("A", "Y"), ("B", 1)),
   (("A", "X"), ("B", 2)),
]
records.sort(key=lambda x: x[0][1])
for r in records:
    print(f"{r[0][1]}, {r[1][1]}")
```

    X, 1
    X, 2
    Y, 1


<a id="org6f32bc6"></a>

# Экзотические сортировки

-   <span class="underline"><span class="underline">[Тыц](https://habr.com/ru/post/161835/)</span></span>
-   <span class="underline"><span class="underline">[Тыц](http://algolab.valemak.com/schrodinger)</span></span>


<a id="org7171f49"></a>

# Дополнительная литература

-   [Пузырьковая сортировка и её улучшения](https://habr.com/ru/post/204600/)
-   [Сравнение алгоритмов](https://habr.com/ru/post/133996/)
-   Т.Кормен, Ч.Лейзерсон, Р.Ривест, К.Штайн «Алгоритмы. Построение и анализ.»


<a id="orgf717ae3"></a>

# Вопросы-ответы

![img](questions.jpg)
