from Bio.Seq import Seq
from colorama import init, Fore, Style
import time
from visualizer import Visualizer

init(autoreset=True)

BASE_TO_NUM = {"A": 1, "C": 2, "G": 3, "T": 4, "U": 4}
NUM_TO_BASE = {1: "A", 2: "C", 3: "G", 4: "T"}


def print_step(message, arr, visualizer, left_idx=None, right_idx=None, merged=None):
    """Imprime um passo da ordenação com visualização gráfica."""

    bases = [NUM_TO_BASE[num] for num in arr]

    visualizer.show_sorting_steps(message, bases, arr, left_idx, right_idx, merged)

    print(f"\n{message}")

    result_bases = "Bases:  "
    result_nums = "Números:"
    for i, num in enumerate(arr):

        base = NUM_TO_BASE[num]

        if merged is not None and num in merged:
            color = Fore.GREEN
        elif left_idx is not None and i <= left_idx:
            color = Fore.YELLOW
        elif right_idx is not None and left_idx is not None and i > left_idx:
            color = Fore.BLUE
        else:
            color = Fore.WHITE

        result_bases += f"{color}{base} "
        result_nums += f"{color}{num} "

    print(result_bases)
    print(result_nums)
    time.sleep(0.5)


def merge_and_count(left, right, visualizer, full_array, start_idx):
    """Merge com visualização."""
    i = j = inv_count = 0
    merged = []

    print_step(
        "Mesclando subarrays:",
        full_array,
        visualizer,
        left_idx=start_idx + len(left) - 1,
        right_idx=start_idx + len(left) + len(right) - 1,
    )

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv_count += len(left) - i
            print_step(
                f"Inversão encontrada! ({inv_count} inversões até agora)",
                full_array,
                visualizer,
                merged=merged,
            )

    merged.extend(left[i:])
    merged.extend(right[j:])

    print_step(
        "Array mesclado e ordenado:",
        merged + full_array[start_idx + len(merged) :],
        visualizer,
        merged=merged,
    )

    return merged, inv_count


def merge_sort_and_count(arr, visualizer, full_array=None, start_idx=0):
    """Merge sort com visualização."""
    if full_array is None:
        full_array = arr.copy()

    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    print_step(
        f"Dividindo array no índice {mid}:",
        full_array,
        visualizer,
        left_idx=start_idx + mid - 1,
    )

    left, left_inv = merge_sort_and_count(arr[:mid], visualizer, full_array, start_idx)
    right, right_inv = merge_sort_and_count(
        arr[mid:], visualizer, full_array, start_idx + mid
    )
    merged, merge_inv = merge_and_count(left, right, visualizer, full_array, start_idx)

    full_array[start_idx : start_idx + len(merged)] = merged
    return merged, left_inv + right_inv + merge_inv


def calculate_disorder(seq):
    """Calcula o grau de desordem de uma sequência biológica com visualização."""

    vis = Visualizer()

    print(f"{Fore.CYAN}Sequência original: {seq}{Style.RESET_ALL}")

    numeric_seq = [BASE_TO_NUM[base] for base in seq if base in BASE_TO_NUM]

    print(
        f"\n{Fore.YELLOW}Iniciando ordenação e contagem de inversões...{Style.RESET_ALL}"
    )
    _, inversions = merge_sort_and_count(numeric_seq, vis)

    n = len(numeric_seq)
    max_inversions = n * (n - 1) // 2
    disorder_index = (inversions / max_inversions) if max_inversions > 0 else 0

    print(f"\n{Fore.GREEN}Resultados finais:{Style.RESET_ALL}")
    print(f"Número de inversões: {inversions}")
    print(f"Índice de desordem: {disorder_index:.2%}")

    return inversions, disorder_index


if __name__ == "__main__":
    from visualizer import Visualizer

    vis = Visualizer()
    sequence = vis.get_sequence()
    seq = Seq(sequence)
    inversions, disorder_index = calculate_disorder(seq)
    vis.show_results(inversions, disorder_index)
