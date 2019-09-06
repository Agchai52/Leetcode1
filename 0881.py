class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dmap = collections.defaultdict(int)
        for cpdomain in cpdomains:
            cp, domain = cpdomain.split(' ')          
            sub = ''
            domain = domain.split('.')
            for d in domain[::-1]:
                sub = d + '.' + sub
                dmap[sub[:-1]] += int(cp)
        res = [str(v)+' '+k for k, v in dmap.items()]
        return res
                
