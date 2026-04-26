import pandas as pd
import matplotlib.pyplot as plt

file_path = "collegeass/python/dataset.csv"
data = pd.read_csv(file_path)

data["Selling Price"] = data["Selling Price"].astype(str)
data["Selling Price"] = data["Selling Price"].str.replace("$", "")
data["Selling Price"] = data["Selling Price"].str.split("-").str[0]
data["Selling Price"] = data["Selling Price"].str.strip()
data["Selling Price"] = pd.to_numeric(data["Selling Price"], errors="coerce")
subset = data.dropna(subset=["Selling Price", "Category"])

#  BAR GRAPH 
subset["Category"].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title("Top 10 Product Categories")
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.xticks(rotation=45)
plt.show()

# LINE GRAPH 
plt.plot(subset["Selling Price"].head(50), marker='o', color='green')
plt.title("Selling Price Trend (First 50 Products)")
plt.xlabel("Product Index")
plt.ylabel("Selling Price ($)")
plt.show()

#  HISTOGRAM 
plt.hist(subset["Selling Price"], bins=15, color='orange', edgecolor='black')
plt.title("Distribution of Selling Prices")
plt.xlabel("Selling Price ($)")
plt.ylabel("Frequency")
plt.show()

# PIE CHART 
subset["Is Amazon Seller"].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    colors=['lightcoral', 'lightgreen']
)
plt.title("Amazon vs Non-Amazon Sellers")
plt.ylabel("")  # Hides the extra label
plt.show()

#  SCATTER PLOT 
plt.scatter(range(len(subset)), subset["Selling Price"], color='purple')
plt.title("Scatter Plot of Selling Prices")
plt.xlabel("Product Index")
plt.ylabel("Selling Price ($)")
plt.show()
