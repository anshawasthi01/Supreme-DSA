# https://leetcode.com/problems/reorganize-string/

class Solution {
public:
    string reorganizeString(string s) {
        // CodeHelp
        // Method 1 : Priority Queue
        // Method 2 : Greedy ->
        int hashh[26] =  {0};
        for(int i=0;i<s.size();i++){
            hashh[(s[i]) - 'a']++;
        }
        // find the most frequent char
        int max_freq_char;
        int max_freq = INT_MIN;
        for(int i=0;i<26;i++){
            if(hashh[i] > max_freq){
            max_freq = hashh[i];
            max_freq_char = i + 'a';
            }
        }
        int index = 0;
        while(max_freq > 0 && index < s.size()){
            s[index] = max_freq_char;
            max_freq--;
            index += 2;
        }
        if(max_freq != 0){
            return "";
        }
        hashh[max_freq_char - 'a'] = 0;
        // let's place the rest of the characters
        for(int i=0;i<26;i++){
                while(hashh[i] > 0){
                index = index >= s.size() ? 1 : index;
                s[index] = i + 'a';
                hashh[i]--;
                index += 2;
                }
        }
        return s; 
    }
};