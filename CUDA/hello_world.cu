#include <stdio.h>

__global__ void mykernel(void){
    printf("Hello World from GPU!\n");
}

int main(void){
    mykernel<<<1,1>>>();
    cudaDeviceSynchronize();
    return 0;
}
