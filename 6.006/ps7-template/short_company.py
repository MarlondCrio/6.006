def short_company(C, P, n, k):
    '''
    Input:  C | Tuple of s = |C| strings representing names of companies
            P | Tuple of s lists each of size nk representing prices
            n | Number of days of price information
            k | Number of prices in one day
    Output: c | Name of a company with highest shorting value
            S | List containing a longest subsequence of 
              | decreasing prices from c that doesn't skip days
    '''
    c = C[0]
    S = []
    for comp in range(len(C)):
        seq = lon_dec_seq(P[comp], k)
        if len(seq) > len(S):
            S = seq
            c = C[comp]
    return (c, S)

def lon_dec_seq(d, k):
    lis = []
    for i in range(len(d)):

        new = []
        for j in range(max(0, i-i%k-k), i):
            if d[i] < lis[j][-1]:
                new.append(lis[j])

        lis.append(max(new or [[]], key=len) + [d[i]])

    return max(lis, key=len)
