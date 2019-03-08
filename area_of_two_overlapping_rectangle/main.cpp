/**
 * main.cpp
 *  area of two overlapping rectangles
 *  Created on: 6 Nov 2016
 *      Author: Kaz
**/
#include <stdio.h>
#include <algorithm>
#include <math.h>

using namespace std;

int M(int K, int L, int M, int N, int P, int Q, int R, int S) {
	int SI, SA, SB;

	SA = (M - K) * (N - L);
	SB = (R - P) * (S - Q);
	SI = max(0, min(M, R) - max(K, P)) * max(0, min(N, S) - max(L, Q));
	return SA+SB-SI;
}

int main() {
	int area;
	area = M(1, 1, 2, 2, 3, 3, 4, 4);
	printf("MN : 1, 1, 2, 2\tAB : 3, 3, 4, 4 = %i\n", area); //2

	area = M(1, 1, 3, 3, 1, 1, 3, 3);
	printf("MN : 1, 1, 3, 3\tAB : 1, 1, 3, 3 = %i\n", area); //4

	area = M(1, 1, 2, 2, 1, 1, 3, 3);
	printf("MN : 1, 1, 2, 2\tAB : 1, 1, 3, 3 = %i\n", area); //4

	area = M(5, 5, 6, 6, 1, 1, 7, 7);
	printf("MN : 5, 5, 6, 6\tAB : 1, 1, 7, 7 = %i\n", area); //36

	area = M(1, 1, 2, 10, 1, 1, 10, 2);
	printf("MN : 1, 1, 2, 10\tAB : 1, 1, 10, 2 = %i\n", area); //17

	area = M(-4, 1, 2, 6, 0, -1, 4, 3);
	printf("MN : -4, 1, 2, 6\tAB : 0, -1, 4, 3 = %i\n", area); //42

	return 0;
}

