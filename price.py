#task market ma janca saman order garxa saman ko kei fixed price hunxa ani certain discount hunca ani final price huca

market_name=str(input("enter your city:"))
item_kaname=str(input("enter the item name...:"))
item_no=(input("enter item number...:"))
mp=int(inputz("enter the market price...:"))
dt=int("enter the discount percent:")

sp=mp-(d*mp)/100

my_order="i want to the {} and i briugh a {} also it has costing rs {} with discounyt{}, finally got with {}. "
print(my_order.format(market_name,item_name,item_no,mp,d,sp))