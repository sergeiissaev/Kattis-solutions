#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    float N, a;
    cin >> N;
    a = pow(10, (log10(N) / N));
    cout << a;
}

