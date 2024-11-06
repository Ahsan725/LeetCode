from typing import List
from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # Dictionary to store times of transactions for each name
        name_to_time = defaultdict(list)
        
        # Dictionary to store cities of transactions for each name
        name_to_city = defaultdict(list)
        
        # Dictionary to map each transaction to its name and time for easy access
        transaction_map = defaultdict(list)
        
        # Set to store invalid transactions
        invalid_transactions = []

        # Step 1: Populate the dictionaries with transaction details
        for trans in transactions:
            name, time, amount, city = trans.split(',')
            time = int(time)
            amount = int(amount)
            city = city.lower()  # Convert city to lowercase for case-insensitive comparison

            # Store the transaction details in each dictionary
            name_to_time[name].append(time)
            name_to_city[name].append(city)
            transaction_map[name].append((time, city, trans))

            # Case 1: If the amount exceeds $1000, add it directly to the invalid set
            if amount > 1000:
                invalid_transactions.append(trans)

        # Step 2: Check for transactions within 60 minutes in different cities
        for name in transaction_map:
            transactions = transaction_map[name]

            # Compare each transaction for this name with others for 60-minute window in different cities
            for i in range(len(transactions)):
                time_i, city_i, trans_i = transactions[i]

                # Check transaction i against every other transaction j for the same name
                for j in range(i + 1, len(transactions)):
                    time_j, city_j, trans_j = transactions[j]

                    # If transactions are within 60 minutes and in different cities, both are invalid
                    if abs(time_i - time_j) <= 60 and city_i != city_j:
                        invalid_transactions.append(trans_i)
                        invalid_transactions.append(trans_j)

        # Step 3: Convert the invalid set to a list and return it
        return list(invalid_transactions)
