/**
 * @file: IteratorSample.cpp
 *
 * @brief: Iterator model of the Design pattern.
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
class IteratorInterface;
class AggregateInterface;

/**
 * @brief  
 */
class Book{
  public:
    /**
     * 
     */
    void SetName(string name){
      name_=name;
    }

    /**
     * @brief  
     */
    string GetName(void){
      return name_;
    }

  private:
    string name_;// 
};

/**
 *  @brief  
 */
class IteratorInterface{
  public:
    virtual bool IsLast(void)=0;// 
    virtual Book Next(void)=0;// 
};

/**
 *  @brief  
 */
class AggregateInterface{
  public:
    // 
    virtual IteratorInterface* Iterator(void)=0;
};


/**
 *  @brief  
 *          Aggregate 
 **/
class BookShelf : public AggregateInterface{
  public:
    /**
     *  @brief  
     *          
     *  @param maxsize  
     **/
    BookShelf(int maxsize){
      books_.resize(maxsize);
      nBooks=0;// 
    }

    /**
     * @brief  
     * @param index  
     */
    Book GetBookAt(int index){
      return books_[index];
    }

    /**
     * @brief  DB 
     * @param book  
     */
    void AppendBook(Book book){
      books_[nBooks]=book;//DB 
      nBooks++;// 
    }

    /**
     * @brief DB 
     */
    int GetNBooks(void){return nBooks;}

    /**
     * @brief BookShelf 
     */
    IteratorInterface* Iterator(void);

  private:
    vector<Book> books_;// DB
    int nBooks;// 
};

/**
 * @brief BookShelf 
 */
class BookShelfIterator:public IteratorInterface{
  public:
    BookShelfIterator(BookShelf bookShelf)
    :index_(0),bookShelf_(bookShelf)
    {}

    bool IsLast(void);
    Book Next(void);

  private:
    BookShelf bookShelf_;
    int index_;// 
};

/**
 * @brief BookShelf 
 */
IteratorInterface* BookShelf::Iterator(void){
  return new BookShelfIterator(*this);
}



/**
 * @brief  
 */
bool BookShelfIterator::IsLast(void){
  if(index_<(bookShelf_.GetNBooks())){
      return true;
  }
  else{
      return false;
  }
}

/**
 * @brief  
 *         
 */
Book BookShelfIterator::Next(void){
  Book book=bookShelf_.GetBookAt(index_);
  index_++;
  return book;
}

int main(void){
  std::cout<<"Iterator Sample Start!!"<<std::endl;

  // 
  BookShelf bookShelf(5);

  // 
  Book book1;
  book1.SetName("Code Complete");
  bookShelf.AppendBook(book1);

  Book book2;
  book2.SetName("Agile Samurai");
  bookShelf.AppendBook(book2);

  Book book3;
  book3.SetName("Effective C++");
  bookShelf.AppendBook(book3);

  // 
  IteratorInterface *it=bookShelf.Iterator();

  while(it->IsLast()){
    Book book=it->Next();
    cout<<book.GetName()<<endl;
  }

  return 0;
}
