/**
 * @file: Decorator.cpp
 *
 * @brief: Foratoractory model of the Design pattern.
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
 **/
class Display{
  public:
    // 
    virtual int GetColumns(void)=0;
    // 
    virtual string GetRawText(void)=0;
    // 
    void Show(void){
      cout<<GetRawText()<<endl;
    }
};

/**
 *  @brief  
 **/
class StringDisplay:public Display{
  public:
    StringDisplay(const string &str):str_(str){}
    int GetColumns(void){return str_.size();}
    string GetRawText(void){return str_;};
  private:
    string str_;// 
};

/**
 *  @brief   
 **/
class Border:public Display{
  public:
    Border(Display *display):display_(display){}
    Display *display_;
};

/**
 *  @brief   
 **/
class SideBorder:public Border{
  public:
    SideBorder(Display *display,string str):Border(display),str_(str){}

    string GetRawText(void){
      return (str_+display_->GetRawText()+str_);
    };

    int GetColumns(void){return display_->GetColumns()+2;}

  private:
    string str_;
};

/**
 *  @brief   
 **/
class FullBorder:public Border{
  public:
    FullBorder(Display *display):Border(display){}

    string GetRawText(void){
      string str=GetLine(display_->GetColumns()+2);
      str+="*"+display_->GetRawText()+"*\n";
      str+=GetLine(display_->GetColumns()+2);
      return str;
    };

    int GetColumns(void){return (display_->GetColumns()+2);}

  private:
    /**
     *  @brief   
     */
    string GetLine(int nCol){
      string str="";
      for(int i=0;i<nCol;i++){
        str+="-";
      }
      str+="\n";
      return str;
    }
};

int main(void){
  cout<<"Decorator Pattern Sample Start!!"<<endl;

  Display *d1=new StringDisplay("HogeHoge");
  cout<<endl;
  d1->Show();

  Display *d2=new SideBorder(d1,"@");
  cout<<endl;
  d2->Show();

  Display *d3=new FullBorder(d2);
  cout<<endl;
  d3->Show();

  return 0;
}
