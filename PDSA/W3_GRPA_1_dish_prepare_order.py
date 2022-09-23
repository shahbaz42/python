def DishPrepareOrder(nums):
    d ={}
    for i in nums:
        if i in d:
            d[i] += 1
        else :
            d[i] = 1
    order_freq = list(d.items())
    order_freq = sorted(order_freq, key=lambda x:x[0])
    order_freq = sorted(order_freq, key=lambda x: -1*x[1])
    result = [x[0] for x in order_freq]
    return result
    
nums = eval(input())
print(DishPrepareOrder(nums))