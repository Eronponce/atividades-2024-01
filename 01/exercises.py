# Exercicio 01

def max_consecutive_sum(nums):  
    best_sum = -100000
    temp_sum = 0
    for i in range(0, len(nums)):
        temp_sum = temp_sum + nums[i]
        if (best_sum < temp_sum):
            best_sum = temp_sum
        if temp_sum < 0:
            temp_sum = 0
    return best_sum 


# Testes 01


def test_max_consecutive_sum():
    print(max_consecutive_sum([1, -3, 2, 1, -1]) == 3)
    print(max_consecutive_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
    print(max_consecutive_sum([5, -1, -2, 3, -1, 2, -4]) == 7)
    print(max_consecutive_sum([1]) == 1)
    print(max_consecutive_sum([-1, -2, -3, -4, -5]) == -1)


# Exercício 02
def is_palindrome(word):
    inverse_word = word[::-1]
    if (word == inverse_word):
        return True
    else:
        return False

# Testes 02


def text_is_palindrome():
    print(is_palindrome("radar") == True)
    print(is_palindrome("racecar") == True)
    print(is_palindrome("level") == True)
    # Testes negativos
    print(is_palindrome("python") == False)
    print(is_palindrome("hello") == False)
    print(is_palindrome("12321") == False)
    print(is_palindrome("abccbaa") == False)


# Exercício 03
def count_increasing_subsets(nums):
    temp_sum = 0
    for first_num in range(len(nums)):
        length = 1
        for j in range(first_num + 1, len(nums)):
            if nums[j] > nums[j - 1]:
                length += 1
            else:
                break
        temp_sum += (length * (length + 1)) // 2
    return temp_sum

# Testes 03


def test_count_increasing_subsets():
    # Teste com lista vazia
    print(count_increasing_subsets([]) == 0)
    # Teste com uma lista de um elemento
    print(count_increasing_subsets([1]) == 1)
    # Teste com uma lista de números aleatórios
    print(count_increasing_subsets([1, 3, 2, 4]) == 8)
    # Teste com uma lista de números ordenados
    print(count_increasing_subsets([1, 2, 3, 4, 5]) == 31)
    # Teste com uma lista de números em ordem decrescente
    print(count_increasing_subsets([5, 4, 3, 2, 1]) == 0)
    # Teste com uma lista contendo números repetidos
    print(count_increasing_subsets([1, 2, 2, 3, 3, 3, 4]) == 16)


# Run the tests
if __name__ == "__main__":
    test_max_consecutive_sum()
    text_is_palindrome()
    test_count_increasing_subsets()
