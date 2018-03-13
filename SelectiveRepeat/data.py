from random import randint


total_packets = randint(30, 100)
window_size = randint(5, total_packets // 2)
error_packets = []
sent_packets = [False] * total_packets
received_packets = [False] * total_packets

for _ in range(total_packets):
    tmp = True if randint(1, 10) % 2 is 0 else False
    error_packets.append((_, tmp))

print('total_packets', total_packets)
print('window size', window_size)
