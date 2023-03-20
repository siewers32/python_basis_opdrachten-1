import psutil
adapters = psutil.net_if_addrs()
keysList = list(adapters.keys())
print(keysList)
print(adapters['en1'][0].address)

