/**
 * @file: Command.cpp
 *
 * @brief: Command model of the Design pattern.
 *
 * @author: Atsushi Sakai 
 *
 * @copyright (c): 2014 Atsushi Sakai
 *
 * @license : GPL Software License Agreement
 **/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

/**
 *  @brief Calcurator Command
 **/
class CalcuratorCommand{
  public:
    CalcuratorCommand(string &ope,int num):ope_(ope),num_(num){}

    string ope_;
    int num_;
  private:
};

/**
 *  @brief  
 **/
class CalculatorEngine{
  public:
    CalculatorEngine(){num_=0;}

   /**
    *  @brief  
    */
    void Operation(CalcuratorCommand *cmd){
      if(cmd->ope_=="+"){
        num_+=cmd->num_;
      }
      else if(cmd->ope_=="-"){
        num_-=cmd->num_;
      }
      else if(cmd->ope_=="*"){
        num_*=cmd->num_;
      }
      else if(cmd->ope_=="/"){
        num_/=cmd->num_;
      }

      cout<<"Calc Result:"<<num_<<"\t(operator:"<<cmd->ope_<<",num:"<<cmd->num_<<")"<<endl;

    }

    /**
     *  @brief  
     */
    void InitNum(void){num_=0;}

  private:
    int num_;
};


/**
 *  @brief  
 **/
class Calcurator{
  public:
    Calcurator(void){
      engine=new CalculatorEngine();
    }

    /**
     *  @brief  
     **/
    void Compute(string &ope,int num){
      CalcuratorCommand *command=new CalcuratorCommand(ope,num);
      engine->Operation(command);
      commandList.push_back(*command);
    }

    /**
     *  @brief Undo 
     **/
    void Undo(void){
      cout<<"Undo"<<endl;
      engine->InitNum();
      for(int i=0;i<(commandList.size()-1);i++){
        engine->Operation(&commandList[i]);
      }
      commandList.pop_back();// 
    }

  private:
    CalculatorEngine *engine;// 
    vector<CalcuratorCommand> commandList;// 
};

int main(void){
  cout<<"Command Pattern Sample Start!!"<<endl;

  Calcurator calc;

  string ope="+";
  calc.Compute(ope,100);
  ope="-";
  calc.Compute(ope,50);
  ope="*";
  calc.Compute(ope,2);

  //Undo 
  calc.Undo();

  cout<<"Recalc"<<endl;
  ope="/";
  calc.Compute(ope,5);

  return 0;
}
