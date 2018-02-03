/**
 * @file: Memento.cpp
 *
 * @brief: Memento model of the Design pattern.
 *
 * @author: Atsushi Sakai 
 *
 * @copyright (c): 2014 Atsushi Sakai
 *
 * @license : GPL Software License Agreement
 **/

#include <iostream>

using namespace std;

/**
 *  @brief  Memento  
 **/
class Memento{
  public:
    Memento(int num):num_(num){}
    int GetNum(void){return num_;}
  private:
    int num_;
};

/**
 *  @brief  
 **/
class Number{
  public:
    Number(int num):num_(num){}
    int GetNum(void){return num_;}
    void Increment(void){num_++;}

   /**
    *  @brief  Memeto 
    */
    Memento* CreateMemento(void){
      Memento *memento=new Memento(num_);
      return memento;
    }

   /**
    *  @brief Memento 
    */
    void RestoreMemento(Memento *memento){
      num_=memento->GetNum();
    }

  private:
    int num_;
};

int main(void){
  cout<<"Memento Pattern Sample Start!!"<<endl;

  // 
  Number number(100);
  Memento* memento=number.CreateMemento();// 
  for(int i=0;i<100;i++){
    cout<<number.GetNum()<<endl;
    number.Increment();// 
    if(number.GetNum()%10==0){
      cout<<"Restore"<<endl;
      number.RestoreMemento(memento);
    }
  }

  return 0;
}
