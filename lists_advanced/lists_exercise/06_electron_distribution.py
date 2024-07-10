count_electron = int(input())
def distribute_electrons(count_electron):
    shells = []
    n = 1
    while count_electron > 0:
        max_electrons_in_shell = 2 * n * n
        if count_electron >= max_electrons_in_shell:
            shells.append(max_electrons_in_shell)
            count_electron -= max_electrons_in_shell
        else:
            shells.append(count_electron)
            count_electron = 0
        n += 1
    return shells

filled_shells = distribute_electrons(count_electron)
print(filled_shells)