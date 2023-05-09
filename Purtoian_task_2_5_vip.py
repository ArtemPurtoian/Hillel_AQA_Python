vip_room_guests = ['Anna', 'Bob', 'Chris', 'David']
common_room_guests = {'Suzan', 'Martin', None, None}

common_room_guests.discard(None)

print(tuple(vip_room_guests))
print(common_room_guests)
