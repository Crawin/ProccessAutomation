#include <iostream>

using namespace std;

class Sample {
    public:
    Sample() {cout<<"new����"<<endl;}
    ~Sample() {cout<<"delete�Ҹ�"<<endl;}
    void go() {cout<<"go"<<endl;}
};

int main()
{
    {
        auto Smart_pointer = make_unique<Sample>();
        Smart_pointer->go();
        cout<<&Smart_pointer<<endl;
        cout<<&(*Smart_pointer)<<endl;
    }
}