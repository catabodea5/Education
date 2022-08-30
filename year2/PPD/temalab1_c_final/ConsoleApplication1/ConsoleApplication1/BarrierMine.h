#pragma once

//
// Created by Lazar Ana on 23/10/2021.
//

#ifndef LAB_02_BARRIER_H
#define LAB_02_BARRIER_H


#include <mutex>

class BarrierMine {
public: BarrierMine(int count) : thread_count(count), counter(0), waiting(0)
{}

      void wait() {
          std::unique_lock<std::mutex> lk(m);
          ++counter;
          ++waiting;
          cv.wait(lk, [&] {return counter >= thread_count;});
          cv.notify_one();
          --waiting;
          if (waiting == 0) {
              counter = 0;
          }
          lk.unlock();
      }

private:
    std::mutex m;
    std::condition_variable cv;
    int counter;
    int waiting;
    int thread_count;
};


#endif //LAB_02_BARRIER_H
