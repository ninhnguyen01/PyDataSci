# Explore the data
print(cellphone.head())

# Create a scatter plot of the data from the DataFrame cellphone
plt.scatter(cellphone.x,cellphone.y)

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()

# Change the marker color to red
plt.scatter(cellphone.x, cellphone.y,
           color='red')

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()

# Display the DataFrame hours using print
print(hours)

# Plot the number of hours spent on desk work
plt.bar(hours.officer,hours.desk_work, label = "Desk Work")

# Display the plot
plt.show()

# Create a histogram of the column weight from the DataFrame puppies
plt.hist(puppies.weight)

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()

# Create a histogram of gravel.radius
plt.hist(gravel.radius)

# Display histogram
plt.show()

