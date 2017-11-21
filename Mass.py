#For this piece of code, I decided to use the mass numbers from my "Extended Game."

weights = [71,78,58,96,82,52,95,56,59,63]

category1Count = 0
category2Count = 0
category3Count = 0
category4Count = 0

for weight in weights:
  if weight < 70:
   category1Count = category1Count + 1 
  if weight >= 70 and weight <= 85:
    category2Count = category2Count + 1 
  if weight >= 85 and weight <= 100:
    category3Count = category3Count + 1 
  if weight > 100:
    category4Count = category4Count + 1 
print("Category 1, Count", category1Count)
print("Category 2, Count", category2Count)
print("Category 3, Count", category3Count)
print("Category 4, Count", category4Count)
