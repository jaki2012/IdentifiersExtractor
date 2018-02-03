/**
 * @file: Mediator.cpp
 *
 * @brief: Mediator model of the Design pattern.
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
 *  @brief Mediator  
 **/
class Mediator{
  public:
    virtual void CreateColleagues(void)=0;
    virtual void ColleageModeChangeed(const string &name)=0;
  private:
};

/**
 *  @brief Colleages 
 **/
class Colleages{
  public:
    Colleages(Mediator *mediator):mediator_(mediator){};
    // 
    virtual void ModeChange(void)=0;
    // Colleage 
    virtual void ReceiveModeChange(const string &name)=0;
  protected:
    Mediator* mediator_;
};

/**
 *  @brief Component A 
 **/
class ComponentA:public Colleages{
  public:
    ComponentA(Mediator *mediator):Colleages(mediator){};

    void ModeChange(void){
      cout<<"ComponentA change mode"<<endl;
      mediator_->ColleageModeChangeed("a");
    }

    void ReceiveModeChange(const string &name){
      cout<<"ComponentA receive mode change from "<<name<<endl;
    }
    
  private:
};

/**
 *  @brief Component B 
 **/
class ComponentB:public Colleages{
  public:
    ComponentB(Mediator *mediator):Colleages(mediator){};

    void ModeChange(void){
      cout<<"ComponentB change mode"<<endl;
      mediator_->ColleageModeChangeed("b");
    }

    void ReceiveModeChange(const string &name){
      cout<<"ComponentB receive mode change from "<<name<<endl;
    }

  private:
};

/**
 *  @brief Component C 
 **/
class ComponentC: public Colleages{
  public:
    ComponentC(Mediator *mediator):Colleages(mediator){};

    void ModeChange(void){
      cout<<"ComponentC change mode"<<endl;
      mediator_->ColleageModeChangeed("c");
    }

    void ReceiveModeChange(const string &name){
      cout<<"ComponentC receive mode change from "<<name<<endl;
    }

  private:
};

/**
 *  @brief Concreate Mediator
 **/
class ConcreteMediator:public Mediator{
  public:
   /**
    *  @brief Colleages 
    */
    void CreateColleagues(void){
      // DB 
      ComponentA *a=new ComponentA(this);
      colleages_["a"]=a;
      ComponentB *b=new ComponentB(this);
      colleages_["b"]=b;
      ComponentC *c=new ComponentC(this);
      colleages_["c"]=c;
    }

    /**
     *  @brief Colleage 
     */
    void ColleageModeChangeed(const string &name){
      // 
      //DB Colleage 
      for (auto it=colleages_.begin();it!=colleages_.end();++it){
        if(it->first!=name){
          it->second->ReceiveModeChange(name);
        }
      }
    }

    /**
     *  @brief  Colleage 
     */
    void ChangeMode(const string &name){
      // 
      for(auto it=colleages_.begin();it!=colleages_.end();++it){
        if(it->first==name){
          it->second->ModeChange();
        }
      }
    }

  private:
    map<string, Colleages*> colleages_;//Colleages DB 
};

int main(void){
  cout<<"Mediator Pattern Sample Start!!"<<endl;

  ConcreteMediator *mediator=new ConcreteMediator;
  mediator->CreateColleagues();

  //a 
  mediator->ChangeMode("a");
  
  //c 
  mediator->ChangeMode("c");

  return 0;
}

