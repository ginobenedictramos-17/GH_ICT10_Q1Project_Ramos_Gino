from pyscript import display
# I used chat GPT to check and correct certain parts of this script
restaurant_name = 'Taco Bell'
year_established = '1962'
slogan = 'Live Mas!'
item_1 = 'Burrito Beef and Potato'
item_1_price = 'P169'
item_2 = 'Crispy Shell Beef Taco'
item_2_price = 'P99'
item_3 = 'Flaming Quesowrap Supreme'
item_3_price = 'P219' 
has_delivery = 'We offer delivery (call 2357911131719) and'
business_hours = 'we are open at our branches everyday from 7am-10pm'

display(f"{restaurant_name} (Est. {year_established}) - {slogan}", target="div1") # col 15-21 were corrected and improved upon by chat GPT
# col 8-27 in index.html was also corrected and debugged by chat GPT (I put this note here because the hastag statement did not work on my html file)
display(f"{item_1} — {item_1_price}", target="div2")
display(f"{item_2} — {item_2_price}", target="div3")
display(f"{item_3} — {item_3_price}", target="div4")

display(f"{has_delivery} {business_hours}", target="div5")