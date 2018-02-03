/**
 * @file: ChainOfResponsibility.cpp
 *
 * @brief: Chain Of Responsibility model of the Design pattern.
 *
 * @author: Atsushi Sakai 
 *
 * @copyright (c): 2014 Atsushi Sakai
 *
 * @license : GPL Software License Agreement
 **/

#include <iostream>
#include <cstdint>

using namespace std;

/**
 *  @brief   
 **/
class Purchase{
  public:
    Purchase(int itemNumber, uint64_t price):
      itemNumber_(itemNumber),
      price_(price){}

    uint64_t GetPrice(void) const {return price_;}

    int GetItemNumber(void) const {return itemNumber_;}

  private:
    int itemNumber_;// 
    uint64_t price_;// 
};

/**
 *  @brief  
 **/
class Approver{
  public:
    Approver(const string &name):name_(name){}

   /**
    *  @brief   
    */
    void SetNext(Approver* next){
      next_=next;
    }

    /**
     *  @brief  
     */
    virtual void Approve(const Purchase &item)=0;

  protected:
    string name_;// 
    Approver* next_;// 
};

/**
 *  @brief Director  
 **/
class Director: public Approver{
  public:
    Director(const string &name):Approver(name){}

    void Approve(const Purchase &item){
      if(item.GetPrice()<100000.0){
        cout<<"Item "<<item.GetItemNumber()<<" is apprived by "<<name_<<endl;
      }
      else{// 
        next_->Approve(item);
      }
    }
    
  private:
};

/**
 *  @brief VicePresident 
 **/
class VicePresident: public Approver{
  public:
    VicePresident(const string &name):Approver(name){}

    void Approve(const Purchase &item){
      if(item.GetPrice()<10000000.0){
        cout<<"Item "<<item.GetItemNumber()<<" is apprived by "<<name_<<endl;
      }
      else{// 
        next_->Approve(item);
      }
    }
    
  private:
};

/**
 *  @brief CEO 
 **/
class CEO: public Approver{
  public:
    CEO(const string &name):Approver(name){}

    void Approve(const Purchase &item){
      if(item.GetPrice()<10000000000.0){
        cout<<"Item "<<item.GetItemNumber()<<" is apprived by "<<name_<<endl;
      }
      else{//CEO Commity 
        cout<<"Item "<<item.GetItemNumber()<<" will be apprived by commity"<<endl;
      }
    }
    
  private:
};

int main(void){
  cout<<"Chain Of Responsibility Pattern Sample Start!!"<<endl;

  // 
  Approver* taro= new Director("taro");
  Approver* ray=  new VicePresident("ray");
  Approver* jobs= new CEO("jobs");

  // chain 
  taro->SetNext(ray);
  ray->SetNext(jobs);

  // 
  Purchase books(1,5000);
  Purchase pc(2,300000);
  Purchase building(3,30000000);
  Purchase campany(4, 90000000000);

  //Director 
  taro->Approve(books);
  taro->Approve(pc);
  taro->Approve(building);
  taro->Approve(campany);

  return 0;
}
