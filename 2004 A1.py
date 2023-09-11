def restaurantFinder(d, site_list):
    max_profits = [0] * len(site_list)
    max_profits[0] = site_list[0]
    
    # Need first loop since we cannot assume d < len(site_list)
    for i in range(1,d):
        if site_list[i] > max_profits[i-1]:
            max_profits[i] = site_list[i]
        else:
            max_profits[i] = max_profits[i-1]

    for j in range(d, len(site_list)):
        if max_profits[j-1] > max_profits[j-d-1] + site_list[j]:
            max_profits[j] = max_profits[j-1]
        else:
            max_profits[j] = max_profits[j-d-1] + site_list[j]
    
    # Getting site lists from max_profits list
    rests = []  
    k = len(site_list)-1
    while k>=0:
        if max_profits[k]> max_profits[k-1]:
            rests.append(k+1)
            k = k-d-1
        else:
            k = k-1
        if k == 0:
            rests.append(1)

    return max_profits[-1], rests[::-1]



print(restaurantFinder(1, [50, 10, 12, 65, 40, 95, 100, 12, 20, 30])) #252 [1,4,6,8,10]
print(restaurantFinder(2, [50, 10, 12, 65, 40, 95, 100, 12, 20, 30])) #245 [1,4,7,10]
print(restaurantFinder(3, [50, 10, 12, 65, 40, 95, 100, 12, 20, 30])) #175 [1,6,10]
print(restaurantFinder(7, [50, 10, 12, 65, 40, 95, 100, 12, 20, 30])) #100 [7]
print(restaurantFinder(0, [50, 10, 12, 65, 40, 95, 100, 12, 20, 30])) #434 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(restaurantFinder(1, [1, 2, 3, 3,0, 0, 2, 2,2]))