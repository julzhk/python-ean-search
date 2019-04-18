# EANSearch

A Python class for EAN and ISBN name lookup and validation using the API on https://www.ean-search.org

Compatible with Python 3.6+

```python
from eansearch import EANSearch

# get a token from https://www.ean-search.org/ean-database-api.html
apiToken = "<TOKEN>"
ean = "5099750442227" # Thriller

lookup = EANSearch(apiToken)

name = lookup.barcodeLookup(ean)
print(f"{ean} is {name}")

ok = lookup.verifyChecksum(ean)
print(ean, " is ", "OK" if ok else "Not OK")

eanList = lookup.productSearch('iPod');
for product in eanList:
    print(f'{product["ean"]} is {product["name"]}')

eanList = lookup.barcodePrefixSearch('4007249146')
for product in eanList:
    print(f'{product["ean"]} is {product["name"]}')

