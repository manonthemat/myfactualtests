import mykey
from factual import Factual # compiled for python 3 from the forked rep: https://github.com/manonthemat/factual-python-driver

factual = Factual(mykey.OAuthKey, mykey.OAuthSecret)
acai = factual.table('products').search('acai').data()
for i, listitem in enumerate(acai):
    print('Product #'+str(i+1))
    for k, v in listitem.items():
        if k == 'avg_price':
            print('Average price:', v)
        if k == 'product_name':
            print('Name:', v)
    print('*'*20)