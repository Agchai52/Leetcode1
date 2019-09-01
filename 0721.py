class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        if len(accounts) <= 0: return accounts
        eset = set() # emails
        parent = {} # {a: parent(a)}
        owner = {} # {email: name}
        res = collections.defaultdict(list)
        
        def findParent(e): # find root, and rank of e in tree 
            rank = 0
            while e != parent[e]:
                rank += 1
                e = parent[e]
            return e, rank
        
        def merge(a, b): 
            pa, ra = findParent(a)
            pb, rb = findParent(b)
         
            if ra < rb: 
                
                parent[pa] = pb
            else: 
                parent[pb] = pa
                
        
            
            
        for account in accounts:
            name, emails = account[0], account[1:]
            for email in emails:
                eset.add(email)
                owner[email] = name
                if email not in parent: parent[email] = email
            for email in emails[1:]:
                merge(emails[0], email)
        
        for email in eset:
            res[findParent(email)[0]].append(email)
        
        
        return [[owner[k]]+sorted(v) for k, v in res.iteritems()]
                
        
        
