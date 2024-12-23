import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configuração inicial
sequence = "AGCTGAC"
base_order = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
colors = {'A': 'blue', 'C': 'green', 'G': 'orange', 'T': 'red'}

# Converter sequência para números e cores
numeric_seq = [base_order[base] for base in sequence]
color_seq = [colors[base] for base in sequence]

# Função para contar inversões e gerar passos
def get_inversion_steps(arr):
    steps = []
    def merge_and_record(left, right, indices):
        i = j = 0
        merged = []
        local_steps = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                local_steps.extend([(indices[i], indices[i + len(left)])])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, local_steps


    def merge_sort_and_track(arr, indices):
        if len(arr) <= 1:
            return arr, []
        mid = len(arr) // 2
        left, left_steps = merge_sort_and_track(arr[:mid], indices[:mid])
        right, right_steps = merge_sort_and_track(arr[mid:], indices[mid:])
        merged, merge_steps = merge_and_record(left, right, indices)
        return merged, left_steps + right_steps + merge_steps

    _, steps = merge_sort_and_track(arr, list(range(len(arr))))
    return steps

# Gerar passos de troca
inversion_steps = get_inversion_steps(numeric_seq)

# Configurar gráfico
fig, ax = plt.subplots()
bars = ax.bar(range(len(sequence)), numeric_seq, color=color_seq)

# Atualizar gráfico
def update(frame):
    if frame >= len(inversion_steps):
        return
    i, j = inversion_steps[frame]
    numeric_seq[i], numeric_seq[j] = numeric_seq[j], numeric_seq[i]
    bars[i].set_height(numeric_seq[i])
    bars[j].set_height(numeric_seq[j])
    bars[i].set_color(color_seq[j])
    bars[j].set_color(color_seq[i])
    color_seq[i], color_seq[j] = color_seq[j], color_seq[i]


# Criar animação
ani = FuncAnimation(fig, update, frames=len(inversion_steps), interval=500, repeat=False)

# Salvar animação em um arquivo (opcional)
try:
    ani.save('animation.mp4', writer='ffmpeg')
except Exception as e:
    print(f"Erro ao salvar a animação: {e}")


# Mostrar gráfico
plt.xlabel("Posição na sequência")
plt.ylabel("Valor base (A=1, C=2, G=3, T=4)")
plt.title("Animação de Desordem na Sequência Biológica")

# Forçar exibição no ambiente não interativo (se for compatível)
plt.savefig('output_plot.png')  # Salvar o gráfico em um arquivo
plt.show()

