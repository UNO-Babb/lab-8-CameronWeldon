#ProcessData.py
#Name: Cameron Weldon
#Date:
#Assignment: Lab 8

import random

def main():

  # Open
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  # Write csv
  outFile.write("Last Name,First Name,UserID,Major-Year\n")

  # output to csv
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    year = data[5]
    major = data[6]

    student_id = makeID(first, last, idNum)

    # major and year
    year_abbrev = convertYear(year)
    major_abbrev = major[:3].upper()
    major_year = major_abbrev + "-" + year_abbrev

    # Write to CSV
    output = last + "," + first + "," + student_id + "," + major_year + "\n"
    outFile.write(output)

  
  inFile.close()
  outFile.close()


def makeID(first, last, idNum):
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "X"

  id = first[0].lower() + last.lower() + idNum[idLen - 3:]
  return id


def convertYear(year):
  year_map = {
    "Freshman": "FR",
    "Sophomore": "SO",
    "Junior": "JR",
    "Senior": "SR"
  }
  return year_map.get(year, "UN")  # Use "UN" for unknown


if __name__ == '__main__':
  main()
