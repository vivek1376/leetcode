#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int compress(vector<char>& chars) {
    char prevch = '\0';
    char digits[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };

    int currcnt = 1;
    int totallen = 0;

    vector<char>::iterator it_chars, it2;

    for (it_chars = chars.begin(), it2 = chars.begin();
         it_chars != chars.end(); ++it_chars) {

      if (prevch) {

        if (prevch == *it_chars) {
          // cout<<"here"<<endl;
          currcnt++;
        } else {

          *it2++ = prevch;
          totallen = totallen + 1;

          if (currcnt > 1) {
            string st(to_string(currcnt));
            vector<char> vec_st(st.begin(), st.end());

            totallen = totallen + vec_st.size();

            for (auto ch2: vec_st) {
              *it2++ = ch2;
            }
          }

          currcnt = 1;
        }
      }

      prevch = *it_chars;
    }

    *it2++ = prevch;
    totallen += 1;

    if (currcnt > 1) {
      string st(to_string(currcnt));
      vector<char> vec_st(st.begin(), st.end());

      totallen = totallen + vec_st.size();

      for (auto ch2: vec_st) {
        //cout << it2;
        *it2++ = ch2;
      }
    }

    chars.resize(totallen);

    return totallen;
  }
};


int main()
{
  Solution sol;

  // vector<char> vin = {'a', 'a', 'b', 'c', 'c', 'c'};
  vector<char> vin = {'a', 'b', 'c', 'c', 'c'};

  sol.compress(vin);

  for(auto ch : vin) {
    cout << ch << " ";
  }
  cout << endl;

  return 0;
}
