import ephem
mars = ephem.Mars('2017/09/01')
print(ephem.constellation(mars))

print(ephem.next_full_moon('2017/09/01'))