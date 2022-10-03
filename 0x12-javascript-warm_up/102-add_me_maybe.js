#!/usr/bin/node
exports.addMeMaybe = (nb, func) => {
  nb++;
  func(nb);
};
