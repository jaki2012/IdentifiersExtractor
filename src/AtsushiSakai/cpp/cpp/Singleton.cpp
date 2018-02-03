/**
 * @file: Singleton.cpp
 *
 * @brief: Singleton model of the Design pattern.
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
 *  @brief  ( )
 */
class Singleton{
  public:
    /**
     *  @brief  
     */
    static Singleton* GetInstance(void){
      static Singleton singleton;  
      return &singleton;
    }

    /**
     *  @brief Num 
     */
    void SetNum(int num){num_=num;}

    /**
     *  @brief Num 
     */
    int GetNum(void){return num_;}
    
  private:
    Singleton(){}// private 
    Singleton(const Singleton& r){}			//  private  
    Singleton &operator=(const Singleton& r); //  private  
    int num_;// 
};

int main(void){
  cout<<"Singleton Pattern Sample Start!!"<<endl;

  // 
  Singleton *singleton1=Singleton::GetInstance();
  Singleton *singleton2=Singleton::GetInstance();

  // 
  singleton1->SetNum(10);

  // 
  cout<<"Singleton1:"<<singleton1->GetNum()<<endl;
  cout<<"Singleton2:"<<singleton2->GetNum()<<endl;

  return 0;
}
