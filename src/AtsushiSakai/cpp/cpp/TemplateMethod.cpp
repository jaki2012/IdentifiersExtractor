/**
 * @file: TemplateMethod.cpp
 *
 * @brief: TemplateMethod model of the Design pattern.
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
 *  @brief  
 */
class AbstractDisplay{
  public:
    // 
    virtual void open(void){};
    // 
    virtual void print(void){};
    // 
    virtual void close(void){};
    
    /**
     *  @brief  
     */
    void display(void){
      open();
      for(int i=0;i<5;i++){
        print();
      }
      close();
    }
};

/**
 *  @brief  
 */
class SimpleDisplay : public AbstractDisplay{
  public:
    SimpleDisplay(string str):str_(str){
      len_=str.length();
    }

    void open(void){
      cout<<"+";
      for(int iw=0;iw<len_;iw++){
        cout<<"-";
      }
      cout<<"+"<<endl;
    }

    void print(void){
      cout<<"|"<<str_<<"|"<<endl;
    }

    void close(void){
      open();
    }
  
  private:
    string str_;
    int len_;
};

/**
 *  @brief  
 */
class GorgeousDisplay : public AbstractDisplay{
  public:
    GorgeousDisplay(string str):str_(str){
      len_=str.length();
    }

    void open(void){
      cout<<"*";
      for(int iw=0;iw<len_;iw++){
        cout<<"=";
      }
      cout<<"*"<<endl;
    }

    void print(void){
      cout<<"#"<<str_<<"#"<<endl;
    }

    void close(void){
      open();
    }
  
  private:
    string str_;
    int len_;
};


int main(void){
  cout<<"TemplateMethod Pattern Sample Start!!"<<endl;

  // 
  AbstractDisplay *sim = new SimpleDisplay("Hello");
  AbstractDisplay *gor = new GorgeousDisplay("Hello");

  sim->display();
  gor->display();

  return 0;
}
