pens_pack_price = 5.8
markers_pack_price = 7.2
cleaning_agent_price_per_liter = 1.2

pens_packs = int(input())
markers_packs = int(input())
cleaning_agent_liters = int(input())
discount = int(input())

total_price = (pens_packs * pens_pack_price + markers_packs * markers_pack_price +
               cleaning_agent_liters * cleaning_agent_price_per_liter) * (100 - discount) / 100

print(total_price)