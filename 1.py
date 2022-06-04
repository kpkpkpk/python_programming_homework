import gspread
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
from math import sqrt

if __name__ == '__main__':
    gc = gspread.oauth()
    gsheet = gc.open("MySheet").get_worksheet(1)
    data_all = gsheet.get_all_records()
    series = []
    for i in range(len(data_all)):
        series.append(data_all[i].get('price'))

    train, test = series[1:len(series) - 1], series[len(series) - 1:]
    # train autoregression
    model = AutoReg(train, lags=6)  # 6 - 63.89, 7 (max) - 58.82, expected - 62,25
    model_fit = model.fit()
    print('Coefficients: %s' % model_fit.params)
    # make predictions
    predictions = model_fit.predict(start=len(train), end=len(train) + len(test) - 1, dynamic=False)
    for i in range(len(predictions)):
        if predictions[i] > test[i]:
            print('predicted=%f, expected=%f' % (predictions[i], test[i]) + ' - overvalued')
        else:
            print('predicted=%f, expected=%f' % (predictions[i], test[i]) + ' - undervalued')
    rmse = sqrt(mean_squared_error(test, predictions))
    print('Test RMSE: %.3f' % rmse)

