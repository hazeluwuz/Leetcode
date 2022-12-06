var countBits = function (n) {
  let arr = [0];
  for (let i = 1; i < n + 1; i++) {
    arr.push(arr[Math.floor(i / 2)] + (i % 2));
  }
  return arr;
};