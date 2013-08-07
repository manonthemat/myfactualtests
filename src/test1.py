import mykey
from factual import Factual # compiled for python 3 from the forked rep: https://github.com/manonthemat/factual-python-driver

factual = Factual(mykey.OAuthKey, mykey.OAuthSecret)
starbucks = factual.table("places").search("starbucks palmdale").filters({"address":{"$blank":False}})

print('Starbucks in Palmdale')
for listitem in starbucks.data():
    for k, v in listitem.items():
        if k == 'address':
            print (v)