/**
 * @file: State.cpp
 *
 * @brief: State model of the Design pattern.
 *
 * @author: Atsushi Sakai 
 *
 * @copyright (c): 2014 Atsushi Sakai
 *
 * @license : GPL Software License Agreement
 **/

#include <iostream>

using namespace std;

class PMState;
class AMState;
class Clock;

/**
 *  @brief State 
 **/
class State{
  public:
    virtual void ShowTime(int time)=0;
  private:
};

/**
 *  @brief  
 **/
class PMState:public State{
  public:
    void ShowTime(int time){
      cout<<"PM"<<(time-12)<<":00"<<endl;
    }

    /**
     *  @brief  
     */
    static PMState* GetInstance(void){
      static PMState singleton;  
      return &singleton;
    }

  private:
};


/**
 *  @brief  
 **/
class AMState:public State{
  public:
    void ShowTime(int time){
      cout<<"AM"<<time<<":00"<<endl;
    }

    /**
     *  @brief  
     */
    static AMState* GetInstance(void){
      static AMState singleton;  
      return &singleton;
    }

  private:
};

/**
 *  @brief   
 **/
class Clock{
  public:
    Clock(void){
      state_=new AMState(); 
    }

    /**
     *  @brief  
     */
    void ShowTime(int time){
      state_->ShowTime(time);
      if(time>=12){
        state_=PMState::GetInstance();
      }
      else{
        state_=AMState::GetInstance();
      }
    }

  private:
    State* state_;
};

int main(void){
  cout<<"State Pattern Sample Start!!"<<endl;

  Clock clock;
  for(int i=0;i<24;i++){
    cout<<i<<":00=";
    clock.ShowTime(i);
  }

  return 0;
}
