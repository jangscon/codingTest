N , M = map(int, input().split())
recipe = []
for i in range(M) :
    recipe_input = list(map(int , input().split()))
    recipe_input = (recipe_input[1:recipe_input[0]+1] , recipe_input[-1])
    recipe.append(recipe_input)
L = int(input())
potion = list(map(int , input().split()))

temp = []

for i in recipe_input :
    temp.append(i[1])





# while_break = True
#
# while True :
#     while_break = True
#     if not recipe :
#         break
#     for i in recipe[:] :
#         if i[1] in potion :
#             recipe.remove(i)
#             while_break = False
#         elif list(set(i[0]) & set(potion)) == i[0] :
#             L += 1
#             potion.append(i[1])
#             recipe.remove(i)
#             while_break = False
#     if while_break :
#         break
#
#
# potion.sort()
# print(L)
# print(' '.join(map(str , potion)))