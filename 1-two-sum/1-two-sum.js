/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const dict = {};

  for (let i in nums) {
    let remainder = target - nums[i];
    if (dict[remainder]) {
      return [Number(i), Number(dict[remainder])];
    } else {
      dict[nums[i]] = i;
    }
  }
  return null;
};
