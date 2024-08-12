from binance.client import Client

# Substitua com suas próprias chaves de API

client = Client(API_KEY, SECRET_KEY)




convert= client.convert_request_quote(fromAsset='USDT', toAsset='BRL',fromAmount=1)


print(convert)
