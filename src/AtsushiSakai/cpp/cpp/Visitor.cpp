/**
 * @file: Visitor.cpp
 *
 * @brief: Visitor Method model of the Design pattern.
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

// 
class File;
class Directory;

/**
 *  @brief Visitor 
 **/
class Visitor{
  public:
    virtual void Visit(File *file)=0;
    virtual void Visit(Directory *Directory)=0;
  private:
};

/**
 *  @brief Visitor  
 **/
class Element{
  public:
    virtual void Accept(Visitor &v)=0;
  private:
};

/**
 *  @brief   
 **/
class Entry: public Element{
  public:
    virtual string* GetName(void)=0;
    virtual int GetSize(void)=0;

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
    *  @brief Visitor Accept  
    */
    void Accept(Visitor &v){
      v.Visit(this);
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
    *  @brief Visitor Accept  
    */
    void Accept(Visitor &v){
      v.Visit(this);
    }

    vector<Entry*> directory_;// DB
  private:
    string name_;// 
};

/**
 *  @brief Entry Vistor  
 **/
class ListVisitor:public Visitor{
  public:
    /**
     *  @brief File Visit 
     */
    void Visit(File *file){
      file->ShowInfo(str_);
    }

    /**
     *  @brief Directory Visit 
     */
    void Visit(Directory *directory){
      directory->ShowInfo(str_);
      int dsize=directory->directory_.size();
      str_+="/"+*(directory->GetName());
      for(int i=0;i<dsize;i++){
        directory->directory_[i]->Accept(*this);
      }
    }

  private:
    string str_;
};

int main(void){
  cout<<"Visitor Method Pattern Sample Start!!"<<endl;

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

  // 
  rootdir.Accept(*(new ListVisitor()));

  cout<<"Making User directory..."<<endl;
  Directory tomdir("Tom");
  File avi("123.avi",100000);
  usrdir.Add(&tomdir);
  tomdir.Add(&avi);

  // 
  rootdir.Accept(*(new ListVisitor()));

  return 0;
}
