import pandas as pd


def add_keyword(word):
    df = pd.read_csv('test.csv') 

    if word in df.values:
        filt = (df['key'] == word)
        df.loc[filt, 'freq'] += 1
    else:
        df = df.append({'key': word, 'freq': 1}, ignore_index=True)

    df.to_csv('test.csv', index=False)


def recommend():
    df = pd.read_csv('test.csv')    

    if df.shape[0] <= 0:
        return '295'

    df.sort_values(by='freq', ascending=False, inplace=True)
    ff = df.head(1)
    output = ff.loc[0, 'key']
    
    return output


