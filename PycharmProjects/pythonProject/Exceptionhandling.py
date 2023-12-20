ItemsInCart = 0
if ItemsInCart != 2:
    # raise Exception('Product cart count is not match')  -- this is one condition
   pass  #it does not do anything if condtion not execute by using pass keyword
assert(ItemsInCart == 0)

try:
    with open('textfileone.txt') as reader:
        reader.read()

except:
    print('I have reached this block because there is an error in try block')

try:
    with open('textfileone.txt') as reader:
        reader.read()

except Exception as error:
    print(error)