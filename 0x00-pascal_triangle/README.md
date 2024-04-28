# Pascal's Triangle
>> This Python script generates Pascal's Triangle up to the nth row and provides a function to retrieve the triangle as a list of lists.

# Table of Contents
>> Introduction
>> Features
>> Requirements
>> Installation
>> Usage
>> Examples
>> Contributing
>> License

# Introduction
>> Pascal's Triangle is a mathematical triangle named after the French mathematician Blaise Pascal. It is constructed by summing adjacent elements in preceding rows. The triangle starts with a single 1 at the top and continues placing numbers below it in a triangular pattern, with each number being the sum of the two numbers directly above it.

This Python script provides a function pascal_triangle(n) that generates Pascal's Triangle up to the nth row and returns it as a list of lists.

# Features
>> Generates Pascal's Triangle up to the nth row
>> Returns the triangle as a list of lists
>> Handles edge cases gracefully

# Requirements
>> Python 3.x

# Installation
>> Clone the repository:
	git clone https://github.com/yourusername/pascals-triangle.git
>> Change directory to the project folder:
	cd pascals-triangle
>> Run the provided example or incorporate the pascal_triangle function into your own Python projects.

# Usage
	from pascal_triangle import pascal_triangle

	# Generate Pascal's Triangle up to the 5th row
	triangle = pascal_triangle(5)
	print(triangle)

# Examples
>> Input :
	from pascal_triangle import pascal_triangle

	# Generate and print Pascal's Triangle up to the 7th row
	triangle = pascal_triangle(7)
	for row in triangle:
		print(row)
>> Output:
	[1]
	[1, 1]
	[1, 2, 1]
	[1, 3, 3, 1]
	[1, 4, 6, 4, 1]
	[1, 5, 10, 10, 5, 1]
	[1, 6, 15, 20, 15, 6, 1]

# Contributing
>> Contributions are welcome! If you have suggestions or improvements, please fork the repository and create a pull request. For major changes, please open an issue first to discuss the changes.

# License
>> None



