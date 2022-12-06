var countBits = function (n) {
  let arr = [];
  for (let i = 0; i < n + 1; i++) {
    let curNum = i.toString(2);
    let ones = curNum.split("0").join("");
    arr.push(ones.length);
  }
  return arr;
};