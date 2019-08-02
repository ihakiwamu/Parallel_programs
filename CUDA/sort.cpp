#include <vector> 
#include <random>
#include <time.h>
#include <iostream>
#include <algorithm>

#define vec_size 1000000

int main(){

  std::random_device rnd;
  clock_t start,end;
  int size;
  
  std::cin >> size;

  std::vector<int> data(size);

  for(int i = 0; i < data.size(); i++){
    data[i] = rnd();
  }

  start = clock();

  std::sort(data.begin(),data.end());

  end = clock();

  std::cout << (double)(end - start) / (double)CLOCKS_PER_SEC << "sec.\n";

  return 0;
}

