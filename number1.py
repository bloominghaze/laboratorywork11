import csv

def read_csv_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
            return data
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено. Перевірте шлях до файлу.")
    except IOError:
        print(f"Помилка під час відкриття файлу {file_path}.")
    return []

def write_csv_file(file_path, data):
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"Результати успішно записані у файл {file_path}")
    except IOError:
        print(f"Помилка під час запису у файл {file_path}.")

def search_in_range(data, start_year, end_year):
    result = []
    year_index_map = {int(data[0][i]): i for i in range(4, len(data[0]))}
    for row in data:
        if row[0] == "Ukraine":
            for year in range(start_year, end_year + 1):
                if year in year_index_map:
                    index = year_index_map[year]
                    result.append([year, row[index]])
    return result

def main():
    input_file = 'Ukraine_GDP_Life_expectancy.csv'

    data = read_csv_file(input_file)
    if data:
        print("Вміст файлу:")
        for row in data:
            print(row)

        while True:
            try:
                start_year = int(input("Введіть початковий рік (наприклад, 1991): "))
                end_year = int(input("Введіть кінцевий рік (наприклад, 2019): "))

                if start_year > end_year:
                    print("Початковий рік не може бути більшим за кінцевий рік. Спробуйте знову.")
                    continue

                available_years = {int(data[0][i]) for i in range(4, len(data[0]))}
                if start_year < min(available_years) or end_year > max(available_years):
                    print(f"Будь ласка, введіть роки в межах {min(available_years)} - {max(available_years)}.")
                    continue

                break

            except ValueError:
                print("Некоректний формат року. Спробуйте знову.")
                continue

        search_result = search_in_range(data, start_year, end_year)

        if search_result:
            print("\nРезультат пошуку:")
            print(f"{'Рік':<10} {'Очікувана тривалість життя (роки)':<35}")
            print("=" * 45)
            for year, life_expectancy in search_result:
                print(f"{year:<10} {life_expectancy:<35}")
            output_file = 'search_results.csv'
            write_csv_file(output_file, search_result)
        else:
            print(f"Дані за період {start_year}-{end_year} не знайдено.")
    else:
        print("Не вдалося прочитати вміст файлу.")

if __name__ == "__main__":
    main()
