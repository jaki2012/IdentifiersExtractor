/**
 * @file: Adapter.cpp
 *
 * @brief: Adapter model of the Design pattern.
 *
 * @author: Atsushi Sakai 
 *
 * @copyright (c): 2014 Atsushi Sakai
 *
 * @license : GPL Software License Agreement
 **/

#include <iostream>
#include <string>

using namespace std;

/**
 *  @brief  
 */
class PrintInterface{
  public:
    // 
    virtual string Kakko(string str)=0;
    // 
    virtual string DaburuKakko(string str)=0;
};

/**
 *  @brief  Print 
 */
class EnglishPrint{
  public:
    string Brackets(string str){
      return ("["+str+"]");
    }

    string DoubleBrackets(string str){
      return ("[["+str+"]]");
    }
};

/**
 *  @brief  Print 
 */
class JapanesePrint : public PrintInterface{
  public:
    /**
     *  @brief  Blackets( )
     */
    string Kakko(string str){
      return (eng_.Brackets(str));
    }

    /**
     *  @brief  Double Blackets( )
     */
    string DaburuKakko(string str){
      return (eng_.DoubleBrackets(str));
    }

  private:
    EnglishPrint eng_;
};

int main(void){
  std::cout<<"Adapter Pattern Sample Start!!"<<std::endl;

  // 
  EnglishPrint eng;
  cout<<eng.Brackets("Hi!")<<endl;
  cout<<eng.DoubleBrackets("Ho!")<<endl;

  // 
  JapanesePrint jap;
  cout<<jap.Kakko(" !")<<endl;
  cout<<jap.DaburuKakko(" !")<<endl;

  return 0;
}
