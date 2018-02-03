/**
 * @file: Facade.cpp
 *
 * @brief: Facade model of the Design pattern.
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
 *  @brief  A
 **/
class A{
  public:
    void DoSomething(void){
      cout<<"Class A does somthing"<<endl;
    }
  private:
};

/**
 *  @brief  B
 **/
class B{
  public:
    void DoSomething(void){
      cout<<"Class B does somthing"<<endl;
    }
  private:
};

/**
 *  @brief  C
 **/
class C{
  public:
    void DoSomething(void){
      cout<<"Class C does somthing"<<endl;
    }
  private:
};

/**
 *  @brief Class A,B,C Facade  
 **/
class Facade{
  public:
    /**
     * @brief  A,B,C 
     */
    void Do(void){
      a.DoSomething();
      b.DoSomething();
      c.DoSomething();
    }

  private:
    //facade 
    A a;
    B b;
    C c;
};

int main(void){
  cout<<"Facade Pattern Sample Start!!"<<endl;

  // facade 
  Facade facade;
  //facade A,B,C 
  facade.Do();

  return 0;
}
