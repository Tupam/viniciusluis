class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converte uma string de números romanos em um número inteiro.

        A função interpreta uma string contendo números romanos e converte para o valor inteiro correspondente.
        Ela lida com a subtração e adição baseadas nas regras dos números romanos.

        Parâmetros:
        - s (str): String contendo a representação de um número romano.

        Retorna:
        - int: O valor inteiro equivalente ao número romano fornecido.
        """
        # Dicionário dos números romanos
        numero_romano = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        resultado = 0
        valor_ant = 0

        # Percorre cada caractere na string 's'
        for numero in s:
            # Obtém o valor atual do número romano
            valor_atual = numero_romano[numero]
            # Se o valor atual é maior que o valor anterior, subtrai duas vezes o valor anterior e adiciona o valor atual ao resultado
            if valor_atual > valor_ant:
                resultado += valor_atual - 2 * valor_ant
            else:
                # Caso contrário, apenas adiciona o valor atual ao resultado
                resultado += valor_atual
            # Atualiza o valor anterior para o valor atual
            valor_ant = valor_atual

        return resultado

solution = Solution()
print(solution.romanToInt("III"))      #  3
print(solution.romanToInt("LVIII"))    #  58
print(solution.romanToInt("MCMXCIV"))  # 1994 
