/**
 * @file: Builder.cpp
 *
 * @brief: Builder model of the Design pattern.
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
 * @brief Builder 
 */
class Builder{
  public:
    /**
     *  @brief  
     */
    virtual void MakeHeader(string &text_)=0;

    /**
     *  @brief MainText 
     */
    virtual void MakeMainText(string maintext, string &text_)=0;

    /**
     *  @brief Footer 
     */
    virtual void MakeFooter(string &text_)=0;
};

/**
 *  @brief PlainText 
 */
class PlainTextBuilder:public Builder{

  void MakeHeader(string &text_){
    text_+="----------\n";
  }

  void MakeMainText(string maintext, string &text_){
    text_+="|"+maintext+"|\n";
  }

  void MakeFooter(string &text_){
    text_+="----Fin---\n";
  }

};

/**
 *  @brief PlainText 
 */
class GorgeousTextBuilder:public Builder{

  void MakeHeader(string &text_){
    text_+="*********\n";
  }

  void MakeMainText(string maintext, string &text_){
    text_+="*"+maintext+"*\n";
  }

  void MakeFooter(string &text_){
    text_+="***Fin***\n";
  }

};

/**
 *  @brief  
 */
class Director{
  public:
    Director(){}

    /**
     * @brief  
     */
    void Construct(void){
      builder_->MakeHeader(text_);
      builder_->MakeMainText(" ",text_);
      builder_->MakeFooter(text_);
    }

    /**
     * @brief  
     */
    const string& GetText(void){
      return text_;      
    }

    /**
     * @brief Builder 
     */
    void SetBuilder(Builder* builder){
      builder_=builder;
    }

  private:
    Builder* builder_;// Builder 
    string text_;// 
};

/**
 *  @brief Main
 */
int main(int argc,char *argv[]){
  cout<<"Builder Pattern Sample Start!!"<<endl;

  // 
  if(argc<2){
    cout<<"Add Command-line parameter"<<endl;
    return 0;// 
  }

  string arg=argv[1];// 

  Director director;// 

  if(arg=="plain"){
    cout<<"Create Plain Text"<<endl;
    PlainTextBuilder plain;
    director.SetBuilder(&plain);
  }
  else if(arg=="gorgeous"){
    cout<<"Create Gorgeous Text"<<endl;
    GorgeousTextBuilder gorg;
    director.SetBuilder(&gorg);
  }
  else{// 
    cout<<"Invalid text mode.Plase use plain or gorgeous"<<endl;
    return 0;
  }

  director.Construct();// 
  string text=director.GetText();// 
  cout<<text<<endl;

  return 0;
}
