#include <bit/stdc++.h>
using namespace std;

int binSearch (int ar[], int n, int x) {
	int l = 1, r = n;
	while (l <= r) {
		int m = l + (r - l)/2;
		if (ar[m] == x) return m;
		else if (ar[m] < x) l = m + 1;
		else r = m - 1;
	}
}

/*
	To find first x for which f(x) is true
*/

int first (int l, int r) {
	while (l < r) {
		int m = l + (r - l)/2;
		if (f(m) == true) r = m;
		else l = m + 1;
	}
	if (f(l) == false) // complain
	return l;
}

/*
	To find last x for which f(x) is false
*/

int last (int l, int r) {
	while (l < r) {
		int m = l + (r - l + 1)/2;	// To avoid an division truncation bug
		if (f(m) == true) r = m - 1;
		else l = m;
	}
	if (f(l) == true) // complain
	return l;
}

int main () {
	return 0;
}