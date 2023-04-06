dictionar = {"key1": 1,
             "key2": 2,
             3: 4,
             5.3: [0, 2, 5]
             }
print(type(dictionar))
print(dictionar)
print(dictionar.keys())
print(dictionar.values())
print(dictionar.items())
print(dictionar["key1"])
print(dictionar.get("Key1"))
dictionar["Key1"] = dictionar.get("key1", 100)
dictionar.update({"Key1": 100})
print()