price_per_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
starting_bullets = len(bullets)
locks = [int(x) for x in input().split()]
value_of_intelligence = int(input())

gun_barrel = 0
finished = True

while locks:
    # check for bullets left
    if bullets:
        current_bullet = bullets.pop()
    else:
        print(f"Couldn't get through. Locks left: {len(locks)}")
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
else:
    earned = value_of_intelligence - ((starting_bullets - len(bullets)) * price_per_bullet)
    print(f'{len(bullets)} bullets left. Earned ${earned}')