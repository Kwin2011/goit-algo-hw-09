# Домашнє завдання: Розрахунок оптимальної кількості монет для видачі решти

## Опис

Це завдання демонструє підхід до видачі решти покупцю за допомогою двох різних алгоритмів — жадібного алгоритму та методу динамічного програмування. Обидва алгоритми спрямовані на мінімізацію кількості монет, необхідних для видачі заданої суми, з різними підходами до досягнення оптимального результату.

### Завдання

1. **Жадібний алгоритм** (`find_coins_greedy`):  
   - Алгоритм вибирає монети з найбільшим номіналом, доступним для поточної залишкової суми, доки вся сума не буде покрита.
   - Цей підхід дає швидкий результат, але не завжди забезпечує мінімальну кількість монет для кожного набору номіналів.
   
2. **Алгоритм динамічного програмування** (`find_min_coins`):  
   - Метод, який використовує динамічне програмування, щоб знайти мінімальну кількість монет для кожної проміжної суми від 0 до заданої суми.
   - Гарантує оптимальне рішення з мінімальною кількістю монет для будь-якого набору номіналів.

## Порівняння ефективності

### Швидкодія (О велике)

- **Жадібний алгоритм**: 
  - Має часову складність \(O(n)\), де \(n\) — кількість монетних номіналів.
  - Для кожної залишкової суми обирається монета найбільшого номіналу, тому жадібний алгоритм працює за лінійний час, незалежно від самої суми.
  - Підходить для застосування в касових системах, коли номінали монет задовольняють умови оптимальності жадібного алгоритму (наприклад, коли кожний більший номінал кратний попереднім).

- **Метод динамічного програмування**:
  - Часова складність цього алгоритму становить \(O(m \times n)\), де \(m\) — сума, а \(n\) — кількість номіналів.
  - Виконує більше обчислень, оскільки обробляє кожну проміжну суму до заданого значення, забезпечуючи оптимальне розбиття.
  - Підходить для випадків, коли потрібно забезпечити мінімальну кількість монет за будь-яких умов (наприклад, коли номінали не кратні один одному).

### Продуктивність при великих сумах

1. **Жадібний алгоритм**:
   - Виконується швидше, особливо для великих сум, оскільки потребує лише одного проходу по списку номіналів.
   - Однак для наборів монет, які не задовольняють умови оптимальності, може дати неоптимальну кількість монет.
   
2. **Динамічне програмування**:
   - Забезпечує мінімальну кількість монет незалежно від складності набору номіналів.
   - Проте обчислення можуть стати значно більш витратними при великих значеннях суми, через що алгоритм менш ефективний у реальному часі.

### Підсумок

- **Жадібний алгоритм** є оптимальним для касових систем, де важливо виконати обчислення швидко, і для випадків, коли набір номіналів дозволяє отримати оптимальне розв’язання. Він менш витратний за часом, але не гарантує мінімальну кількість монет для кожного можливого набору.
- **Динамічне програмування** забезпечує мінімальну кількість монет у всіх випадках, тому є кращим вибором для універсальних касових систем або для випадків із нестандартними номіналами монет, хоча вимагає більших обчислювальних ресурсів.
