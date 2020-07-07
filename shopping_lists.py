#Shopping List

print('Welcome to the Grocery Shopping Store')
print ('Add items to your bucket')
item=[]
item.append(str(input()))
for i in item:
    if i == 'done':
        item.remove ('done')
        print ('Here is your shopping list: {}'.format(item))
        print ('Do you wish to add more items?')
        print ('Enter Yes or No')
        str1 = str(input())
        if str1 == 'Yes':
            print ('Start adding items:')
            more_items=[]
            more_items.append(str(input()))
            for p in more_items:
                if p == 'done':
                    more_items.remove ('done')
                    final=item + more_items
                    print ('Your updated shopping list contains: {}'.format(final))
                    empty_list=[]
                    for i in final:
                        if (final.count(i)>1):
                            empty_list.append(i)
                            for j in empty_list:
                                if (empty_list.count(j)>1):
                                    empty_list.remove(j)
                    print('Found some duplicate items: {}'.format(empty_list))
                    print ('Do you wish to keep all duplicate items in your bucket?')
                    print ('Enter Yes or No')
                    str2 = str(input())
                    if str2 == 'Yes':
                        print ('Your shopping bucket with duplicate items is: {}'.format(final))
                    else:
                        for x in final:
                            if (final.count(x)>1):
                                final.remove(x)
                        print('Thank you for shopping. Your final list is: {}'.format(final))
                else:
                    more_items.append(str(input()))  
        else:
            print('Thank you for shopping with us. Your items are:')
            print (item)
        
    else:
        #print('Continue shopping')
        item.append(str(input()))
