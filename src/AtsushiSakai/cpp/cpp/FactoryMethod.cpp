/**
 * @file: FactoryMethod.cpp
 *
 * @brief: Factory Method model of the Design pattern.
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
 *  @brief Product 
 */
class Product{
  public:
    virtual void Use(void)=0;
};

/**
 * @brief IDCard 
 */
class IDCard: public Product{
  public:
    /**
     *  @brief  
     */
    IDCard(string name){
      ownerName_=name;
    }

    /**
     *  @brief IDCard 
     */
    void Use(void){
      cout<<" "<<ownerName_<<" IDCard ."<<endl;
    }

  private:
    string ownerName_;// 
};

/**
 * @brief BusinessCard 
 */
class BusinessCard: public Product{
  public:
    /**
     *  @brief  
     */
    BusinessCard(string name){
      ownerName_=name;
    }

    /**
     *  @brief BusinessCard 
     */
    void Use(void){
      cout<<" "<<ownerName_<<" BusinessCard ."<<endl;
    }

  private:
    string ownerName_;// 
};

/**
 *  @brief  Factory 
 */
class Factory{
  public:
    /**
     *  @brief Product 
    */
    Product* Create(string type,string name){
      Product* p=CreateProduct(type,name); 
      return p;
    }

  private:
    /**
     *  @brief Product 
     *  @param type Product 
     *  @param name Product 
     */
    virtual Product* CreateProduct(string type, string name)=0;
};

/**
 *  @brief  Factory 
 */
class StationeryFactory: public Factory{
  public:
    /**
     * @brief Product 
     */
    Product* CreateProduct(string type,string name){
      if(type=="BusinessCard"){
        return new BusinessCard(name);
      }
      else if(type=="IDCard"){
        return new IDCard(name);
      }
      else{
        cout<<"Unknown Stationery:"<<type<<endl;
        return 0;
      }
    }
};

int main(void){
  cout<<"Factory Method Pattern Sample Start!!"<<endl;

  //Factory 
  Factory *factory=new StationeryFactory(); 

  //Factory 
  Product *item1  = factory->Create("BusinessCard","TOM");
  Product *item2  = factory->Create("BusinessCard","SAM");
  Product *item3  = factory->Create("IDCard","RAI");
  Product *item4  = factory->Create("IDCard","TED");

  // 
  item1->Use();
  item2->Use();
  item3->Use();
  item4->Use();

  return 0;
}
