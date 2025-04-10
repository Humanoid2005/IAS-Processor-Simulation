#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int main(){
    map<string, int> m{
        {"LOAD MQ",00001010},
        {"LOAD MQ,M(X)",00001001},
        {"STOR M(X)",00100001},
        {"LOAD M(X)",00000001},
        {"LOAD -M(X)",00000010},
        {"LOAD |M(X)|",00000011},
        {"LOAD -|M(X)|",00000100},
        {"JUMP M(X,0:19)",00001101},
        {"JUMP M(X,20:39)",00001110},
        {"JUMP + M(X,0:19)",00001111},
        {"JUMP + M(X,20:39)",00010000},
        {"ADD M(X)",00000101},
        {"ADD |M(X)|",00000111},
        {"SUB M(X)",00000110},
        {"SUB |M(X)|",00001000},
        {"MUL M(X)",00001011},
        {"DIV M(X)",00001100},
        {"LSH",00010100},
        {"RSH",00010101},
        {"STOR M(X,8:19)",00010010},
        {"STOR M(X,28:39)",00010011},
        {"DECR",00011000},
        {"COMP",00011110},
        {"HALT",00000000},
    };
    string filename = "inputfile.txt";
    ifstream inputfile(filename); 
    string line;
    vector<string> v;
    vector<string> binaryV;
    while(getline(inputfile, line)){
        v.push_back(line);
    }
    for(string g : v){
        vector<string> v_words;
        stringstream a(g);
        string word;
        while(a >> word){
            v_words.push_back(word);
        }
        string extractednum;
        vector<int> v_num;
        for(char c : g){
            if(isdigit(c)){
                extractednum += c; 
            }
            else if(!extractednum.empty()){
                //cout << extractednum << endl;
                v_num.push_back(stoi(extractednum));
                extractednum.clear();

            }
        
        }  
        string bin_str;
        if(v_words[0] == "LOAD"){
            if(v_words[1] == "MQ"){
                bin_str = bin_str + "00001010";
            }
            else if(v_words[1][1] == '('){
                bin_str = bin_str + "00000001";
            }
            else if(v_words[1][0] == '-'){
                bin_str = bin_str + "00000010";
            }
            else if(v_words[1][0] == '-' && v_words[1][1] == '|'){
                bin_str = bin_str + "00000100";
            }
            else if(v_words[1][0] == '|'){
                bin_str = bin_str + "00000011";
            }
            else if(v_words[1][0] == 'M' && v_words[1][2] == ','){
                bin_str = bin_str + "00001001";
            }
            
            
        }
        else if(v_words[0] == "HALT"){
            bin_str = bin_str + "00000000";
        }
        else if(v_words[0] == "RSH"){
            bin_str = bin_str + "00010101";
        }
        else if(v_words[0] == "LSH"){
            bin_str = bin_str + "00010100";
        }
        else if(v_words[0] == "ADD"){
            if(v_words[1][0] == 'M'){
                bin_str = bin_str + "00000101";
            }
            else if(v_words[1][0] == '|'){
                bin_str = bin_str + "00000111";
            }
        }
        else if(v_words[0] == "SUB"){
            if(v_words[1][0] == 'M'){
                bin_str = bin_str + "00000110";
            }
            else if(v_words[1][0] == '|'){
                bin_str = bin_str + "00001000";
            }
        }
        else if(v_words[0] == "MUL"){
            bin_str = bin_str + "00001011";
        }
        else if(v_words[0] == "DIV"){
            bin_str = bin_str + "00001100";
        }
        else if(v_words[0] == "DECR"){
            bin_str = bin_str + "00011000";
        }
        else if(v_words[0] == "COMP"){
            bin_str = bin_str + "00011110";
        }
        else if(v_words[0] == "JUMP+"){
            if(v_words[1][v_words[1].size()-3] == '1'){
                bin_str = bin_str + "00001111";
            }
            else if(v_words[1][v_words[1].size() - 3] == '3'){
                bin_str = bin_str + "00010000";
            }
        }
        else if(v_words[0] == "JUMP"){
            if(v_words[1][v_words[1].size() - 3] == '1'){
                bin_str = bin_str + "00001101";
            }
            else if(v_words[1][v_words[1].size() - 3] == '3'){
                bin_str = bin_str + "00001110";
            }
        }
        else if(v_words[0] == "STOR"){
            if(v_words[1][v_words[1].size() - 3] == '1'){
               bin_str = bin_str + "00010010";
            }
            else if(v_words[1][v_words[1].size() - 3] == '3'){
                bin_str = bin_str + "00010011";
            }
            else{
                bin_str = bin_str + "00100001";
            }  
        }
        /*bitset<12> bin_rep(v_num[0]);
        string binaryRep;
        for(int i = 0; i < 12; i++){
            binaryRep = binaryRep +  (char)(bin_rep[i]);
        }
        cout << binaryRep;*/
        string binarystr = bitset<12>(v_num[0]).to_string();
        bin_str = bin_str + binarystr;


        if(v_words[2] == "LOAD"){
            if(v_words[3] == "MQ"){
                bin_str = bin_str + "00001010";
            }
            else if(v_words[3][1] == '('){
                bin_str = bin_str + "00000001";
            }
            else if(v_words[3][0] == '-'){
                bin_str = bin_str + "00000010";
            }
            else if(v_words[3][0] == '-' && v_words[1][1] == '|'){
                bin_str = bin_str + "00000100";
            }
            else if(v_words[3][0] == '|'){
                bin_str = bin_str + "00000011";
            }
            else if(v_words[3][0] == 'M' && v_words[1][2] == ','){
                bin_str = bin_str + "00001001";
            }
            
            
        }
        else if(v_words[2] == "HALT"){
            bin_str = bin_str + "00000000";
        }
        else if(v_words[2] == "RSH"){
            bin_str = bin_str + "00010101";
        }
        else if(v_words[2] == "LSH"){
            bin_str = bin_str + "00010100";
        }
        else if(v_words[2] == "ADD"){
            if(v_words[3][0] == 'M'){
                bin_str = bin_str + "00000101";
            }
            else if(v_words[3][0] == '|'){
                bin_str = bin_str + "00000111";
            }
        }
        else if(v_words[2] == "SUB"){
            if(v_words[3][0] == 'M'){
                bin_str = bin_str + "00000110";
            }
            else if(v_words[3][0] == '|'){
                bin_str = bin_str + "00001000";
            }
        }
        else if(v_words[2] == "MUL"){
            bin_str = bin_str + "00001011";
        }
        else if(v_words[2] == "DIV"){
            bin_str = bin_str + "00001100";
        }
        else if(v_words[2] == "DECR"){
            bin_str = bin_str + "00011000";
        }
        else if(v_words[2] == "COMP"){
            bin_str = bin_str + "00011110";
        }
        else if(v_words[2] == "JUMP+"){
            if(v_words[3][v_words[3].size()-3] == '1'){
                bin_str = bin_str + "00001111";
            }
            else if(v_words[3][v_words[3].size() - 3] == '3'){
                bin_str = bin_str + "00010000";
            }
        }
        else if(v_words[2] == "JUMP"){
            if(v_words[3][v_words[3].size() - 3] == '1'){
                bin_str = bin_str + "00001101";
            }
            else if(v_words[3][v_words[3].size() - 3] == '3'){
                bin_str = bin_str + "00001110";
            }
        }
        else if(v_words[2] == "STOR"){
            if(v_words[3][v_words[3].size() - 3] == '1'){
               bin_str = bin_str + "00010010";
            }
            else if(v_words[3][v_words[3].size() - 3] == '3'){
                bin_str = bin_str + "00010011";
            }
            else{
                bin_str = bin_str + "00100001";
            }  
        }
        /*bitset<12> bin_rep(v_num[0]);
        string binaryRep;
        for(int i = 0; i < 12; i++){
            binaryRep = binaryRep +  (char)(bin_rep[i]);
        }
        cout << binaryRep;*/
        //string binarystr = bitset<12>(200).to_string();
        //bin_str = bin_str + binarystr;
        if(v_words[0] == "JUMP" || v_words[0] == "JUMP+" || (v_words[0] == "STOR" && (v_words[0][v_words[0].size()-3]=='1' || v_words[0][v_words.size()-3]=='3'))){
            string binarystr1 = bitset<12>(v_num[3]).to_string();
            bin_str = bin_str + binarystr1;
        }
        else if(v_words[2]=="HALT" || v_words[2] == "LSH" || v_words[2] == "RSH" || (v_words[2]== "LOAD" && v_words[3] =="MQ")){
            bin_str = bin_str + "000000000000";
        }
        else{
            string binarystr1 = bitset<12>(v_num[1]).to_string();
            bin_str = bin_str + binarystr1;
        }
        binaryV.push_back(bin_str);
    }

    ofstream outputfile("outputfile.txt");
    for(string i : binaryV){
        outputfile << i << endl;
    }
}


    
    
    

