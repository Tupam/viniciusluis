from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove todas as ocorrências de um valor específico de uma lista e retorna o novo comprimento da lista.

        A função percorre a lista `nums`, removendo todas as ocorrências do valor `val` e reorganiza a lista para 
        que os elementos restantes fiquem no início da lista. O comprimento da lista resultante é retornado, 
        e o conteúdo da lista `nums` é modificado in-place para refletir a remoção dos valores.

        Parâmetros:
        - nums (List[int]): Lista de números inteiros que pode conter o valor a ser removido.
        - val (int): Valor a ser removido da lista.

        Retorna:
        - int: O novo comprimento da lista após a remoção dos valores iguais a `val`. Os primeiros `k` elementos da 
          lista `nums` contêm os valores restantes, onde `k` é o valor retornado.
        """
        # Contador para armazenar o índice dos elementos que não são iguais a 'val'
        k = 0

        # Percorre a lista lendo cada valor
        for i in range(len(nums)):
            if nums[i] != val:
                # Se o número não for igual a 'val', coloca-o na posição 'k'
                nums[k] = nums[i]
                # Incrementa o contador
                k += 1

        return k


solution = Solution()
nums1 = [3, 2, 2, 3]                       # Lista com os numeros
val1 = 3                                   # Numero selecionado para busca
print(solution.removeElement(nums1, val1)) # Apresenta quantidade de valores diferente do selecionado

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
print(solution.removeElement(nums2, val2))
