import random

def main():

	print("Randomizer!")

	numberOfGroups = int(input("Input number of groups: "))
	peoplePerGroup = int(input("Input amount of people per group: "))
	nameList = []

	nameList = namebuilder(nameList)
	groupbuilder(peoplePerGroup, numberOfGroups, nameList)


def namebuilder(nameList):
	name = ''
	name = input("Enter names, type 'done' when finished: ")
	while name.lower() != 'done':
		nameList.append(name)
		name = input("Enter names, type 'done' when finished: ")

	random.shuffle(nameList)
	return nameList


def groupbuilder(peoplePerGroup, numberOfGroups, nameList):
	ct = 1
	start = 0
	move = peoplePerGroup
	while ct < numberOfGroups + 1:
		print("Group", ct)
		print(nameList[start:move])
		start += peoplePerGroup
		move += peoplePerGroup
		ct += 1

main()