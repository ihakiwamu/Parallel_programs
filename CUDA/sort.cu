#include <thrust/host_vector.h>
#include <thrust/device_vector.h>
#include <thrust/copy.h>
#include <thrust/sort.h>
#include <thrust/functional.h>
#include <iostream>
#include <random>
#include <time.h>

#define vec_size 1000000

int main() {
  
  std::random_device rnd;
  clock_t start,end;
  int size;

  std::cin >> size;

  thrust::device_vector<int> host_a(size);
  thrust::device_vector<int> device_vec(size);

  // create num's
  for(int i = 0; i < host_a.size(); i++){
    host_a[i] = rnd();
  }

  start = clock();

  thrust::copy(host_a.begin(), host_a.end(), device_vec.begin()); // Copy host -> device
  thrust::sort(device_vec.begin(), device_vec.end()); // Start sort
  thrust::copy(device_vec.begin(), device_vec.end(), host_a.begin()); // Copy device -> host

  end = clock();

  std::cout << (double)(end - start) / (double)CLOCKS_PER_SEC << "sec.\n";

  return 0;
}
