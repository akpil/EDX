#include <stdio.h>
   int g1 = 6;
   static int g2;

   void trace_me(int p1, int p2, int p3)
   {
     int i;
     int j = 7+p2;
     static int si = 3;
     static int sj;
     printf ("**\n");
     printf ("%d %d\n", p1, p2);

     if ((p1/3)*3 == p1) {
       i = j + 1;
       si--;
       sj = sj + p1 + p2 + p3;
       trace_me(p1-1, p2-1, p3-p2);
       g1 += 2;
       g2 = g2 - p1 - p2 -p3;
       printf("!\n");
     } else {
       if (((p1/3)*3+2) == p1) {
         i = p1;
         g1 -= (p2+p3);
         g2 += (p1 + p2 + p3);
         trace_me(p1-1, p2+1, p2 + p3);
         sj--;
         sj = sj - p1 - p2 -p3;
	 printf("@\n");
       } else {
         i = j + 1;
	 printf("#\n");
         printf("%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n", p1, p2, i, j,
             si, sj, g1, g2);
       }
     }
   }

   int main()
   {
     trace_me(6, 4, 2);
     printf("%d\t%d\n", g1, g2);
     return 0;
   }
