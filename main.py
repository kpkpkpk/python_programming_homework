total_money = 10_000_000
money_for_one = 3_333_333
n = 21
number_of_fields = 4  # номер периода, цена, изменение, капиталзация
number_of_periods = 8  # количество периодов
data = []
period_price_dif_cap = [[i] * number_of_fields for i in range(n * number_of_periods)]
number_of_stocks_and_last_price = []


def read_csv_and_fill_data():
    import os
    import re
    root_dir = os.getcwd()
    regex = re.compile('.*csv$')

    for root, dirs, files in os.walk(root_dir):
        index = 0
        for file in files:
            if regex.match(file):
                with open(file, 'r', encoding='utf8') as f:
                    local_data = []
                    k = 1
                    for line in f:
                        if line.__contains__('Дата'):
                            continue
                        _, price, dif, cap = list(line.split(';'))
                        period_price_dif_cap[index][1] += float(price.replace(',', '.'))
                        period_price_dif_cap[index][2] += float(dif.replace(',', '.'))
                        period_price_dif_cap[index][3] += float(cap.replace('\\n', '').replace(',', '.'))
                        if k % 6 == 0:
                            period_price_dif_cap[index][0] = index % 8
                            period_price_dif_cap[index][1] = round(period_price_dif_cap[index][1] / k, 2)
                            period_price_dif_cap[index][2] = round(period_price_dif_cap[index][2] / k, 2)
                            period_price_dif_cap[index][3] = round(period_price_dif_cap[index][3] / k, 2)
                            k = 0
                            local_data.append(period_price_dif_cap[index])
                            index += 1
                        k += 1
                    pair = {str(file).replace('.csv', ''): local_data}
                    data.append(pair)


def reverse():
    import csv

    with open("buffer.csv", encoding='utf8') as fr, open("YNDX.csv", "w", encoding='utf8') as fw:
        cr = csv.reader(fr, delimiter=";")
        cw = csv.writer(fw, delimiter=";")
        cw.writerow(next(cr))  # write title as-is
        cw.writerows(reversed(list(cr)))


def count_evgen_part():
    for i_period in range(number_of_periods):
        sum_cap = 0
        for i_comp in range(n):
            data_for_period = list(data[i_comp].values())[0][i_period]
            sum_cap += data_for_period[3]
        print(f'{round(sum_cap, 2)} - summary capitalization in {i_period} period')


if __name__ == '__main__':
    # reverse()
    read_csv_and_fill_data()
    print(data)
    count_evgen_part()
