/**
 * @file: Abstract Facroty.cpp
 *
 * @brief: Abstract Facroty Method model of the Design pattern.
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
 */
class AbstructStapleMeal{
  public:

   /**
    *  @brief   
    */
    virtual void Eat(void)=0;
};

/**
 *  @brief  
 */
class AbstructMainMeal{
  public:

    /**
     *  @brief  
     */
    virtual void Eat(void)=0;
};

/**
 *  @brief  
 */
class AbstructSoup{
  public:

    /**
     *  @brief  
     */
    virtual void Eat(void)=0;
};

/**
 *  @brief  
 */
class AbstructMealFactory{
  public:
    virtual AbstructStapleMeal* CreateStapleMeal(void)=0;
    virtual AbstructMainMeal* CreateMainMeal(void)  =0;
    virtual AbstructSoup* CreateSoup(void)      =0;
};

/**
 *  @brief  
 */
class JapaneaseStapleMeal:public AbstructStapleMeal{
  public:
    void Eat(void){
      cout<<" "<<endl;
    }
};

/**
 *  @brief  
 */
class JapaneaseMainMeal:public AbstructMainMeal{
  public:
    void Eat(void){
      cout<<" "<<endl;
    }
};

/**
 *  @brief  
 */
class JapaneaseSoup:public AbstructSoup{
  public:
    void Eat(void){
      cout<<" "<<endl;
    }
};

/**
 *  @brief  
 */
class JapaneaseMealFactory:public AbstructMealFactory{
  public:
    AbstructStapleMeal* CreateStapleMeal(void){
      AbstructStapleMeal *meal=new JapaneaseStapleMeal;
      return meal;
    }

    AbstructMainMeal* CreateMainMeal(void){
      AbstructMainMeal *meal=new JapaneaseMainMeal;
      return meal;
    }

    AbstructSoup* CreateSoup(void){
      AbstructSoup *meal=new JapaneaseSoup;
      return meal;
    }

};

/**
 *  @brief  
 */
class AmericanStapleMeal:public AbstructStapleMeal{
  public:
    void Eat(void){
      cout<<" "<<endl;
    }
};

/**
 *  @brief  
 */
class AmericanMainMeal:public AbstructMainMeal{
  public:
    void Eat(void){
      cout<<" "<<endl;
    }
};

/**
 *  @brief  
 */
class AmericanSoup:public AbstructSoup{
  public:
    void Eat(void){
      cout<<" "<<endl;
    }
};

/**
 *  @brief   
 */
class AmericanMealFactory:public AbstructMealFactory{
  public:
    AbstructStapleMeal* CreateStapleMeal(void){
      AbstructStapleMeal *meal=new AmericanStapleMeal;
      return meal;
    }

    AbstructMainMeal* CreateMainMeal(void){
      AbstructMainMeal *meal=new AmericanMainMeal;
      return meal;
    }

    AbstructSoup* CreateSoup(void){
      AbstructSoup *meal=new AmericanSoup;
      return meal;
    }
};

int main(void){
  cout<<"Abstract Facroty Pattern Sample Start!!"<<endl;

  cout<<"==== ===="<<endl;

  AbstructMealFactory *factory=new JapaneaseMealFactory();

  AbstructStapleMeal *stapleMeal=factory->CreateStapleMeal();
  stapleMeal->Eat();

  AbstructMainMeal *mainMeal=factory->CreateMainMeal();
  mainMeal->Eat();

  AbstructSoup *soupMeal=factory->CreateSoup();
  soupMeal->Eat();

  cout<<"==== ===="<<endl;

  AbstructMealFactory *factory2=new AmericanMealFactory();

  AbstructStapleMeal *stapleMeal2=factory2->CreateStapleMeal();
  stapleMeal2->Eat();

  AbstructMainMeal *mainMeal2=factory2->CreateMainMeal();
  mainMeal2->Eat();

  AbstructSoup *soupMeal2=factory2->CreateSoup();
  soupMeal2->Eat();

  return 0;
}
