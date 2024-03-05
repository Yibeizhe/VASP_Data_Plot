import numpy as np

# 定义模拟参数
L = 10  # 晶格边长
J = 1.0  # 交换耦合常数
temperature_range = np.linspace(1, 10, 10)  # 温度范围
num_cycles = 10000  # 模拟循环次数

# 初始化自旋状态
spins = np.random.choice([-1, 1], size=(L, L))


# 计算总能量
def calculate_total_energy(spins):
    energy = 0
    for i in range(L):
        for j in range(L):
            energy += -J * spins[i, j] * (spins[(i + 1) % L, j] + spins[i, (j + 1) % L])
    return energy


# 进行蒙特卡罗模拟循环
for temperature in temperature_range:
    energies = []

    for _ in range(num_cycles):
        # 随机选择一个晶格点
        i, j = np.random.randint(0, L, size=2)

        # 计算能量差
        delta_energy = 2 * J * spins[i, j] * (spins[(i + 1) % L, j] + spins[i, (j + 1) % L] +
                                              spins[(i - 1) % L, j] + spins[i, (j - 1) % L])

        # 根据Metropolis准则接受或拒绝状态转移
        if delta_energy <= 0 or np.random.random() < np.exp(-delta_energy / temperature):
            spins[i, j] *= -1

        energies.append(calculate_total_energy(spins))

    # 计算能量的平均值
    average_energy = np.mean(energies)

    # 计算居里温度
    curie_temperature = abs(average_energy) / (2 * J * L * L)

    print(f"Temperature: {temperature}, Curie Temperature: {curie_temperature}")
