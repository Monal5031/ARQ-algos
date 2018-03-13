from SelectiveRepeat.data import *


def search(idx, failed):
    for i in range(len(failed)):
        if idx is failed[i][0]:
            # print(i)
            return i


def send_packet_to_receiver(packets: list):
    failed = []
    for i in range(len(packets)):
        if packets[i][1] is False:
            failed.append(packets[i][0])
    print('Failed Packets:', failed)
    return failed


def sender(packets: list):
    failed_packets = send_packet_to_receiver(packets)
    failed = []
    for i in failed_packets:
        failed.append((i, False))
    corrected = randint(1, 4)
    for i in failed_packets:
        if corrected == 0:
            break
        elif corrected != 0:
            failed_pos = search(i, failed)
            if failed_pos is not None:
                failed[failed_pos] = (i, True)
            corrected -= 1
    return failed


def print_sent_packets(sent: list):
    print('We sent:', end=' ')
    sent_new = []
    for i in sent:
        sent_new.append(i[0])
    print(sent_new)


def main():
    sent = error_packets
    while len(sent) > 0:
        print_sent_packets(sent)
        # print('Sent packet:', sent)
        sent = sender(sent)
        print()


if __name__ == '__main__':
    main()