from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Encontra os índices de dois números em uma lista que somam um valor alvo.

        Dado uma lista de números inteiros e um valor alvo, a função procura dois números na lista 
        cuja soma seja igual ao valor alvo. Retorna uma lista contendo os índices desses dois números.

        Parâmetros:
        - nums (List[int]): Lista de números inteiros.
        - target (int): O valor alvo que queremos alcançar com a soma de dois números.

        Retorna:
        - List[int]: Lista com dois índices, onde os números nos índices somam o valor alvo.
          Se não houver tal par, retorna uma lista vazia.
        """
        # Cria um dicionário para armazenar os números e seus índices
        num_indices = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                # Encontramos a solução
                return [num_indices[complement], i]
            num_indices[num] = i

        # Se não houver solução, retorna uma lista vazia
        return []



solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Deve retornar [0, 1]
print(solution.twoSum([3, 2, 4], 6))       # Deve retornar [1, 2]
print(solution.twoSum([3, 3], 6))          # Deve retornar [0, 1]
