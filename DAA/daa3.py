class Item:
  def __init__(self , profit , weight):
    self.profit = profit
    self.weight = weight

def fractionalKnapsack(capacity,arr):   
  arr.sort(key=lambda obj : (obj.profit/obj.weight) ,reverse=True)
  finalprofit=0.0
  for item in arr:
    if(item.weight < capacity):
      capacity=capacity - item.weight
      finalprofit=finalprofit + item.profit
    else:
      finalprofit=finalprofit+(item.profit*(capacity/item.weight))
      break
  return finalprofit


if __name__=="__main__":
  capacity=int(input("enter capacity: "))
  n=int(input("enter the no of items: "))
  arr=[]
  for i in range(0,n):
    profit = int(input("Enter profit: "))
    weight = int(input("Enter weight: "))
    temp = Item(profit,weight)
    
    arr.append(temp)

  # arr = [Item(24, 15), Item(15, 10), Item(25, 18)]
  maxprofit=fractionalKnapsack(capacity,arr)
  print(maxprofit)
  
