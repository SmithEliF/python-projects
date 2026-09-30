letter_file = open('mail-merge/input/letters/starting_letter.txt')
letter = letter_file.read()
names_file = open('mail-merge/input/names/invited_names.txt')
names = names_file.readlines()

for name in names:
    name = name.strip()
    with open(f"/mail-merge/output/ready-to-send/letter_for_{name}.txt", mode="w") as output_letter:
        letter.replace("[name]", name)
        output_letter.write(letter)


output_letter.close()
names_file.close()
letter_file.close()