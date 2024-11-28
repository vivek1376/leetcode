// leetcode 853

#include <bits/stdc++.h>

using namespace std;

void printProfile(const vector<pair<int, int>>& speedProfile) {
    cout << "SPEED:\n";
    for (auto speed_dist: speedProfile) {
        cout << speed_dist.first << " : " << speed_dist.second << endl; 
    }
    cout << endl;
}


pair<bool, vector<pair<int, int>>> calc_ifCatch_SpeedProfile(int carSpeed,
        int startPos,
        vector<pair<int, int>> speedProfile_carAhead,
        int startPos_carAhead,
        int target
        ) {

    vector<pair<int, int>> newProfile;

    int currSpeed = carSpeed;
    int currPos_car = startPos;
    long dist_car_currWindow = 0;
    /* long dist_carAhead = 0; */
    bool ifCatchUp = false;
    int currPos_carAhead = startPos_carAhead;

    /* auto speedProfile = ifCatchUp_speedProfile.second; */

    for (auto speed_dist: speedProfile_carAhead) {

        if (ifCatchUp) {
            newProfile.push_back(speed_dist);
            continue;
        }

        double timeWindow = (double) speed_dist.second / speed_dist.first;

        if (currSpeed <= speed_dist.first) {
            // car can't catch up the front car in this leg of the profile

            dist_car_currWindow += lround(currSpeed * timeWindow);
            /* dist_carAhead += speed_dist.second; */

            currPos_car += lround(currSpeed * timeWindow);
            currPos_carAhead += speed_dist.second;
            continue;
        }

        // speed is greater, so, at some point this car can
        // potentially catch the car/fleet in front

        int currGap = currPos_carAhead - currPos_car;
        double timeToCatchUp = (double) currGap / (currSpeed - speed_dist.first);

        if (timeToCatchUp > timeWindow) {
            // can't catch up in this window; currSpeed remains unchanged

            dist_car_currWindow += lround(currSpeed * timeWindow);
        } else {
            ifCatchUp = true;
            dist_car_currWindow += lround(currSpeed * timeToCatchUp);
            newProfile.push_back(make_pair(currSpeed, dist_car_currWindow));
            currPos_car += lround(currSpeed * timeToCatchUp);

            // reset
            dist_car_currWindow = 0;

            currSpeed = speed_dist.first;

            double remainingTime = (double) timeWindow - timeToCatchUp;
            // for, the remaining distance, the current car has attained the speed of 
            // the front fleet
            int distWithNewSpeed = lround(currSpeed * remainingTime);
            dist_car_currWindow += distWithNewSpeed;
            currPos_car += dist_car_currWindow;

            if (dist_car_currWindow != 0)
                newProfile.push_back(make_pair(currSpeed, dist_car_currWindow));

            currPos_carAhead += speed_dist.second;
        }
        
        /* dist_carAhead += speed_dist.second; */
    }

    if (!ifCatchUp) {
        newProfile.push_back(make_pair(currSpeed, target - startPos));
    }

    printProfile(newProfile);

    return make_pair(ifCatchUp, newProfile);
}


// 1st member is no. of fleets
// 2nd member is pair(ifCatchUp, speedprofile_currCar)
pair<int, vector<pair<int, int>>> solve_subProblem(
        vector<int>& position,
        vector<int>& speed,
        int ind_currentCar,
        int target) {

    // base cond.
    if (ind_currentCar == position.size() - 1) {
        return make_pair(1, vector<pair<int, int>> {
                make_pair(speed[ind_currentCar], target - position[ind_currentCar])});
    }

    auto sol = solve_subProblem(position, speed, ind_currentCar + 1, target);

    auto numFleet_prev = sol.first;
    auto speedProfile_carAhead = sol.second;

    auto res = calc_ifCatch_SpeedProfile(speed[ind_currentCar], position[ind_currentCar],
            speedProfile_carAhead,
            position[ind_currentCar + 1],
            target);

    auto ifCatchUp_currCar = res.first;


    if (ifCatchUp_currCar == false)
        return make_pair(numFleet_prev + 1, res.second);
    else
        return make_pair(numFleet_prev, res.second);
}


int main()
{
    /* vector<int> position {10, 12}; */
    /* vector<int> speed {20, 10}; */
    /* int target = 100; */

    /* vector<int> position {1, 9, 10}; */
    /* vector<int> speed {2, 30, 4}; */
    /* int target = 100; */

    /* vector<int> position {0, 3, 5, 8, 10}; */
    /* vector<int> speed {1, 3, 1, 4, 2}; */
    /* int target = 12; */

    vector<int> position {0, 2, 4};
    vector<int> speed {4, 2, 1};
    int target = 100;

    auto res = solve_subProblem(position, speed, 0, target);

    cout << "no of fleets: " << res.first << endl;
    return 0;
}
