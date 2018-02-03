/**
 * @file: Composite.cpp
 *
 * @brief: Composite Method model of the Design pattern.
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
 *  @brief   
 **/
class Entry{
  public:
    virtual string* GetName(void)=0;
    virtual int GetSize(void)=0;
    virtual void ShowListInfo(const string& prefix)=0;

    /**
     *  @brief Entry 
     */
    void ShowInfo(const string &prefix){
      cout<<prefix+"/"+*(GetName())+" ["+to_string(GetSize())+"]"<<endl;
    }
};

/**
 *  @brief  
 **/
class File : public Entry{
  public:
    File(const string &name,int size){
      name_=name;
      size_=size;
    }

    string* GetName(void){return &name_;}
    
    int GetSize(void){return size_;}

   /**
    *  @brief   
    */
    void ShowListInfo(const string &prefix){
      ShowInfo(prefix);
    }

  private:
    string name_;
    int size_;
};

/**
 *  @brief  
 **/
class Directory : public Entry{
  public:
    Directory(const string &name){
      name_=name;
    }

    string* GetName(void){return &name_;}
    
   /**
    *  @brief  
    *          
    */
    int GetSize(void){
      int size=0;
      int dsize=directory_.size();
      for(int i=0;i<dsize;i++){
        size+=directory_[i]->GetSize();
      }
      return size;
    }

    /**
     *  @brief  
     */
    void Add(Entry* entry){
      directory_.push_back(entry);
    }

   /**
    *  @brief    
    */
    void ShowListInfo(const string &prefix){
      ShowInfo(prefix);
      int dsize=directory_.size();
      for(int i=0;i<dsize;i++){
        directory_[i]->ShowListInfo(prefix+"/"+*(GetName()));
      }
    }

   /**
    *  @brief  
    *          
    */
    void ShowListInfo(void){
      ShowListInfo("");
    }

  private:
    string name_;// 
    vector<Entry*> directory_;// DB
};

int main(void){
  cout<<"Composite Method Pattern Sample Start!!"<<endl;

  cout<<"Making top directory..."<<endl;
  Directory rootdir("root");
  Directory bindir("bin");
  Directory tmpdir("tmp");
  Directory usrdir("usr");

  // 
  rootdir.Add(&bindir);
  rootdir.Add(&tmpdir);
  rootdir.Add(&usrdir);
  
  // 
  File vim("vim",100);
  File git("git",1000);
  bindir.Add(&vim);
  bindir.Add(&git);

  rootdir.ShowListInfo();// 

  cout<<"Making User directory..."<<endl;
  Directory tomdir("Tom");
  File avi("123.avi",100000);
  usrdir.Add(&tomdir);
  tomdir.Add(&avi);

  rootdir.ShowListInfo();// 

  return 0;
}
