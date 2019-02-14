/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
  const output = [];
  let cur = 1;
  for (let i = 0; i < nums.length; i++) {
    output[i] = cur;
    cur *= nums[i];
  }
  cur = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    output[i] *= cur;
    cur *= nums[i];
  }
  return output;
};