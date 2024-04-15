#Problem 1. print your first and last name.
first_name= "Ezequiel"
last_name= "Gwilliam"
print (first_name,last_name)

#Problem 2. Create an array named cars.
cars= ["Ford","Chrysler","Dodge","Ram","Jeep","Chevy","GMC"]
print(cars)

#Problem 3. Print the array to the console.
#['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC']

#Problem 4. Print the length of the array to the console
length_of_array= len(cars)
print(f"The length of the array is: {length_of_array} ")

#Problem 5. Append Buick to the array.
cars.append("Buick")
print(cars)

#Problem 6. print the array to the console.
#['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC', 'Buick']

#Problem 7. print the 4th element in the array.
print("The 4th element in the array is", cars[3])

#Problem 8. Insert 'Toyota' into element 3 in the array.
cars.insert(2, "Toyota")
print(cars)

#Problem 9. Print the array to the console
#['Ford', 'Chrysler', 'Toyota', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC', 'Buick']

#Problem 10. Remove element 5 of the array.
cars.pop(4)
print(cars)

#Problem 11. Print the array to the console.
#['Ford', 'Chrysler', 'Toyota', 'Dodge', 'Jeep', 'Chevy', 'GMC', 'Buick']

#Problem 12. Sort the Array in ascending order
cars.sort()
print(cars)

#Problem 13. Print the array to the console
#['Buick', 'Chevy', 'Chrysler', 'Dodge', 'Ford', 'GMC', 'Jeep', 'Toyota']

#Problem 14. Sort the array in descending order.
cars.sort(reverse=True)
print(cars)

#Problem 15. Print the array to the console
#['Toyota', 'Jeep', 'GMC', 'Ford', 'Dodge', 'Chrysler', 'Chevy', 'Buick']

#Problem 16. Create a variable called my_array_length with a value of the cars array length.
my_array_length= len(cars)
print( my_array_length)

#Problem 17. create a variable called array_string with a value of 'The length of my array is '.
array_string= 'The length of my array is: '

#Problem 18. 
print(array_string + str(my_array_length))

#Total Console Log-
#Ezequiel Gwilliam
#['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC']
#The length of the array is: 7
#['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC', 'Buick']
#The 4th element in the array is Ram
#['Ford', 'Chrysler', 'Toyota', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC', 'Buick']
#['Ford', 'Chrysler', 'Toyota', 'Dodge', 'Jeep', 'Chevy', 'GMC', 'Buick']
#['Buick', 'Chevy', 'Chrysler', 'Dodge', 'Ford', 'GMC', 'Jeep', 'Toyota']
#['Toyota', 'Jeep', 'GMC', 'Ford', 'Dodge', 'Chrysler', 'Chevy', 'Buick']
#8
#The length of my array is: 8