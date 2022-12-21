/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
let floodFill = function (image, sr, sc, color, firstColor = image[sr][sc]) {
  // base cases

  if (
    sr < 0 ||
    sc < 0 ||
    sr >= image.length ||
    sc >= image[0].length ||
    image[sr][sc] !== firstColor ||
    image[sr][sc] == color
  ) {
    return image;
  }

  image[sr][sc] = color;

  floodFill(image, sr - 1, sc, color, firstColor);
  floodFill(image, sr + 1, sc, color, firstColor);
  floodFill(image, sr, sc - 1, color, firstColor);
  floodFill(image, sr, sc + 1, color, firstColor);

  return image;
};
