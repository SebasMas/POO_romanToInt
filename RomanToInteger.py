class Solution(object):
    def RomanToInteger(self, x):
        """
        :type x: str
        :rtype: int
        """
        romanos = {"I": 1, "V": 5, "X": 10,  "L": 50, "C": 100, "D": 500, "M": 1000}
        
        # Revisamos si el valor ingresado es válido dentro de nuestro diccionario
        if all(i in romanos for i in x):
            # Establecemos unas variables iniciando en 0 para guardar los resultados de las operaciones
            resultado = 0
            prev_value = 0
            
            # Recorremos cada valor de la cadena x desde el último índice
            for i in x[::-1]:
                # La variable value será igual al valor que contenga i dentro de romanos
                value = romanos[i]
                
                # Si el valor es mayor o igual al valor anterior, entonces se suma
                if value >= prev_value:
                    resultado += value
                else:
                    resultado -= value
                
                # La variable prev_value es igual al valor actual de la lista (recorriendo desde el último valor)
                prev_value = value
            
            return resultado
        else:
            print("Ingresaste un romano inválido!!!")
            
#Al crear una instancia de la clase dentro de una variable, evitamos que, cambios que hagamos, se guarden en la clase global y así podamos darle usos personalizados.
solution = Solution()
x = input("Ingrese un número romano: ") #Creamos la variable que se usará en la función
print(solution.RomanToInteger(x)) # Llamamos la función