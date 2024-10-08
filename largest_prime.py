#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!

import argparse
from fibonnaci import fib_num

def is_prime(num):
	if num <= 1:
		return False
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return False
	return True

def largest_prime_fib(limit):
	fib_sequence = fib_num(limit)
	largest_prime = [num for num in fib_sequence if is_prime(num)]
	if largest_prime:
		return max(largest_prime)
	else: 
		return None

def main():
	parser = argparse.ArgumentParser(description="Find the largest prime Fibonacci number less than a number.")
	parser.add_argument('limit', type=int, help="Upper limit for Fibonacci numbers")
	args = parser.parse_args()
	largest_prime = largest_prime_fib(args.limit)
	if largest_prime_fib:
		print(f"The largest prime Fibonacci number less than {args.limit} is: {largest_prime}")
	else:
		print(f"No prime Fibonacci numbers found less than {args.limit}.")

if __name__ == "__main__":
	main()

