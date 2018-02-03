/**
 * @file: Observer.cpp
 *
 * @brief: Observer model of the Design pattern.
 *
 * @author: Atsushi Sakai 
 *
 * @copyright (c): 2014 Atsushi Sakai
 *
 * @license : GPL Software License Agreement
 **/

//#include <time.h>// 

#include <iostream>
#include <vector>
#include <random>
#include <ctime>

using namespace std;

class NumberGenerator;

/**
 *  @brief  
 **/
class Observer{
  public:
    // Notify 
    virtual void Update(NumberGenerator *generator)=0;
};

/**
 *  @brief  
 **/
class NumberGenerator{
  public:
   /**
    *  @brief Observer 
    */
    void AddObserver(Observer *observer){
      observers_.push_back(observer);
    }

   /**
    *  @brief  Observer  
    */
    void Notify(void){
      int nobserver=observers_.size();
      for(int io=0;io<nobserver;io++){
        // Update 
        observers_[io]->Update(this); 
      }
    }

    virtual int GetNum(void)=0;
    virtual void Generate(void)=0;

  private:
    vector<Observer*> observers_;// 
};

/**
 *  @brief  
 */
class DigitObserver:public Observer{
  public:
   /**
    *  @brief Update 
    */
    void Update(NumberGenerator *generator){
      cout<<"DigitObserver:"<<generator->GetNum()<<endl;
    }
  private:
};

/**
 *  @brief  
 */
class StarObserver:public Observer{
  public:
   /**
    *  @brief Update * 
    */
    void Update(NumberGenerator *generator){
      cout<<"DigitObserver:";
      for(int i=0;i<generator->GetNum();i++){
        cout<<"*";
      }
      cout<<endl;
    }
  private:
};


/**
 *  @brief  
 **/
class RandomNumberGenerator:public NumberGenerator{
  public:
    RandomNumberGenerator(void){}

   /**
    *  @brief   
    */
    int GetNum(void){return number_;}

   /**
    *  @brief  10  
    */
    void Generate(void){
      //  
      //  
      mt19937 engine_(static_cast<unsigned int>(time(nullptr)));
      uniform_int_distribution<int> dist(0,100);
      for(int i=0;i<10;i++){
        number_=static_cast<int>(dist(engine_));
        Notify();//  
      }
    }
    
  private:
    int number_;// 
    mt19937 engine_;// 
};


int main(void){
  cout<<"Observer Pattern Sample Start!!"<<endl;

  NumberGenerator* generator=new RandomNumberGenerator();
  Observer *ob1=new DigitObserver();
  Observer *ob2=new StarObserver();

  // 
  generator->AddObserver(ob1);
  generator->AddObserver(ob2);
  
  // 
  generator->Generate();

  return 0;
}
