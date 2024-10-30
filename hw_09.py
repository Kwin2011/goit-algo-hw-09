# Всі алгоритми знаходження мінімальної кількості монет.

coin_values = [50, 25, 10, 5, 2, 1]  # Доступні номінали монет

def calculate_greedy_change(total_amount):
    """
    Обчислює мінімальну кількість монет для вказаної суми за допомогою жадібного алгоритму.
    """
    coins_used = {}
    amount_left = total_amount
    
    for coin in coin_values:
        if amount_left <= 0:
            break
        coins_used[coin] = amount_left // coin
        amount_left %= coin

    return {denomination: count for denomination, count in coins_used.items() if count > 0}


def calculate_dynamic_change(total_amount):
    """
    Обчислює мінімальну кількість монет для вказаної суми за допомогою алгоритму динамічного програмування.
    """
    # Ініціалізація масиву мінімальних монет для кожної суми до total_amount
    min_coins_needed = [0] + [float('inf')] * total_amount

    # Основний цикл обчислення мінімальної кількості монет для кожної суми
    for coin in coin_values:
        for i in range(coin, total_amount + 1):
            if min_coins_needed[i - coin] + 1 < min_coins_needed[i]:
                min_coins_needed[i] = min_coins_needed[i - coin] + 1

    # Відновлення списку монет для оптимального рішення
    coins_used = {}
    remaining_amount = total_amount
    while remaining_amount > 0:
        for coin in coin_values:
            if remaining_amount >= coin and min_coins_needed[remaining_amount] == min_coins_needed[remaining_amount - coin] + 1:
                coins_used[coin] = coins_used.get(coin, 0) + 1
                remaining_amount -= coin
                break

    return coins_used


def compare_algorithms():
    """
    Порівнює результати жадібного алгоритму та динамічного програмування на діапазоні сум.
    """
    matches, mismatches = 0, 0

    for amount in range(1, 1001):
        greedy_solution = calculate_greedy_change(amount)
        dynamic_solution = calculate_dynamic_change(amount)

        if greedy_solution == dynamic_solution:
            matches += 1
        else:
            mismatches += 1

    print("Співпадінь результатів двох алгоритмів у діапазоні 1-1000 коп.:", matches)
    print("НЕспівпадінь результатів у діапазоні 1-1000 коп.:", mismatches)


def main():
    """
    Основна функція, яка приймає суму від користувача і обчислює кількість монет двома методами.
    """
    while True:
        amount = input("Введіть суму в копійках (або 'exit' для виходу): ")

        # Перевірка на вихід
        if amount.lower() == "exit":
            break

        # Перевірка, чи введено число
        try:
            total_amount = int(amount)
        except ValueError:
            print("Неправильне значення. Будь ласка, введіть ціле число.")
            continue

        # Результати жадібного алгоритму
        greedy_result = calculate_greedy_change(total_amount)
        print("Жадібний алгоритм - Кількість монет за номіналами:", greedy_result)

        # Результати динамічного програмування
        dynamic_result = calculate_dynamic_change(total_amount)
        print("Динамічне програмування - Кількість монет за номіналами:", dynamic_result)
        
        # Порівняння результатів
        print("Чи рівні результати:", greedy_result == dynamic_result)
        print()  # Пустий рядок для розділення виводу між тестами


if __name__ == "__main__":
    compare_algorithms()
    main()
