import sys
import pandas as pd
import numpy as np
import time

def main():
    df = pd.read_csv('yelp_business.csv')
    print len(df)
    h1 = h = list(df.columns.values)

    for item in h:
        try:
            if df[item].dtype == np.dtype('O'):
                if not df[item][0].isdigit():
                    df[item] = df[item].map(lambda a:a.replace('"',''))
        except:
            continue

    target = open('target.json','w+')

    headers = []
    for item in h:
        s = '"'+item+'"'
        headers.append(s)

    for i in range(len(df.iloc[:])):
        rec = '{'
        for j in range(len(headers)):
            if j == len(headers) - 1:
                rec += '{'+headers[j]+':'+ str('"'+df.iloc[i][h[j]]+'"')+'}'
            else:
                rec += '{'+str(headers[j])+':'+'"'+str(df.iloc[i][h[j]])+'"'+'},'
        rec += '},'
        target.write(rec+'\n')
    target.close()

if __name__ == '__main__':
    main()
