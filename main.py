total_money = 10_000_000
money_for_one = 3_333_333
n = 21
number_of_fields = 5  # номер периода, цена средняя, цена последняя (для закупки и продажи), изменение, капиталзация
number_of_periods = 8  # количество периодов
data = []
period_priceavg_pricelast_dif_cap = [[i] * number_of_fields for i in range(n * number_of_periods)]
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
                        period_priceavg_pricelast_dif_cap[index][1] += float(price.replace(',', '.'))
                        period_priceavg_pricelast_dif_cap[index][3] += float(dif.replace(',', '.'))
                        period_priceavg_pricelast_dif_cap[index][4] += float(cap.replace('\\n', '').replace(',', '.'))
                        if k % 6 == 0:
                            period_priceavg_pricelast_dif_cap[index][0] = index % 8
                            period_priceavg_pricelast_dif_cap[index][1] = round(
                                period_priceavg_pricelast_dif_cap[index][1] / k, 3)
                            period_priceavg_pricelast_dif_cap[index][2] = round(float(price.replace(',', '.')), 3)
                            period_priceavg_pricelast_dif_cap[index][3] = round(
                                period_priceavg_pricelast_dif_cap[index][3] / k, 3)
                            period_priceavg_pricelast_dif_cap[index][4] = round(
                                period_priceavg_pricelast_dif_cap[index][4] / k, 3)
                            k = 0
                            local_data.append(period_priceavg_pricelast_dif_cap[index])
                            index += 1
                        k += 1
                    pair = {str(file).replace('.csv', ''): local_data}
                    data.append(pair)


# def reverse():
#     import csv
#
#     with open("buffer.csv", encoding='utf8') as fr, open("YNDX.csv", "w", encoding='utf8') as fw:
#         cr = csv.reader(fr, delimiter=";")
#         cw = csv.writer(fw, delimiter=";")
#         cw.writerow(next(cr))  # write title as-is
#         cw.writerows(reversed(list(cr)))


def count_evgen_part():
    for i_period in range(number_of_periods):
        sum_cap = 0
        list_caps_comp = []
        list_prices = []
        for i_comp in range(n):
            data_for_period = list(data[i_comp].values())[0][i_period]
            list_prices.append(data_for_period[2])
            list_caps_comp.append(data_for_period[4])
            sum_cap += data_for_period[4]
        sum_cap = round(sum_cap, 3)
        print(f'\n{sum_cap} - summary capitalization in {i_period} period')
        list_caps_comp_percent = []
        for i_comp in range(n):
            list_caps_comp_percent.append(round(list_caps_comp[i_comp] / sum_cap, 3))
            k = int((money_for_one * list_caps_comp_percent[i_comp]) // list_prices[i_comp])
            i = round(list_prices[i_comp] * k, 3)
            number_of_stocks_and_last_price.append((k, round(i, 3)))
            print(f'{number_of_stocks_and_last_price[i_comp]} - numbers of'
                  f' {list(data[i_comp].keys())[0]} stock and price')


if __name__ == '__main__':
    # reverse()

    read_csv_and_fill_data()
    print(data)
    count_evgen_part()
