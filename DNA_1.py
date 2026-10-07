#!/usr/bin/python3
while True:
    dna = input("Введите последовательность ДНК: ").strip().upper()
    valid = True
    for i in dna:
        if i not in ['A', 'T', 'G', 'C']:
            valid = False
            break
    if dna and valid:
        break
    print("Ошибка! Только символы A, T, G, C.")

nucleotides = ['A', 'T', 'G', 'C']
counts = [0, 0, 0, 0]
for i in dna:
    for j in range(4):
        if i == nucleotides[j]:
            counts[j] += 1
            break

print("\nКоличество нуклеотидов:")
for i in range(4):
    print(f"  {nucleotides[i]}: {counts[i]}")
print(f"  Всего: {len(dna)}")

def complementary(seq):
    orig = ['A', 'T', 'G', 'C']
    comp = ['T', 'A', 'C', 'G']
    res = []
    for i in seq:
        for j in range(4):
            if i == orig[j]:
                res.append(comp[j])
                break
    return ''.join(res)
comp = complementary(dna)
print("\nКомплементарная цепочка:")
print(' '.join(dna))
print(' '.join(['|'] * len(dna)))
print(' '.join(comp))
def find(dna, sub):
    sub_len = len(sub)
    positions = []
    for i in range(len(dna) - sub_len + 1):
        if dna[i:i + sub_len] == sub:
            positions.append(i)    
    if not positions:
        return None    
    result = []
    i = 0
    while i < len(dna):
        if dna[i:i + sub_len] == sub:
            result.append('[' + sub + ']')
            i += sub_len
        else:
            result.append(dna[i])
            i += 1
    return ''.join(result), len(positions)
sub = input("\nВведите подпоследовательность для поиска: ").strip().upper()
valid_sub = True
for i in sub:
    if i not in ['A', 'T', 'G', 'C']:
        valid_sub = False
        break

if sub and valid_sub:
    res = find(dna, sub)
    if res:
        highlighted, count = res
        print(f"\nНайдено {count} вхождений:")
        print(highlighted)
    else:
        print("Вхождений не найдено.")
elif sub:
    print("Подпоследовательность содержит недопустимые символы.")
