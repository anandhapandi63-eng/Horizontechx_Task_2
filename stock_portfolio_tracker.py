stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 420,
    "AMZN": 190
}

total_value = 0

print("=" * 40)
print("     STOCK PORTFOLIO TRACKER")
print("=" * 40)

num_stocks = int(input("How many stocks do you own? "))

for i in range(num_stocks):

    stock = input("\nEnter Stock Symbol: ").upper()

    if stock not in stock_prices:
        print("Stock not available!")
        continue

    quantity = int(input("Enter Quantity: "))

    investment = stock_prices[stock] * quantity

    total_value += investment

    print(f"Investment Value: ${investment}")

print("\n" + "=" * 40)
print(f"Total Portfolio Value: ${total_value}")
print("=" * 40)




with open("portfolio_report.txt", "w") as file:
    file.write(f"Total Portfolio Value: ${total_value}")

print("Portfolio report saved successfully!")