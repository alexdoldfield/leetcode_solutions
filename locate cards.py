#!/usr/bin/env python
# coding: utf-8

# In[5]:


cards = [1, 3, 7, 8, 9, 10, 11, 12, 14, 101, 103, 105, 1200, 5601, 7819, 9412]
query = 1

def locate_card(cards: list, query: int) -> int:
    low_index = 0
    high_index = len(cards) -1
    
    while low_index <= high_index:
        midpoint = (high_index + low_index)// 2
        
        if cards[midpoint] == query:
            
            print(f'the card was at position {midpoint+1}')
            
            return midpoint+1

            
        elif cards[midpoint] < query:
            
            print(f"the card was greater than {cards[midpoint]}")
            
            low_index = midpoint +1
            
            print(f"searching between position {low_index+1} and position {high_index+1}")
        
        else:
            
            print(f"the card is less than {cards[midpoint]}")
            
            high_index = midpoint -1
            
            print(f"searching between position {low_index+1} and position {high_index+1}")
    return -1
            
locate_card(cards, query)


# In[ ]:




