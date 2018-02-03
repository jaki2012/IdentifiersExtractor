/**
 * @file: Prototype.cpp
 *
 * @brief: Prototype model of the Design pattern.
 *
 * @author: Atsushi Sakai 
 *
 * @copyright (c): 2014 Atsushi Sakai
 *
 * @license : GPL Software License Agreement
 **/

#include <iostream>
#include <map>

using namespace std;

/**
 *  @brief  
 */
class Decoration{
  public:
    /**
     *  @brief  
     */
    Decoration(string dec){
      decstr_=dec;
    }

    /**
     *  @brief  
     */
    void Use(string str){
      cout<<decstr_<<str<<decstr_<<endl;
    }

  private:
    string decstr_;// 
};

/**
 *  @brief Decoration 
 *         Prototype 
 */
class PrototypeCreator{
  public:
    PrototypeCreator(){}

    /**
     *  @brief  
     */
    void Register(string name, Decoration* dec){
      db_[name]=dec;
    }

    /**
     *  @brief  Key 
     */
    Decoration* GetDecoration(string key){
      return db_[key];
    }

  private:
    map<string,Decoration*> db_;// DB
};

int main(void){
  cout<<"Prototype Pattern Sample Start!!"<<endl;

  // 1
  Decoration dec1("**");
  dec1.Use("Hello");

  // 2
  Decoration dec2("~~~~~~~");
  dec2.Use("Hi");

  //Prototype 
  PrototypeCreator creator;
  creator.Register("TwoStar", &dec1);
  creator.Register("Wave", &dec2);

  // 
  Decoration *TwoStar=creator.GetDecoration("TwoStar");
  Decoration *Wave   =creator.GetDecoration("Wave");

  TwoStar->Use("Good");
  Wave->Use("Bye");

  return 0;
}
