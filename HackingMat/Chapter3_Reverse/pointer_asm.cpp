#include <stdio.h>

int inc(int* a)
{
	*a = *a + 1;
	return *a;
}

int pointer_asm()
{
	int s, ret;
	s = 2;
	ret = inc(&s);
	printf("%d, %d \n", s, ret);

	return 0;
}