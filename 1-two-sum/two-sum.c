/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* pair = (int *)malloc(sizeof(int) * 2);
    for (int i = 0; i < numsSize; i++) {
        for (int j = 0; j < numsSize; j++) {
            if ((i != j) && (nums[j] == (target - nums[i]))) {
                pair[0] = i;
                pair[1] = j;
                *returnSize = 2;
                return pair;
            }
        }
    }
    *returnSize = 0;
    return NULL;
}