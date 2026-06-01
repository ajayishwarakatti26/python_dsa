### temoplet fix window:
def fixed_sliding_window(arr, k):
    n = len(arr)
    if n < k:
        return 0  # Edge case: array smaller than window size
    
    # --- Step 1: Compute information for the FIRST window ---
    # (Low = 0, High = k - 1)
    current_info = sum(arr[:k])  # Example: Information is 'Sum'
    max_result = current_info     # Track the best result found so far
    
    # Initialize pointers for the sliding phase
    low = 0
    high = k - 1
    
    # --- Step 2: Slide the window across the array ---
    while high < n:
        # Update your global result with the current valid window [00:09:18]
        max_result = max(max_result, current_info)
        
        # Remove the 'low' element's contribution and increment 'low' [00:10:01]
        current_info -= arr[low]
        low += 1
        
        # Increment 'high' and check bounds before including it [00:10:33]
        high += 1
        if high == n:
            break
            
        # Include the new 'high' element's contribution [00:10:42]
        current_info += arr[high]
            
    return max_result

###  vriable:
def variable_sliding_window(arr, target):
    n = len(arr)
    low = 0
    max_length = 0
    current_info = 0  # Example: Tracking cumulative sum
    
    # Expand the window using the 'high' pointer [00:13:25]
    for high in range(n):
        # Step 1: Include the new element at 'high' [00:13:50]
        current_info += arr[high]
        
        # Step 2: Contract the window from 'low' while the condition is violated [00:21:19]
        # (Example condition: Sum exceeds a given target limit)
        while current_info > target:  
            current_info -= arr[low]  # Remove 'low' contribution [00:21:49]
            low += 1                  # Shrink the window
            
        # Step 3: If valid, calculate length and update result [00:22:16]
        # (Check if current_info matches your exact 'correct' criteria if required)
        if current_info == target:  
            window_len = high - low + 1
            max_length = max(max_length, window_len)
            
    return max_length