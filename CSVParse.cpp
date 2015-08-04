//
//  CSVParse.cpp
//  Leetcode
//
//  Created by Xiangcao Liu on 7/23/15.
//
//

#include <stdio.h>
/*
 
 Assume you're a host on Airbnb.
 Booking request array -
 x = [5,1,1,5]
 x is the array of booking requests
 x[i] is the number of nights requested for i'th booking.
 
 Also, all these requets are back-to-back.
 x[0] Jan 1 (5 nights) Jan 6
 x[1] Jan 6 (1 night) Jan 7
 x[2] Jan 7 (1 night) Jan 8
 ..
 
 You can not accept consecutive requests.
 If you choose i'th request then you can accept i-1 or i+1 request.
 
 Your goal is to maximize the number of nights.
 The maximum nights for [5,1,1,5] is 10 )   // 5,5
 [4,10,5] = 10
 [4,8,5] = 9
 
 
 CSV parser
 
 CSV comma separated vector
 
 CSV data-
 
 a,b,c
 d,e,f
 "d,e","f"
 "d""e",f
 "ab","de""
 """,""","a",b,
 ""ab"",c
 
 "ab,
 
 ""ab"",c invalid
 Table like format
 a|b|c
 d|e|f
 d,e|f
 d"e|f
 ","|a|b|
 "ab"|c
 */
//"",a -> |a

#include <vector>
#include <iostream>
#include <string>
using namespace std;

// To execute C++, please define "int main()"

vector<string> parse(string line){
    int quote = 0;
    vector<string> result;
    string column="";
    bool commaEnding = false;
    for(size_t i = 0;  i < line.size(); ++i){
        if(line[i]=='"'){
            quote++;
            //double quote
            if(quote == 3){
                quote=1;
                column.push_back('"');
            }
            
        }else if(line[i]==','){
            
            if(quote == 1){
                //the comma is within quotes
                column.push_back(line[i]);
            }else{
                result.push_back(column);
                quote = 0;
                column.clear();
                commaEnding = true;
            }
        }else{
            //line[i] is regular character
            column.push_back(line[i]);
        }
    }
    if(column.size() > 0){
        result.push_back(column);
    }
    if(commaEnding){
        result.push_back("");
    }
    
    return result;
    
}

int main() {
    string testinput = "\"a\"\"b\",c,\"\"";
    vector<string> output = parse(testinput);
    for(size_t i=0; i < output.size(); ++i){
        cout<<output[i];
        if(i <output.size()-1)  cout<<"|";
    }
    
    return 0;
}
