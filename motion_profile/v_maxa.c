#include <math.h>
#include <stdio.h>

double vt = 0.0;
double vn = 0.5;
double at = 0.0;
double an = 0.0;
double amax = 1.12;

/*bool MatInvert(float m[16], float invOut[16]) {
	float inv[16], det;
	int i;
 
	inv[ 0] =  m[5] * m[10] * m[15] - m[5] * m[11] * m[14] - m[9] * m[6] * m[15] + m[9] * m[7] * m[14] + m[13] * m[6] * m[11] - m[13] * m[7] * m[10];
	inv[ 4] = -m[4] * m[10] * m[15] + m[4] * m[11] * m[14] + m[8] * m[6] * m[15] - m[8] * m[7] * m[14] - m[12] * m[6] * m[11] + m[12] * m[7] * m[10];
	inv[ 8] =  m[4] * m[ 9] * m[15] - m[4] * m[11] * m[13] - m[8] * m[5] * m[15] + m[8] * m[7] * m[13] + m[12] * m[5] * m[11] - m[12] * m[7] * m[ 9];
	inv[12] = -m[4] * m[ 9] * m[14] + m[4] * m[10] * m[13] + m[8] * m[5] * m[14] - m[8] * m[6] * m[13] - m[12] * m[5] * m[10] + m[12] * m[6] * m[ 9];
	inv[ 1] = -m[1] * m[10] * m[15] + m[1] * m[11] * m[14] + m[9] * m[2] * m[15] - m[9] * m[3] * m[14] - m[13] * m[2] * m[11] + m[13] * m[3] * m[10];
	inv[ 5] =  m[0] * m[10] * m[15] - m[0] * m[11] * m[14] - m[8] * m[2] * m[15] + m[8] * m[3] * m[14] + m[12] * m[2] * m[11] - m[12] * m[3] * m[10];
	inv[ 9] = -m[0] * m[ 9] * m[15] + m[0] * m[11] * m[13] + m[8] * m[1] * m[15] - m[8] * m[3] * m[13] - m[12] * m[1] * m[11] + m[12] * m[3] * m[ 9];
	inv[13] =  m[0] * m[ 9] * m[14] - m[0] * m[10] * m[13] - m[8] * m[1] * m[14] + m[8] * m[2] * m[13] + m[12] * m[1] * m[10] - m[12] * m[2] * m[ 9];
	inv[ 2] =  m[1] * m[ 6] * m[15] - m[1] * m[ 7] * m[14] - m[5] * m[2] * m[15] + m[5] * m[3] * m[14] + m[13] * m[2] * m[ 7] - m[13] * m[3] * m[ 6];
	inv[ 6] = -m[0] * m[ 6] * m[15] + m[0] * m[ 7] * m[14] + m[4] * m[2] * m[15] - m[4] * m[3] * m[14] - m[12] * m[2] * m[ 7] + m[12] * m[3] * m[ 6];
	inv[10] =  m[0] * m[ 5] * m[15] - m[0] * m[ 7] * m[13] - m[4] * m[1] * m[15] + m[4] * m[3] * m[13] + m[12] * m[1] * m[ 7] - m[12] * m[3] * m[ 5];
	inv[14] = -m[0] * m[ 5] * m[14] + m[0] * m[ 6] * m[13] + m[4] * m[1] * m[14] - m[4] * m[2] * m[13] - m[12] * m[1] * m[ 6] + m[12] * m[2] * m[ 5];
	inv[ 3] = -m[1] * m[ 6] * m[11] + m[1] * m[ 7] * m[10] + m[5] * m[2] * m[11] - m[5] * m[3] * m[10] - m[ 9] * m[2] * m[ 7] + m[ 9] * m[3] * m[ 6];
	inv[ 7] =  m[0] * m[ 6] * m[11] - m[0] * m[ 7] * m[10] - m[4] * m[2] * m[11] + m[4] * m[3] * m[10] + m[ 8] * m[2] * m[ 7] - m[ 8] * m[3] * m[ 6];
	inv[11] = -m[0] * m[ 5] * m[11] + m[0] * m[ 7] * m[ 9] + m[4] * m[1] * m[11] - m[4] * m[3] * m[ 9] - m[ 8] * m[1] * m[ 7] + m[ 8] * m[3] * m[ 5];
	inv[15] =  m[0] * m[ 5] * m[10] - m[0] * m[ 6] * m[ 9] - m[4] * m[1] * m[10] + m[4] * m[2] * m[ 9] + m[ 8] * m[1] * m[ 6] - m[ 8] * m[2] * m[ 5];
 
	det = m[0] * inv[0] + m[1] * inv[4] + m[2] * inv[8] + m[3] * inv[12];
 
	if(det == 0)
		return false;
 
	det = 1.f / det;
 
	for(i = 0; i < 16; i++)
		invOut[i] = inv[i] * det;
 
	return true;
}*/
  
int main(int argc, char** argv) {
	double T22=0.0, T11=0.0;
	if (at == 0.0 && an == 0.0) {
		T22 = abs( 3*(vn - v0)/(2*amax) );
	} else {
		T11 = 3*((-vt + vn)*sqrt(9*at*at - at*amax + at*an - 9*at + amax*amax - amax*an) - (vt - at)*(at + amax + an))/(-8*at*at + 3*at*amax + at*an + 9*at + 3*amax*an + an*an);
		T22 = 3*(vt - vn)*(-at - amax - an + sqrt(9*at*at - at*amax + at*an - 9*at + amax*amax - amax*an))/(-8*at*at + 3*at*amax + at*an + 9*at + 3*amax*an + an*an);
	}
	
	double T = T22;
	double m[8] = {1, T, T*T, T*T*T, 0, 1, 2*T, 3*T*T};
	
	printf("T11 = %f\n", T11);
	printf("T22 = %f\n", T22);
	
	double a[4];
	double det =  1./(m[2] * m[7] - m[3] * m[6]);
	
	a[0] = vt;
	a[1] = at;
	a[2] = det*( vt*( -m[0] * m[7] + m[4] * m[3] ) + at*( -m[1] * m[7] + m[3] * m[5] ) + vn*( m[7] ) + an*( -m[3] ) );
	a[3] = det*( vt*( m[0] * m[6] - m[4] * m[2] ) + at*( m[1] * m[6] - m[2] * m[5] ) + vn*( -m[6] ) + an*( m[2] ) );
	
	
	
}
