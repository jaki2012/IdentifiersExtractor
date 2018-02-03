/**
 * @file: Interpreter.cpp
 *
 * @brief: Interpreter model of the Design pattern.
 *
 * @author: Atsushi Sakai 
 *
 * @copyright (c): 2014 Atsushi Sakai
 *
 * @license : GPL Software License Agreement
 **/

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

/**
 *  @brief  
 */
class Context {
  public:
    Context(string input) 
      : input_(input)
        , output_(0)
  {}

   /**
    *  @brief  
    */
    string Input() {
      return input_;
    }

   /**
    *  @brief  
    */
    void SetInput(string input) {
      input_ = input;
    }

   /**
    *  @brief  
    */
    int Output() {
      return output_;
    }

   /**
    *  @brief  
    */
    void SetOutput(int output) {
      output_ = output;
    }

  private:
    string input_;// 
    int output_;  // 
};

/**
 *  @brief  k 
 **/
class Expression {
  public:
   /**
    *  @brief  
    */
    void Interpret(Context* context) {
      //context 
      if(context->Input().empty())
        return;
      

      // 
      if(context->Input().find(Nine()) == 0) {
        context->SetOutput(context->Output() + 9 * Multiplier());
        context->SetInput(context->Input().substr(2));//9 
      } 
      else if(context->Input().find(Four()) == 0) {
        context->SetOutput(context->Output() + 4 * Multiplier());
        context->SetInput(context->Input().substr(2));//4 2 
      } 
      else if(context->Input().find(Five()) == 0) {
        context->SetOutput(context->Output() + 5 * Multiplier());
        context->SetInput(context->Input().substr(1));//5 
      }

      while(context->Input().find(One()) == 0) {//1 
        context->SetOutput(context->Output() + 1 * Multiplier());
        context->SetInput(context->Input().substr(1));
      }

    }

    virtual string One() = 0;
    virtual string Four() = 0;
    virtual string Five() = 0;
    virtual string Nine() = 0;
    virtual int Multiplier() = 0;// 
};

/**
 *  @brief  
 */
class ThousandExpression : public Expression {
  public:
    string One() { return "M"; }
    string Four() { return " "; }
    string Five() { return " "; }
    string Nine() { return " "; }
    int Multiplier() { return 1000; }
};

/**
 *  @brief  
 */
class HundredExpression : public Expression {
  public:
    string One() { return "C"; }
    string Four() { return "CD"; }
    string Five() { return "D"; }
    string Nine() { return "CM"; }
    int Multiplier() { return 100; }
};

/**
 *  @brief  
 */
class TenExpression : public Expression {
  public:
    string One() { return "X"; }
    string Four() { return "XL"; }
    string Five() { return "L"; }
    string Nine() { return "XC"; }
    int Multiplier() { return 10; }
};

/**
 *  @brief  
 */
class OneExpression : public Expression {
  public:
    string One() { return "I"; }
    string Four() { return "IV"; }
    string Five() { return "V"; }
    string Nine() { return "IX"; }
    int Multiplier() { return 1; }
};

int main() {
  cout<<"Interpreter Pattern Sample Start!!"<<endl;

  // 
  string roman = "MCMXVIIII";
  Context context(roman);

  // 
  vector<Expression*> tree;
  tree.push_back(new ThousandExpression());
  tree.push_back(new HundredExpression());
  tree.push_back(new TenExpression());
  tree.push_back(new OneExpression());

  //   Interpret 
  for(int i=0;i<tree.size();i++){
    tree[i]->Interpret(&context);
  }

  // 
  cout << roman << " = " << context.Output() << endl;

  return 0;
}

