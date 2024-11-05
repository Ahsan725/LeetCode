class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        #the amount exceeds $1000, or;
        #if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

        name_to_info ={}
        full_info = {}
        invalid = []

        #we are really only concerned about name, time and different city
        for trans in transactions:
            fields = trans.split(",") #alice,20,800,mtv"
            name = fields[0].lower()
            mins = int(fields[1])
            amount = int(fields[2])
            city = fields[3].lower()

            #over 1000 invalid
            if amount > 1000:
                invalid.append(trans)

            if name in name_to_info: #name is the same
                prev_time = name_to_info[name]["time"]
                prev_city = name_to_info[name]["city"]
                if abs(prev_time - mins) < 60 and prev_city != city and amount < 1000:
                    invalid.append(trans)
                    invalid.append(full_info[name])
                elif abs(prev_time - mins) < 60 and prev_city == city and amount < 1000:
                    if trans and full_info[name] not in invalid:
                        invalid.append(trans)
                        invalid.append(full_info[name])


            name_to_info[name] = {"time" : mins, "city" : city, "amount" : amount}
            full_info[name] = trans # value is the whole string of transaction

        return invalid


