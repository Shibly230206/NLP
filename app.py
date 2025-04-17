import tabula

# Read PDF into a list of DataFrames
data = tabula.read_pdf("CoffeeShopPriceList.pdf", pages="all", multiple_tables=True)

# Print each DataFrame
for table in data:
    print(table)
tabula.convert_into("CoffeeShopPriceList.pdf","output.csv",pages="all",output_format="csv")