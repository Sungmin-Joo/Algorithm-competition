#include <stdio.h>
#include <stdlib.h>
int x_i[8] = {1,1,0,-1,-1,-1,0,1};
int y_i[8] = {0,-1,-1,-1,0,1,1,1};


void check(int x, int y, int h, int w, int *arr, int *visited){
  int i,t_x,t_y;

  for(i = 0; i<8;i++){
    t_x = x+x_i[i];
    t_y = y+y_i[i];
    if(((t_x >= 0) && (t_x < w)) && ((t_y >= 0) && (t_y < h))){
      if(*(visited+t_x+t_y*w) == -1){
        if(*(arr+t_x +t_y*w) == 1){
          *(visited+t_x +t_y*w) = 1;
          check(t_x,t_y,h,w,arr,visited);
        }
        else{
          *(visited+t_x+t_y*w) = 0;
        }
      }
    }
  }
}

int main(){
  int w, h, i, cnt,x,y;
  int *arr, *visited;
  while(1){
    scanf("%d %d",&w, &h);
    if(w == 0 && h == 0)
      break;

    arr = malloc(sizeof(int)*w*h);
    visited = malloc(sizeof(int)*w*h);
    cnt = 0;
    for(i=0;i<h*w;i++){
      *(visited+i) = -1;
    }

    for(i=0;i<h*w;i++){
      scanf("%d",arr+i);
    }
    for(i=0;i<h*w;i++){
      if(*(visited+i) == -1){
        if(*(arr+i) == 1){
          cnt++;
          *(visited+i) = 1;
          x=i%w;
          y=i/w;
          check(x,y,h,w,arr,visited);
        }
        else{
          *(visited+i) = 0;
        }


      }
    }
    printf("%d\n",cnt);

    free(arr);
    free(visited);
  }

  return 0;
}
