# 42. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def compression_module():
    with open('in.txt') as f:
        lst = f.read()
        print(f'Исходная строка:     {lst}')
    i = 0
    result = ''
    while i < len(lst):
        counter = 1
        while i + 1 < len(lst) and lst[i] == lst[i + 1]:
            counter += 1
            i += 1
        result += str(counter) + lst[i]
        i += 1
    with open('out.rle', 'w') as f:
        f.write(result)
    print(f'Строка после сжатия: {result}')
    return result


def decompression_module():
    with open('out.rle') as f:
        lst = f.read()
    print(f'Исходная строка:         {lst}')
    result = ''
    for i in range(0, len(lst), 2):
        result += int(lst[i]) * lst[i + 1]
    with open('in.txt', 'w') as f:
        f.write(result)
    print(f'Строка после распаковки: {result}')
    return result


def main():
    compression_module()
    decompression_module()


if __name__ == '__main__':
    main()

