food = [int(x) for x in input().split(",")]
stamina = [int(x) for x in input().split(",")]

peaks = {
    'Vihren': 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan':	60,
    'Kamenitza': 70,
}
conquered_peaks = []

for peak, energy_needed in peaks.items():
    while food and stamina:
        daily_food = food.pop()
        daily_stamina = stamina.pop(0)
        energy = daily_food + daily_stamina
        if energy >= energy_needed:
            conquered_peaks.append(peak)
            break

if len(conquered_peaks) == 5:
    print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')
if conquered_peaks:
    print(f"Conquered peaks:")
    print('\n'.join(conquered_peaks))

