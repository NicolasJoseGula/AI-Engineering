# Smart Bill Calculator

A simple Python console application that calculates discounts, VAT, tips, and the final total of a purchase.

## Overview

**Smart Bill Calculator** is a beginner-friendly Python project designed to solve common financial calculations in a clear and reusable way.

The application can:

- calculate the discount amount and discounted price
- calculate VAT and subtotal with VAT
- calculate the tip amount and total with tip
- execute the full purchase flow from base price to final total

This project was built to practice core Python fundamentals through a practical real-world problem.

## Project Goal

The goal of this project is to apply basic programming and math concepts in a structured console application.

It focuses on:

- variables
- arithmetic operators
- functions
- conditional statements
- return values
- clean output formatting

## Features

- Discount calculation
- VAT calculation
- Tip calculation
- Full purchase summary
- Basic validation for invalid values
- Support for decimal prices
- Handling of special cases such as 0% discount, 0% VAT, 0% tip, and 100% discount

## Example Use Cases

This application can be used for scenarios such as:

- calculating the final price of a product after a discount
- adding VAT to a subtotal
- estimating the total cost of a restaurant bill including tip
- showing a full breakdown of a purchase from start to finish

## Functional Scope

The application works with the following logical inputs:

- base price
- discount percentage
- VAT percentage
- tip percentage

The required calculation flow is:

1. apply discount
2. apply VAT to the discounted subtotal
3. apply tip to the updated subtotal

The final output includes:

- original price
- discount amount
- subtotal after discount
- VAT amount
- subtotal with VAT
- tip amount
- final total

## Validation Rules

The application validates that:

- the base price is not negative
- the discount percentage is not negative
- the VAT percentage is not negative
- the tip percentage is not negative

If any value is invalid, the program should display a clear message.

## Special Cases Covered

The project is expected to handle:

- 0% discount
- 0% VAT
- 0% tip
- 100% discount
- decimal values

## Python Concepts Used

This project practices the following Python topics:

- basic data types
- variables
- arithmetic operations
- order of operations
- function definition
- function parameters
- return statements
- conditional logic
- clear console output
- modular program organization

## Math Concepts Used

This project uses basic financial and arithmetic concepts such as:

- percentages
- decimal operations
- sequential calculations
- subtotal and total composition
- rate-based calculations

## Project Structure

The minimum structure of the project is:

- main project file
- execution block with test cases
- README file

## Portfolio Value

This project is intended to be portfolio-ready.

It demonstrates:

- problem decomposition
- clean function-based design
- readable logic
- practical mathematical implementation
- a polished beginner project that solves a real-world problem

Suggested portfolio title:

**Basic Financial Calculator in Python: Discounts, VAT, and Tips**

## Future Improvements

Possible future versions of this project could include:

- user input from the console
- repeated calculations in a menu-based flow
- stronger validation rules
- support for multiple products
- export of results to a file
- a graphical user interface

## Status

In progress.

## Author

Nicolas Gula