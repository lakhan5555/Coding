int minJumps(int arr[], int n){
    if(arr[0] == 0){
        return -1;
    }
    int dp[n];
    int a = std::numeric_limits<int>::max();
    dp[0] = 0;
    for(int i = 1;i < n;i ++){
        dp[i] = a;
    }
    for(int i = 1;i < n;i++){
        if((arr[i] == 0) && (i !=(n-1))){
            dp[i] = 0;
        }
        else{
            for(int j = 0;j<i;j++){
                if((i-j)<=arr[j]){
                    if(dp[i]>(dp[j]+1)){
                        dp[i] = dp[j] + 1;
                    }
                }
            }
        }
    }
    if(dp[n-1] == a){
        return -1;
    }
    else{
        return dp[n-1];
    }
}
