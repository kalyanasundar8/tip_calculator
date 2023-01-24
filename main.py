food_amount = float(input("💵 Enter your food amount : "))
tip_percentage = float(input("💵 Enter your tip amount : ")) / 100
tip_amount = food_amount * tip_percentage
print('----------------------------------------------')

print(f'😋 Food Amount : ${food_amount}')
print(f'💁 Tip percentage : ${tip_percentage}')
print(f'💶 Tip amount : ${tip_amount}')
total_amount = food_amount + tip_amount
print(f'💰 Total Amount : ${total_amount}')
print('----------------------------------------------')