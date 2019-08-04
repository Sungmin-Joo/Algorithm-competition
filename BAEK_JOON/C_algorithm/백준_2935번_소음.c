#include <stdio.h>
#include <string.h>

int main(){
  char a[101]={0,},b[101]={0,},c;
  int i,dif,l_a,l_b;
  scanf("%s",a);
  scanf(" %c",&c);
  scanf("%s",b);
  l_a=strlen(a);
  l_b=strlen(b);
  if(l_a>l_b){
    dif=l_a-l_b;
  } else {
    dif=l_b-l_a;
  }

  if(c=='*'){
    putchar('1');
    for(i=0;i<(l_a+l_b)-2;i++){
      putchar('0');
    }
  }
  else{
    if(l_a==l_b){
      putchar('2');
      for(i=0;i<l_a-1;i++){
        putchar('0');
      }
    } else {
      putchar('1');
      for(i=1;i<dif;i++){
        putchar('0');
      }
      if(l_a>l_b){
        printf("%s",b);
      } else {
        printf("%s",a);
      }
    }
  }
  return 0;
}
