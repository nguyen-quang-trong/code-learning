import csv
import random
import os

def LuuFile(duongdan):
    with open(duongdan, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        for i in range(10):
            dong = []

            for j in range(10):
                dong.append(random.randint(1, 100))

            writer.writerow(dong)

def DocFile(duongdan):
    with open(duongdan, 'r') as file:
        reader = csv.reader(file, delimiter=';')

        for row in reader:
            tong = 0

            for value in row:
                tong += int(value)

            print("Tổng:", tong)

def main():
    duongdan = os.path.join(
        os.path.dirname(__file__),
        "dulieu.csv"
    )

    LuuFile(duongdan)
    DocFile(duongdan)


if __name__ == "__main__":
    main()