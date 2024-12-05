# Ch.6, Ex.4 (extra credit)
# Saba Feilizadeh
# This program creates a table for the Figure Skating Medals


# Constant for the width of the line for the output
LINE_WIDTH = 40
GAP_GOLD = len("gold") // 2
GAP_SILVER = len("silver") // 2
GAP_BRONZE = len("bronze") // 2

# List of medals for each country
# Country,  Gold,  Silver,  Bronze
CANADA = ["Canada", 0, 3, 0]
ITALY = ["Italy", 0, 0, 1]
GERMANY = ["Germany", 0, 0, 1]
JAPAN = ["Japan", 1, 0, 0]
RUSSIA = ["Russia", 3, 1, 1]
SOUTHKOREA = ["South Korea", 0, 1, 0]
US = ["United States", 1, 0, 1]
# A list of all the countries' names and their medals
original_countries = [CANADA, ITALY, GERMANY, JAPAN, RUSSIA, SOUTHKOREA, US]
countries = [CANADA, ITALY, GERMANY, JAPAN, RUSSIA, SOUTHKOREA, US]

# --------------------------------------------------------------------------
def print_table():
    '''
    This function prints a table, showing the medal count for each country.
    '''
    # Table header
    print("=" * LINE_WIDTH)
    print("Country       ", "|", "Gold", "|", "Silver", "|", "Bronze")
    print("=" * LINE_WIDTH)

    # Table content
    for country in countries:
        print(f"{country[0]:<{LINE_WIDTH // 3 + 1}}", "|",
              f" {country[1]:<{GAP_GOLD}}", " | ",
              f" {country[2]:<{GAP_SILVER}}", " | ",
              f" {country[3]:<{GAP_BRONZE}}", "|")

    print("=" * LINE_WIDTH)

# --------------------------------------------------------------------------
def print_total_num_of_medals():
    """
    This function computes the total number of medals.
    """
    medal_num = 0
    for country in countries:
        for i in range(1,4):
            medal_num += country[i]

    print("Total number of medals: ", medal_num)

# --------------------------------------------------------------------------
def calculate_num_of_each_medal():
    """
    This function computes and returns the total number of each type of medal.
    (total number of gold, silver, and bronze medals.)
    """
    
    num_of_gold = 0
    num_of_silver = 0
    num_of_bronze = 0

    for country in countries:
        num_of_gold += country[1]
        num_of_silver += country[2]
        num_of_bronze += country[3]

    return num_of_gold, num_of_silver, num_of_bronze
# --------------------------------------------------------------------------
def print_num_of_each_medal():
    '''
    This function prints the total number of each type of medal.
    (total number of gold, silver, and bronze medals.)
    '''
    print("-" * LINE_WIDTH)
    print("Total number of Gold:   ", calculate_num_of_each_medal()[0])
    print("Total number of Silver: ", calculate_num_of_each_medal()[1])
    print("Total number of Bronze: ", calculate_num_of_each_medal()[2])
    print("-" * LINE_WIDTH)
# --------------------------------------------------------------------------
def remove_countries_without_gold_medal():
    '''
    This function removes the coutries without any gold medals from the table.
    '''

    countries_without_gold_medal = []

    for country in countries:
        if country[1] < 1:
            countries_without_gold_medal.append(country)

    for country in countries_without_gold_medal:
        countries.remove(country)
# --------------------------------------------------------------------------
def save_data_into_a_dictionary():
    '''
    This function saves all the data into a dictionary
    and returns the dictionary.
    (it uses the original list of countries and their medals)
    (the key is the country name and the value is a list of medals)
    '''
    medal_dictionary = {}

    for country in original_countries:
        medal_dictionary[country[0]] = [country[1], country[2], country[3]]
    
    return medal_dictionary
# --------------------------------------------------------------------------
def main():
    # Print the table of medals
    print_table()

    # Print the total number of medals
    print_total_num_of_medals()

    # Print the total number of gold, silver, and bronze medals
    print_num_of_each_medal()

    # Remove countries without a gold medal from the table
    remove_countries_without_gold_medal()

    # Print the updated table of medals
    print("UPDATED TABLE:")
    print_table()

    # Save the info in a dictionary
    medal_dictionary = save_data_into_a_dictionary()

    # Print the dictionary
    print(medal_dictionary)


# --------------------------------------------------------------------------
main()

print("Done!")

# --------------------------------------------------------------------------
'''
Output:

========================================
Country        | Gold | Silver | Bronze
========================================
Canada         |  0   |   3    |   0   |
Italy          |  0   |   0    |   1   |
Germany        |  0   |   0    |   1   |
Japan          |  1   |   0    |   0   |
Russia         |  3   |   1    |   1   |
South Korea    |  0   |   1    |   0   |
United States  |  1   |   0    |   1   |
========================================
Total number of medals:  14
----------------------------------------
Total number of Gold:    5
Total number of Silver:  5
Total number of Bronze:  4
----------------------------------------
UPDATED TABLE:
========================================
Country        | Gold | Silver | Bronze
========================================
Japan          |  1   |   0    |   0   |
Russia         |  3   |   1    |   1   |
United States  |  1   |   0    |   1   |
========================================
{'Canada': [0, 3, 0], 'Italy': [0, 0, 1], 'Germany': [0, 0, 1], 'Japan': [1, 0, 0], 'Russia': [3, 1, 1], 'South Korea': [0, 1, 0], 'United States': [1, 0, 1]}
Done!

'''