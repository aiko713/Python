weight = 80

# Ground shipping 
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20 
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20 

print ("Ground shipping $", cost_ground)

#Ground Shipping Premium
cost_ground_premium = 125

print ("Ground shipping premium $", cost_ground_premium)

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5 
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25 

print ("Drone shipping $", cost_drone)