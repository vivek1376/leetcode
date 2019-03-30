#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

	vector<vector<int>> result;

	sort(nums.begin(), nums.end());

	int diff, j, k, j_prev;

	for (size_t i = 0; i < nums.size(); i++) {
	    cout << "i: " << i << endl;
	    if (i > 0) {
		if (nums[i] == nums[i-1])
		    continue;
	    }

	    diff = 0 - nums[i];

	    j = i + 1;
	    k = nums.size() - 1;

	    cout << endl;

	    while (j < k) {		
		if (nums[j] + nums[k] == diff) {
		    result.push_back(vector<int>{nums[i], nums[j], nums[k]});

		    j_prev = j;
		    while (j < nums.size() && nums[j] == nums[j_prev])
		     	j++;		   
		    
		} else if (nums[j] + nums[k] < diff)
		    j++;
		else
		    k--;
	    }
	}

        return result;
    }
};

int main()
{
    Solution S;
    vector <int> nums{-1,0,1,2,-1,-4};

    S.threeSum(nums);
    

    return 0;
}
