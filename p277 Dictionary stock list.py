print("op1 for print average")
print("op2 for add new stocks")
op=int(input("enter your op=>"))

stock_prices={"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}

if op==1:
    for k,v in stock_prices.items():
        avg_price=sum(v)/len(v)
        print(k,"==>",v,"==>","avg:",avg_price)

if op==2:
    new_data = input("enter your data=>")
    price = int(input("enter key =>"))

    if new_data in stock_prices:
        stock_prices[new_data]=price
        print(stock_prices)

    elif new_data!= stock_prices:
        stock_prices[new_data]=price
        print(stock_prices)