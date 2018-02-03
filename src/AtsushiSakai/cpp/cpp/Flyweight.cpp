/**
 * @file: Flyweight.cpp
 *
 * @brief: Flyweight model of the Design pattern.
 *
 * @author: Atsushi Sakai 
 *
 * @copyright (c): 2014 Atsushi Sakai
 *
 * @license : GPL Software License Agreement
 **/

#include <iostream>
#include <vector>
#include <map>

using namespace std;

/**
 *  @brief  
 **/
class CharFactory{
  public:
    string Create(string s){
      return "===="+s+"====";
    }

  private:
};

/**
 *  @brief   
 **/
class GorgeousString{
  public:

    GorgeousString(const string &str){
      CharFactory factory;
      for(int i=0;i<str.length();i++){
        string s=str.substr(i,1);
        string gs;
        //DB 
        if(stringDB_.find(s) == stringDB_.end()){
            gs=factory.Create(s);
            stringDB_[s] = gs;
        }
        else{//DB 
            gs=stringDB_[s];
        }

        gString_.push_back(gs);
      }

      cout<<"DB Size:"<<stringDB_.size()<<endl;
    }

   /**
    *  @brief  
    */
    void Show(void){
      for(int i=0;i<gString_.size();i++){
        cout<<gString_[i]<<endl;
      }
    }

  private:
    vector<string> gString_;      // 
    map<string,string> stringDB_; // DB
};

int main(void){
  cout<<"Flyweight Pattern Sample Start!!"<<endl;

  GorgeousString gString("AABBBC");
  gString.Show();

  return 0;
}
