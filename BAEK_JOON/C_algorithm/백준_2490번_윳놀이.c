#include <stdio.h>

int main(){
  int i=4,sum,j=3,n[4];
  while(j--){
    scanf("%d %d %d %d",n,n+1,n+2,n+3);
    sum=n[0]+n[1]+n[2]+n[3];
    if(sum==0){putchar('D');}
    else if(sum==1){putchar('C');}
    else if(sum==2){putchar('B');}
    else if(sum==3){putchar('A');}
    else{putchar('E');}
    putchar('\n');
  }
  return 0;
}
