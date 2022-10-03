price_per_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = input().split()
bullets = [int(x) for x in bullets]
starting_bullets = len(bullets)
locks = input().split()
locks = [int(x) for x in locks]
value_of_intelligence = int(input())

gun_barrel = 0
finished = True

while locks:
    # check for bullets left
    if bullets:
        current_bullet = bullets.pop(-1)
    else:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        finished = False
        break
    # take new lock
    current_lock = locks.pop(0)
    # fill gun barrel
    gun_barrel += 1

    if current_bullet > current_lock:
        print("Ping!")
        locks.insert(0, current_lock)
    elif current_bullet <= current_lock:
        print("Bang!")

    # check for reloading
    if gun_barrel == size_of_gun_barrel and bullets:
        print("Reloading!")
        gun_barrel = 0

if finished:
    earned = value_of_intelligence - ((starting_bullets - len(bullets)) * price_per_bullet)
    print(f'{len(bullets)} bullets left. Earned ${earned}')