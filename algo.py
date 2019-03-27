# algo.py contains the implementation of all the algorithms used in this project

# Longest Common substring
def longest_common_substring(X, Y, i, j, count) :  
      
    if (i == 0 or j == 0) :  
        return count  
          
    if (X[i - 1] == Y[j - 1]) : 
        count = longest_common_substring(X, Y, i - 1, j - 1, count + 1)  
      
    count = max(count, max(longest_common_substring(X, Y, i, j - 1, 0),  
                           longest_common_substring(X, Y, i - 1, j, 0)))  
  
    return count 

# Dynamic solution to longest common substring
def LCSubStr(X, Y, m, n): 
  
	LCSuff = [[0 for k in range(n+1)] for l in range(m+1)] 
 
	result = 0 

	for i in range(m + 1): 
		for j in range(n + 1): 
			if (i == 0 or j == 0): 
				LCSuff[i][j] = 0
			elif (X[i-1] == Y[j-1]): 
				LCSuff[i][j] = LCSuff[i-1][j-1] + 1
				result = max(result, LCSuff[i][j]) 
			else: 
				LCSuff[i][j] = 0
	return result 
	
# Longest Common Subsequence
def lcs(X, Y, m, n): 
  
    if m == 0 or n == 0: 
       return 0; 
    elif X[m-1] == Y[n-1]: 
       return 1 + lcs(X, Y, m-1, n-1); 
    else: 
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); 