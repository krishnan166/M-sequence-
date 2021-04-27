import random


## Function that generates m-sequence
def m_sequence_generator(polynomial):
	m = polynomial[0]
	N = ((2 ** m) - 1)
	## Generating initial seed and ensuring all 0 values are not generated
	while (1):
		for i in range(random.randint(5, 10)):
			initial_seed = []
			for j in range(m):
				initial_seed.append(random.randint(0, 1))
		if initial_seed != [0] * m:
			break
		else:
			continue
	m_seq = str(initial_seed[-1])
	iter_seq = initial_seed
	## Taking output after adding and shifting the iter_seq
	for i in range(1, N):
		s = 0
		for j in polynomial[1:]:
			s += iter_seq[j]
		s = s % 2
		iter_seq = iter_seq[:-1]
		iter_seq = [s] + iter_seq
		m_seq += str(iter_seq[-1])
	print("Initial Seed : ", ''.join(map(str, initial_seed)))
	return (m_seq[::-1])

## Function that generates gold codes
def gold_codes_generator(m1, m2):
	print('Gold Code:')
	print('1:', m1)
	print('2:', m2)
	n = len(m1)
	## shifting and XORing second m-seq with first m-seq
	for i in range(n):
		gc = bin(int(m1, 2) ^ int(m2, 2))[2:]
		gc = '0' * (n - len(gc)) + gc
		print(f"{i + 3}:", gc)
		m2 = m2[1:] + m2[0]
	return 1


if __name__ == '__main__':

	while (1):
		print("1. Generate Gold Codes")
		print("2. Exit")
		try:
			choice = int(input("Select choice (1 or 2): "))
			if choice == 2:
				break
			elif choice == 1:
				while (1):
					print("")
					print("")
					print("Enter a preferred pair")
					polynomial1 = input("Input 1st polynomial : ")
					poly1 = list(map(int, polynomial1.split(' ')))
					polynomial2 = input("Input 2nd polynomial : ")
					poly2 = list(map(int, polynomial2.split(' ')))
					checkp1 = poly1.copy()
					checkp1.sort()
					checkp2 = poly2.copy()
					checkp2.sort()
					print(poly1)
					print(poly2)
					if poly1 != checkp1[::-1] or poly2 != checkp2[::-1]:
						print("Incorrect order of exponents.")
						print("Order should be descending order.")
						print("")
						continue
					elif poly1[0] != poly2[0]:
						print("Inputs should generate same length m-sequence")
						print("")
						continue
					elif poly1[0] > 11 or poly1[0] < 3:
						print("Out of bounds: Please enter polynomial with degree between 5 and 11")
						print("")
						print
						continue
					else:
						print("")
						m1 = m_sequence_generator(poly1)
						m2 = m_sequence_generator(poly2)
						sgc = gold_codes_generator(m1, m2)

			else:
				print("Enter value 1 or 2")
				print("")
				continue
		except ValueError as e:
			print("ValueError: ", e)
			print("")
			continue