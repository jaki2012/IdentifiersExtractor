/**
 * @file: Strategy.cpp
 *
 * @brief: Strategy model of the Design pattern.
 *
 * @author: Atsushi Sakai 
 *
 * @copyright (c): 2014 Atsushi Sakai
 *
 * @license : GPL Software License Agreement
 **/

#include <iostream>
#include <vector>

using namespace std;

/**
  @brief   
 */
class AbstractMeanCalc{
  public:
    virtual void MeanCalc(const vector<float> &data)=0;
};

/**
  @brief  
 */
class ArithmeticMean : public AbstractMeanCalc{
  public:
    void MeanCalc(const vector<float> &data){
      int ndata=data.size();
      float mean=0.0;
      for(int i=0;i<ndata;i++){
        mean+=data[i];
      }
      mean/=ndata;
      cout<<"ArithmeticMean:"<<mean<<endl;
    }
  private:
};

/**
 * @brief  
 */
class HarmonicMean : public AbstractMeanCalc{
  public:
    void MeanCalc(const vector<float> &data){
      int ndata=data.size();
      float mean=0.0;
      for(int i=0;i<ndata;i++){
        mean+=1.0/data[i];
      }
      mean*=ndata;
      cout<<"HarmonicMean:"<<mean<<endl;
    }
  private:
};

/**
 * @brief    Strategy 
 */
class Calculator{
  public:
    Calculator(AbstractMeanCalc *meanCalc){
      meanCalc_=meanCalc;
    }

   /**
    * @brief  
    */
    void MeanCalc(const vector<float> &data){
      meanCalc_->MeanCalc(data);
    }

  private:
    AbstractMeanCalc *meanCalc_;// 
};

int main(void){
  cout<<"Strategy Method Pattern Sample Start!!"<<endl;

  // 
  vector<float> data{5.2,10.1,40.8};//C++11 

  // 
  Calculator calc(new ArithmeticMean());
  calc.MeanCalc(data);
  
  // 
  Calculator calc2(new HarmonicMean());
  calc2.MeanCalc(data);
  
  return 0;
}
