from Bio.Seq import Seq

def count_inversions(arr):
    """Conta o número de inversões em um array usando Merge Sort."""
    def merge_and_count(left, right):
        i = j = inv_count = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inv_count += len(left) - i  # Contar inversões
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_count

    def merge_sort_and_count(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, left_inv = merge_sort_and_count(arr[:mid])
        right, right_inv = merge_sort_and_count(arr[mid:])
        merged, merge_inv = merge_and_count(left, right)
        return merged, left_inv + right_inv + merge_inv

    _, total_inversions = merge_sort_and_count(arr)
    return total_inversions

def calculate_disorder(seq):
    """Calcula o grau de desordem de uma sequência biológica."""
    # Converter bases para valores ordenáveis
    base_order = {'A': 1, 'C': 2, 'G': 3, 'T': 4, 'U': 4}
    numeric_seq = [base_order[base] for base in seq if base in base_order]

    # Contar inversões
    inversions = count_inversions(numeric_seq)

    # Calcular o número máximo de inversões possível
    n = len(numeric_seq)
    max_inversions = n * (n - 1) // 2

    # Calcular índice de desordem (percentual)
    disorder_index = (inversions / max_inversions) if max_inversions > 0 else 0

    return inversions, disorder_index

# Exemplo de uso
seq = Seq("AGCTGAC")
inversions, disorder_index = calculate_disorder(seq)
print(f"Sequência: {seq}")
print(f"Número de inversões: {inversions}")
print(f"Índice de desordem: {disorder_index:.2%}")
