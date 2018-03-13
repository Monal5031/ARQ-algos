#include "bits/stdc++.h"

using namespace std;

int winSize = 0;
int damaged = 0;

void send() {
    for(int i = 0; i < winSize + 1; i++) {
        if (i < damaged) {
            cout << "sent " << i << "\t" << "received " << i << endl;
        }
        else {
            cout << "sent " << i << "\t" << "discarded " << i << endl;
        }
    }
    for (int i = damaged; i < winSize + 1; i++) {
        cout << "sent " << i << "\t" << "received " << i << endl;
    }
}

int main() {
    cout << "Window size : ";
    cin >> winSize;
    cout << "\ndamaged frame (between 0 and " << winSize << ") : ";
    cin >> damaged;
    cout << endl;
    send();

    return 0;
}
