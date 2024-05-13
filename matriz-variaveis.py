#Atividade em grupo
#Alunos: Gustavo Fernando Mastrocollo Gea - RA 623201135
#        Guilherme Paiva Flora            - RA 623200498

import numpy as np
from scipy.linalg import inv, det

#Definindo a matriz
Matriz = np.array([[1, 2, 3, 4, 5],
                   [7, -2, -6, 1, -2],
                   [4, 5, -3, 3, 9],
                   [4, 6, 7, 2, -1],
                   [8, -8, 8, -8, 9]])

# Item 1. da atividade: Inversa da matriz M
inversa_M = inv(Matriz)
print("1. Inversa da matriz M:\n", inversa_M)

# Item 2. da atividade: Transposta da matriz M
transposta_M = np.transpose(Matriz)
print("\n2. Transposta da matriz M:\n", transposta_M)

# Item 3. da atividade: Determinante da matriz M para a terceira ordem
determinante_M = det(Matriz)
print("\n3. Determinante da matriz M para a terceira ordem:", determinante_M)

# Item 4. da atividade: Máximo, mínimo, soma, média, variância e desvio padrão
max_M = np.max(Matriz)
min_M = np.min(Matriz)
soma_M = np.sum(Matriz)
media_M = np.mean(Matriz)
variancia_M = np.var(Matriz)
desvio_padrao_M = np.std(Matriz)
print("\n4. Máximo:", max_M)
print("   Mínimo:", min_M)
print("   Soma:", soma_M)
print("   Média:", media_M)
print("   Variância:", variancia_M)
print("   Desvio padrão:", desvio_padrao_M)

# Item 5. da atividade: Valores da Diagonal Principal da matriz M
diagonal_principal = np.diag(Matriz)
print("\n5. Valores da Diagonal Principal da matriz M:", diagonal_principal)

# Item 6. da atividade: Valores da Diagonal Secundária da matriz M
diagonal_secundaria = np.diag(np.fliplr(Matriz))
print("\n6. Valores da Diagonal Secundária da matriz M:", diagonal_secundaria)

# Item 7. da atividade: Somatório da Diagonal Principal da matriz M
somatorio_diagonal_principal = np.trace(Matriz)
print("\n7. Somatório da Diagonal Principal da matriz M:", somatorio_diagonal_principal)

# Item 8. da atividade: Somatório da Diagonal Secundária da matriz M
somatorio_diagonal_secundaria = np.trace(np.fliplr(Matriz))
print("\n8. Somatório da Diagonal Secundária da matriz M:", somatorio_diagonal_secundaria)
