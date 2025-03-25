
# MaxMin Select

## Descrição do Projeto
O **MaxMin Select** é uma iniciativa acadêmica que tem como objetivo implementar o algoritmo de **seleção do maior e menor elementos** em uma sequência numérica, aplicando a técnica de **divisão e conquista**.

A proposta deste projeto é analisar a eficiência do algoritmo, comparando-o com métodos mais simples e discutindo sua complexidade assintótica.

## Funcionamento do Algoritmo MaxMin Select
O algoritmo **MaxMin Select** é capaz de encontrar o maior e o menor número em uma lista com o menor número possível de comparações, por meio da técnica de **divisão e conquista**.

### **Etapas do Algoritmo**
1. Se a lista tiver **um único item**, este item será tanto o maior quanto o menor.
2. Se houver **dois itens**, é realizada **uma única comparação**.
3. Para **mais de dois itens**, o array é dividido em duas partes.
4. Cada metade é processada recursivamente para encontrar o maior e menor número.
5. As respostas são então combinadas para determinar o maior e o menor número da lista inteira.

## Estrutura do Projeto
A estrutura do projeto está organizada da seguinte forma:

```
📂 maxmin-select
│── main.py          # Implementação do algoritmo MaxMin Select
│── README.md        # Documento explicativo do projeto
│── assets/          # Contém imagens e diagramas explicativos
```

## Ambiente Virtual
Para configurar um ambiente isolado para o projeto, siga as etapas abaixo:

### **Passo 1: Criar e ativar o ambiente virtual**

Use o comando a seguir para criar o ambiente virtual:
```bash
python -m venv venv
```

Para ativá-lo:

- **Windows:**
  ```bash
  venv\Scripts ctivate
  ```

- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### **Passo 2: Instalar as dependências (se houver)**
```bash
pip install -r requirements.txt
```

### **Passo 3: Rodar o algoritmo**
```bash
python main.py
```

## Análise de Complexidade Assintótica
A complexidade do algoritmo **MaxMin Select** pode ser analisada de duas maneiras:

### **1. Contagem das Operações**
- O algoritmo minimiza as comparações dividindo o array em duas partes.
- Em cada nível da recursão, realiza-se apenas **3 comparações por nível**.
- A complexidade total é **O(n)**.

### **2. Aplicação do Teorema Mestre**
A recorrência do algoritmo pode ser expressa por:
```
T(n) = 2T(n/2) + O(1)
```
- **Parâmetros:**
  - `a = 2`
  - `b = 2`
  - `f(n) = O(1)`
- **Cálculo de `log_b(a)`:**
  - `log_2(2) = 1`
- **Resultado:** O(n)

## Diagrama do Algoritmo
O projeto também inclui um **diagrama da árvore de recursão** que ilustra o funcionamento do algoritmo. Este diagrama pode ser encontrado na pasta `assets/diagrama.png` e mostra:

1. Como o problema é quebrado em subproblemas menores.
2. Como esses subproblemas são combinados para gerar a solução final.
3. O número de comparações feitas em cada nível da recursão.

## Exemplo de Entrada e Saída
### **Entrada:**
```python
arr = [ 3, 5, 1, 8, 2, 9, 4, 7, 6]
min_val, max_val = max_min_select(arr, 0, len(arr) - 1)
print(f"Menor elemento: {min_val}, Maior elemento: {max_val}")
```

### **Saída:**
```
Menor elemento: 1, Maior elemento: 9
```
## Licença
Este projeto está licenciado sob a **Licença MIT**. Fique à vontade para usar, modificar e distribuir conforme necessário.

---
