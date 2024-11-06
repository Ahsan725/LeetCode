class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans = [transaction.split(",") for transaction in transactions]
        counter = collections.defaultdict(list)
        for name, time, amount, city in trans:
            counter[name].append((int(time), int(amount), city))
        ans = []
        for name in counter:
            for time, amount, city in counter[name]:
                if amount > 1000:
                    ans.append(",".join([name, str(time), str(amount), city]))
                    continue
                for time2, amount2, city2 in counter[name]:
                    if city2 != city and abs(time - time2) <= 60:
                        ans.append(",".join([name, str(time), str(amount), city]))
                        break
        return ans