height = [5,4,3,5,6,7,4,2,1]

def max_area(height:list[int])-> int:
    l,r = 0, len(height)-1
    largest_area = 0
    while l < r: 
        current_area = (r - l) * min(height[l], height[r])
        largest_area = max(largest_area, current_area)
        if height[l] < height[r]:
                l += 1
        elif height[l]> height[r]:
            r -= 1
        else: l += 1
    return largest_area    
            
        
        
        
        

print(max_area(height))