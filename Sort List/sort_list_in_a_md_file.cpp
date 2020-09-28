
/*
Author : 5hifaT
github:https://github.com/jspw
linkedin : https://www.linkedin.com/in/mehedi-hasan-shifat-2b10a4172/
Stackoverflow : https://stackoverflow.com/story/jspw 
*/


#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string str;
    vector<string>v;
    while(getline(cin,str)){
        v.push_back(str);
    }

    sort(v.begin(),v.end());

    for(int i=0;i<v.size();i++){
        cout<<v[i]<<endl;
    }



    return 0;
}
