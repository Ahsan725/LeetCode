class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = []
        name_mail = defaultdict(set)
        #we are returning a list of lists
        #creating a hashmap -> name: emails
        #we only need to check if the name matches if the name does not match then we dont do anything 
        
        #create a hashmap
        for acc in accounts:
            tokens = acc.split(",")
            name = tokens[0]
            emails = tokens[1:]

            #add to hashmap
            if name in name_mail:
                #name matches but now we check for if emails match
                for email in emails:
                    if email in name_mail[name]:
                        #merge
                        all_emails = set()
                        all_emails.add(for email in emails) #add all the emails from this set of emals
                        all_emails.add(name_mail[name] #also add emails from the previous set in the map
                        res.append([(name, list(all_emails))])
                    else:
                        #do not merge
                        continue

            else:
                #not in the map before first time seeing it because if the name doesnt exist the email wont either
                for email in emails:
                    name_mail[name].add(email)
        return res 