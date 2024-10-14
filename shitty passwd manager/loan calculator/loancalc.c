#include<stdio.h>
#include<time.h>
#include<math.h>
int main()
{
    int amt=0,sta=0;
    int tamt=0,va=0,m,am,u=0;
    float t=0;
    printf("Enter the total amount:");
    scanf("%d",&amt);

    am = amt*6.667;
    am/=100;

    t = amt*0.009334;
    // printf("Enter the starting paying amount: ");
    // scanf("%d",&sta);
    printf("Enter the months: ");
    scanf("%d",&m);
    va = am+t;
    
    for(int i=0;i<m;i++)
    {
        tamt = tamt+va;
        va-=100;
    }
    printf("\nBudddy: %0.f\n",t);
    printf("Total amt: %d",tamt);
    int s = am+t;
    printf("\ntotal amount you need pay with buddy is : %d",s);
    return 0;
}