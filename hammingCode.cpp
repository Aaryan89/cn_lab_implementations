#include <iostream>
#include <vector>
using namespace std;

void encode4BitDataUsingHammingCode(int bin, int len) {
    vector<int> arr(len, 0);
    //arr[6] = -1, arr[5] = -1, arr[3] = -1;
    arr[4] = bin%10; bin /= 10;
    arr[2] = bin%10; bin /= 10;
    arr[1] = bin%10; bin /= 10;
    arr[0] = bin%10; bin /= 10;

    int p1 = arr[0] + arr[2] + arr[4]; if(p1%2 == 1) arr[6] = 1;
    int p2 = arr[0] + arr[1] + arr[4]; if(p2%2 == 1) arr[5] = 1;
    int p3 = arr[0] + arr[1] + arr[2]; if(p3%2 == 1) arr[3] = 1;

    int ans = 0;
    for(int i = 0; i < 7; i++) {
        ans += arr[i]; ans *= 10;
    } ans /= 10;
    cout << "The final transmitted codeword is: " << ans;

    int cBit;
    cout << "Enter the bit you want to currupt: (-1 for clean) : "; cin >> cBit;
    // flip bit
    if(cBit == -1) cout << "No changes" << endl;
    else {
        arr[7 - cBit] = 1 - arr[7 - cBit];
        int ans = 0;
        for(int i = 0; i < 7; i++) {
            ans += arr[i]; ans *= 10;
        } ans /= 10;
        cout << "The final transmitted codeword WITH ERROR is: " << ans;
    }
}

int main() {
    int num;
    cout << "Enter a number: "; cin >> num;
    if(num > 16 || num < 8) {
        cout << "we need 4-bit number with no 0 as MSB: "; cin >> num;
    }

    // represent the num into its binary representation.
    int bNum = 0;
    int place = 1;
    for(int i = 0; i < 4; i++) {
        int bit = (num >> i) & 1;
        bNum += bit * place;
        place *= 10;
    }
    cout << "binary representation: " << bNum << endl;

    // calculate r
    int m = 4, r = 0;
    while((1 << r) < (m + r + 1)) r++;
    cout << "Value of r (i.e., no. of parity bits) is: " << r << endl;

    // total length of the codeword
    int len = m+r;
    cout << "Total length of codeword: " << len << endl;
    encode4BitDataUsingHammingCode(bNum, len);
    return 0;
}


