import pandas as pd
import os

# Function to analyze the data
def analyze_diamonds(df):
    # Highest priced item
    highest_price_item = df.loc[df['price'].idxmax()]
    highest_price_item_details = highest_price_item.to_dict()

    # Average price
    average_price = df['price'].mean()

    # Count of "Ideal" cut diamonds
    ideal_count = df[df['cut'] == 'Ideal'].shape[0]

    # Number of unique colors and the list of unique colors
    unique_colors_list = df['color'].unique()
    unique_colors_count = len(unique_colors_list)


    # Median carat for "Premium" cut diamonds
    median_carat_premium = df[df['cut'] == 'Premium']['carat'].median()

    # Average carat for each type of cut
    average_carat_by_cut = df.groupby('cut')['carat'].mean().to_dict()

    # Average price for each color
    average_price_by_color = df.groupby('color')['price'].mean().to_dict()

    return [
        highest_price_item_details,
        average_price,
        ideal_count,
        (unique_colors_count, unique_colors_list),
        median_carat_premium,
        average_carat_by_cut,
        average_price_by_color
    ]

# Function to print the analysis results
def print_analysis_results(results, choice):
    labels = [
        "Highest Priced Item",
        "Average Price",
        "Number of 'Ideal' cut diamonds",
        "Number of unique colors",
        "Median carat for 'Premium' cut diamonds",
        "Average carat for each type of cut",
        "Average price for each color"
    ]

    print(labels[choice - 1] + ":")
    if choice == 4:
        print(f"  Count: {results[choice - 1][0]}")
        print("  Colors:", ', '.join(results[choice - 1][1]))
    elif isinstance(results[choice - 1], dict):
        for key, value in results[choice - 1].items():
            print(f"  {key}: {value}")
    else:
        print(results[choice - 1])

# Reading the CSV data from a file
file_path = os.getenv('DIAMONDS_CSV_PATH', 'diamonds.csv')
diamonds_df = pd.read_csv(file_path)

# Analyzing the diamonds data
analysis_results = analyze_diamonds(diamonds_df)

# User interface
print("Choose an analysis:")
print("1. Highest Priced Item")
print("2. Average Price")
print("3. Number of 'Ideal' cut diamonds")
print("4. Number of unique colors")
print("5. Median carat for 'Premium' cut diamonds")
print("6. Average carat for each type of cut")
print("7. Average price for each color")

choice = int(input("Enter your choice (1-8): "))

# Print the analysis results based on user's choice
print_analysis_results(analysis_results, choice)
