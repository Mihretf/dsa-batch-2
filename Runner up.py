if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores = list(set(arr))     
    unique_scores.sort(reverse=True)   
    
    print(unique_scores[1]) 
