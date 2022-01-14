# Author ATN 1/14/22

from multiprocessing.sharedctypes import Value


print('Enter the net sales for')

previous = float(input('- Prior period:'))
current = float(input('- Current period:'))

change = (current - previous) * 100 / previous

try:
    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'
except:
    result = "Please check your inputs"
finally:
    print("Thank you for using this program.")

print(result)