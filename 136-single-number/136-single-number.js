/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let map = {}

    for (let num of nums) {
        if (map[num] !== undefined) delete map[num]
        else map[num] = num
    }

    return Object.values(map)[0]
};