# meals = ['pasta','pizza','slad','melon']
# meals.sort()
#
# for meal in meals:
#     print(meal.capitalize())
l1 = ['1.vic','2.doc', '3.ram']
# l2 = ['.txt']
l2 = [item.replace('.' , '-') + '.txt'  for item in l1]
print(l2)
